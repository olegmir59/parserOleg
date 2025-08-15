# Сейчас игра получает английское слово и английское определение. Сделайте так, чтобы слова и
# определения этих слов были на русском. Для этого понадобится модуль googletrans

import requests
from bs4 import BeautifulSoup
import googletrans


def translate():
    eng_word = input("Введите английское слово: ")
    # eng_def = input("Введите английское определение: ")
    translator = googletrans.Translator()
    rus_word = translator.translate(eng_word, dest='ru').text
    print(rus_word)

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    # Создаём функцию, чтобы использовать результат функции-словаря
    word_dict = get_english_words()
    word = word_dict.get("english_words")
    word_definition = word_dict.get("word_definition")

    # Переводим слово и определение на русский язык
    translator = googletrans.Translator()
    rus_word = translator.translate(word, dest='ru').text
    rus_definition = translator.translate(word_definition, dest='ru').text

    # Начинаем игру
    print(f"Значение слова - {rus_definition}")
    attempts = 10
    revealed_letters = ['_'] * len(word)
    guessed = False

    for attempt in range(attempts):
        print(f"Попытка {attempt + 1}/{attempts}")
        print("".join(revealed_letters))
        user_guess = input("Что это за слово? ").strip().lower()

        if user_guess == word.lower():
            print("Все верно!")
            guessed = True
            break
        else:
            print(f"Ответ неверный, осталось попыток: {attempts - attempt - 1}")
            if attempt >= 1:  # После второй попытки начинаем открывать буквы
                index = attempt - 1
                if index < len(word):
                    revealed_letters[index] = word[index]
                else:
                    print("Слово слишком короткое для такого количества попыток.")

    if not guessed:
        print(f"Запомни это слово: {word} ({rus_word})")

"""  старая версмя игры


    user = input("Что это за слово? ")
    if user == word:
        print("Все верно!")
    else:
        print(f"Ответ неверный, было загадано это слово - {word}")

    # Создаём возможность закончить игру
    play_again = input("Хотите сыграть еще раз? y/n")
    if play_again != "y":
        print("Спасибо за игру!")
"""

translate()
while True:
    word_game()
    play_again = input("Хотите сыграть еще раз? y/n")
    if play_again != "y":
        print("Спасибо за игру!")
        break

