from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


def main():
    driver = webdriver.Chrome()

    # open the webpage
    driver.get("https://scrolller.com/r/cats?sort=top&filter=pictures")


if __name__ == '__main__':
    main()
