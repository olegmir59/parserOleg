import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация браузера
driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(10)  # Время на загрузку страницы

# Селектор для блока с вакансиями
vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.vacancy-serp-item')

parsed_data = []

for vacancy in vacancies:
    try:
        # Название вакансии и ссылка
        title_element = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link.bloko-link_primary.vacancy-serp-item__title')
        title = title_element.text
        link = title_element.get_attribute('href')

        # Название компании
        company = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link.bloko-link_secondary.vacancy-serp-item__company-name').text

        # Зарплата
        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'span.bloko-header-section-3').text
        except:
            salary = "Не указана"

        parsed_data.append([title, company, salary, link])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

driver.quit()

# Сохранение в CSV
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)
