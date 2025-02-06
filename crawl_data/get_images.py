import csv
from random import randint
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import requests
import pyautogui

def get_images(driver, url): 
    driver.get(url)
    time.sleep(randint(1,2))

    close_noti = driver.find_element(By.XPATH, f'//*[@class="tbclose-btn"]')
    close_noti.click()

    # scroll = -1000
    # scroll_times = 10
    # for _ in range(scroll_times):
    #     pyautogui.scroll(scroll)
    #     time.sleep(1)
    scroll_amount = 1000  # Số pixel cuộn mỗi lần
    scroll_times = 20     # Số lần cuộn

    for _ in range(scroll_times):
        # Sử dụng JavaScript để cuộn trang
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(1)



    images = driver.find_elements(By.CLASS_NAME, 'aligncenter')
    time.sleep(5)

    number = len(images)
    print(f'==> URL: {url}')
    print(f'Number of photos on url: {number}')


    for i, img in enumerate(images):
            try:
                img_url = img.get_attribute('src')
                time.sleep(1)
                if img_url:
                    response = requests.get(img_url)
                    time.sleep(1)
                    if response.status_code == 200:
                        with open(f'../data/sex_photos/image_{i}.jpg', 'wb') as f:
                            f.write(response.content)
                            time.sleep(1)
            except Exception as e:
                print(f"Lỗi khi tải ảnh {i}: {str(e)}")
    
    return driver