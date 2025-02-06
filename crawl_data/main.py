from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import randint
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from get_images import get_images

def main():
    chrome = r"./chromedriver-linux64/chromedriver"
    website_url = "https://anhsex.asia/"
    service = Service(chrome)
    
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.set_window_size(1850, 1000)
    driver.set_window_position(10, 10)

    driver.implicitly_wait(5)

    time.sleep(randint(3, 5))
    driver.get(website_url)
    close_noti = driver.find_element(By.XPATH, f'//*[@class="tbclose-btn"]')
    time.sleep(randint(1,2))
    close_noti.click()

    time.sleep(randint(1,2))
    
    df_links = pd.read_csv(r'../data/link.csv')

    time.sleep(randint(1,2))

    for page_index in range(df_links.shape[0]):
        url = df_links["Link"][page_index]
        get_images(driver, url)

        time.sleep(randint(1,2))


    return driver

main()