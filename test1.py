import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = (webdriver.Google())
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(10)

vacancies = driver.find_elements(By.CSS_SELECTOR, '[data-qa="vacancy-serp-item"]')

parsed_data = []

for vacancy in vacancies:
    try:
        title_element = vacancy.find_element(By.CSS_SELECTOR, 'span.serp-item__title-text').text
        title = title_element.text
#        link = title_element.get_attribute('href')
#        company = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text

        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-labels--cR9OD8ZegWd3f7Mzxe6z').text
        except:
            salary = "Не указана"

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

#    parsed_data.append([title, company, salary, link])
    parsed_data.append([title, salary])

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)