from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

def setup_driver():
    options = Options()
#    return webdriver.Chrome()

    return webdriver.Firefox(options=options)

def search_wikipedia(driver, query):
    url = f"https://ru.wikipedia.org/wiki/{query.replace(' ', '_')}"
    driver.get(url)
    time.sleep(1)
    if "страница не существует" in driver.page_source.lower():
        print("Статья не найдена.")
        return False
    return True

def get_paragraphs(driver):
    content_div = driver.find_element(By.ID, "bodyContent")
    paragraphs = content_div.find_elements(By.TAG_NAME, "p")
    return [p.text.strip() for p in paragraphs if p.text.strip()]

def get_internal_links(driver):
    content_div = driver.find_element(By.ID, "bodyContent")
    links = content_div.find_elements(By.TAG_NAME, "a")
    internal_links = []
    for link in links:
        href = link.get_attribute("href")
        if href and "/wiki/" in href and ":" not in href:
            text = link.text.strip()
            if text and (href, text) not in internal_links:
                internal_links.append((href, text))
    return internal_links[:10]

def main():
    driver = setup_driver()
    print("Введите запрос для поиска в Википедии:")
    query = input(">> ").strip()

    if not search_wikipedia(driver, query):
        driver.quit()
        return

    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Листать параграфы статьи")
        print("2. Перейти на связанную страницу")
        print("3. Выйти")

        choice = input(">> ").strip()

        if choice == '1':
            paragraphs = get_paragraphs(driver)
            for i, para in enumerate(paragraphs):
                print(f"\n--- Параграф {i+1} ---")
                print(para)
                if i < len(paragraphs) - 1:
                    cont = input("Нажмите Enter для следующего параграфа или 'q' для выхода: ")
                    if cont.lower() == 'q':
                        break
        elif choice == '2':
            links = get_internal_links(driver)
            if not links:
                print("Нет доступных внутренних ссылок.")
                continue
            print("\nВыберите одну из связанных страниц:")
            for idx, (_, text) in enumerate(links):
                print(f"{idx+1}. {text}")
            try:
                sel = int(input(">> ")) - 1
                if sel < 0 or sel >= len(links):
                    print("Неверный выбор.")
                    continue
                new_url = links[sel][0]
                driver.get(new_url)
                time.sleep(1)
            except ValueError:
                print("Введите корректное число.")
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверная команда. Повторите ввод.")

    driver.quit()

if __name__ == "__main__":
    main()