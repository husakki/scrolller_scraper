from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


def main(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)  # Temporary Solution because with the other one I get not code completion :x

    # element = WebDriverWait(driver, 5).until(lambda x: x.find_element(By.CLASS_NAME, 'vertical-view__columns').
    #                                          find_element(By.CLASS_NAME, 'vertical-view__item').
    #                                          find_element(By.CSS_SELECTOR, 'img.vertical-view__media'))

    # Getting the columns(generally 2-3)
    elements = []
    elements = driver.find_elements(By.CLASS_NAME, 'vertical-view__column')

    # Getting the div where the images are located
    div_elements = []
    for x in elements:
        tmp = x.find_elements(By.CLASS_NAME, 'vertical-view__item')
        div_elements.append(tmp)

    # flatting the list
    flat_div_elements = [item for sublist in div_elements for item in sublist]
    
    # Getting the image URL's
    image_url = []
    for y in flat_div_elements:
        tmp = y.find_element(By.CSS_SELECTOR, 'img.vertical-view__media')
        image_url.append(tmp.get_attribute('src'))

    print(image_url)

    driver.close()


if __name__ == '__main__':
    main("https://scrolller.com/r/cats?sort=top&filter=pictures")
