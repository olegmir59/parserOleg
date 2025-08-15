from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

# Инициализация браузера
browser = webdriver.Chrome()


def search_wikipedia(query):
    # Переходим на главную страницу Википедии
    browser.get("https://ru.wikipedia.org/wiki/Главная_страница")

    # Находим поле поиска и вводим запрос
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    # Ожидаем, пока страница загрузится
    time.sleep(3)

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs):
        print(f"{i + 1}. {paragraph.text}")
  #      input("Нажмите 'Q' - завершить просмотр, 'Enter' - продолжить: ")
        if input("Нажмите 'Q' - завершить просмотр, 'Enter' - продолжить: ").lower() == 'q':
            if i == 0:
                print("Вы достигли начала статьи.")
            else:
                print(f"Вы достигли {i} параграфа.")
            break

def get_random_link():
    browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if "hatnote navigation-not-searchable ts-main" == cl:
            hatnotes.append(element)
    if not hatnotes:
        print("Не удалось найти ссылки для перехода.")
        return

    if hatnotes:
        print("Найдены ссылки для перехода:")
        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
    else:
        print("Не удалось найти ссылки для перехода.")


def main():
    query = "Солнечная система"
#        query = input("Введите запрос для поиска в Википедии (или 'Q' для завершения): ")
    search_wikipedia(query)

    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Ваш выбор (1/2/3): ")

        if choice == '1':
            list_paragraphs()
        elif choice == '2':
            get_random_link()
        elif choice == '3':
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

    browser.quit()


if __name__ == "__main__":
    main()
