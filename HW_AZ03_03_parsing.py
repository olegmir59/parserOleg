# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные, найти среднюю цену # и вывести ее,
# а также сделать гистограмму цен на диваны

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = (webdriver.Chrome())

url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
time.sleep(3)


svets = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
parsed_data = []

for svet in svets:
    try:
        name_element = svet.find_element(By.CSS_SELECTOR, 'div.lsooF span')
        name = name_element.text
        link = name_element.get_attribute('href')
        price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        url = svet.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([name, price, url])

driver.quit()

with open("divans.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'цена', 'url'])
    writer.writerows(parsed_data)
