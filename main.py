from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


def main(url, input_image_amount):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(6)  # Temporary Solution because with the other one I get not code completion :x

    # element = WebDriverWait(driver, 5).until(lambda x: x.find_element(By.CLASS_NAME, 'vertical-view__columns').
    #                                          find_element(By.CLASS_NAME, 'vertical-view__item').
    #                                          find_element(By.CSS_SELECTOR, 'img.vertical-view__media'))

    # Getting the columns(generally 2-3)
    elements = []
    elements = driver.find_elements(By.CLASS_NAME, 'vertical-view__column')
    print(f"elements_size: {len(elements)}")
    image_url = []

    while len(image_url) < input_image_amount:
        # Scroll down and load images
        # only scroll down two times because the images get unloaded
        for j in range(0, 2):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

        time.sleep(5)  # Wait for page to load

        # Todo scroll down
        # Todo continue if same image already found
        # Getting the div where the images are located
        div_elements = []
        for x in elements:
            tmp = x.find_elements(By.CLASS_NAME, 'vertical-view__item')
            div_elements.append(tmp)

        # flatting the list
        flat_div_elements = [item for sublist in div_elements for item in sublist]
        print(f"flat_div_size: {len(flat_div_elements)}")
        # Getting the image URL's
        url_finder(flat_div_elements, image_url, input_image_amount)

    print(f"image_url_size: {len(image_url)} \n {image_url}")

    driver.close()


def url_finder(flat_div_elements, image_url, input_image_amount):

    for y in flat_div_elements:
        if len(image_url) >= input_image_amount:
            return
        # TODO check if the image as an 'alt' attribute --> then it an real image and not an ad
        tmp = y.find_element(By.CLASS_NAME, 'vertical-view__media')
        tag_name = tmp.tag_name

        print(f'alt?: {tmp.get_attribute("alt")}')

        if tag_name == 'img' and tmp.get_attribute('alt') != 'None':
            url = tmp.get_attribute('src')
            if url in image_url:
                continue
            image_url.append(url)


if __name__ == '__main__':
    main("https://scrolller.com/r/cats?sort=top&filter=pictures", 30)
