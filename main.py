import re
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main(url, input_image_amount, path=None):
    if path is None or path == "":
        path = "./images/"
    # Using Chrome Driver for the Webscraping
    driver = webdriver.Chrome()
    
    # Set the maximum waiting time (in seconds)
    wait = WebDriverWait(driver, 7)
    
    driver.get(url)
    wait.until(EC.url_to_be(url))
    

    # Getting the columns(generally 2-3)
    elements = []
    elements = driver.find_elements(By.CLASS_NAME, 'vertical-view__column')
    # print(f"elements_size: {len(elements)}")

    image_url = []
    # while the requested amount of images are not scraped yet...
    while len(image_url) < input_image_amount:
        # Scroll down and load images
        # only scroll down two times because the images get unloaded
        for j in range(0, 2):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.6) # wait 600ms for next scroll

        wait.until(EC.presence_of_all_elements_located)

        # Getting the div where the image urls are located
        div_elements = []
        for x in elements:
            # in vertical-view__item there is a src property which containts the image url
            tmp = x.find_elements(By.CLASS_NAME, 'vertical-view__item')
            div_elements.append(tmp)

        # flatting the list because...
        flat_div_elements = [item for sublist in div_elements for item in sublist]
        # print(f"flat_div_size: {len(flat_div_elements)}")

        # Getting the image URL's
        url_finder(flat_div_elements, image_url, input_image_amount)

    print(f"image_url_size: {len(image_url)} \n {image_url}")

    driver.close()

    counter = 1
    scrolller_name = re.search("r/([a-zA-Z0-9]+)[?]", url).group(1)
    for x in image_url:
        # download_image(x, path + scrolller_name + " " + str(counter) + ".jpg") TODO activate me later!!!
        counter += 1

def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download the image.")


def url_finder(flat_div_elements, image_urls, input_image_amount):
    for y in flat_div_elements:
        if len(image_urls) >= input_image_amount:
            return
        foundImage = y.find_element(By.CLASS_NAME, 'vertical-view__media')
        tag_name = foundImage.tag_name

        # print(f'alt?: {foundImage.get_attribute("alt")}')

        # Check if it is an image and not a scroller video ad | usually they only have video ads
        if tag_name == 'img' and foundImage.get_attribute('alt') != 'None':
            imageURL = foundImage.get_attribute('src')
            # if we already have that image continue and dont append to list
            if imageURL in image_urls:
                continue
            image_urls.append(imageURL)


if __name__ == '__main__':
    main("https://scrolller.com/r/cats?sort=top&filter=pictures", 15)
