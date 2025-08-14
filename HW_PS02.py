# Задание PS02

# Задание 1: Получение данных
#   1. Импортируйте библиотеку `requests`.
#   2. Отправьте GET-запрос к открытому API (например, [https://api.github.com](https://api.github.com/))
#   с параметром для поиска репозиториев с кодом html.
#   3. Распечатайте статус-код ответа.
# 4. Распечатайте содержимое ответа в формате JSON.

import requests
import pprint


print("Задание 1: Получение данных")
params = {
    'q': 'html'
}
response = requests.get('https://api.github.com/search/repositories', params=params)

print("Статус-код ответа:", response.status_code)
print("Содержимое ответа в формате JSON:")
pprint.pprint(response.json())

print(50*"**")
# Дополнительно проверю, что я писал на JAVA
# Отправка GET-запроса к API GitHub с параметром для поиска репозиториев аккаунта miroleg с кодом Java
params = {
    'q': 'user:miroleg language:java'
}

response = requests.get('https://api.github.com/search/repositories', params=params)
print("Статус-код ответа:", response.status_code)
print("Содержимое ответа в формате JSON:")
pprint.pprint(response.json())


#
# Задание 2: Параметры запрос
# 1. Используйте API, который позволяет фильтрацию данных через URL-параметры
# (например, https://jsonplaceholder.typicode.com/posts).
# 2. Отправьте GET-запрос с параметром `userId`, равным `1`.
# 3. Распечатайте полученные записи.

print(50*"**")
print("Задание 2: Параметры запрос")

# Шаг 1: Отправка GET-запроса с параметром userId=1
url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}
response = requests.get(url, params=params)

if response.status_code == 200:
    # Распечатка полученных записей
    data = response.json()
    for post in data:
        print(post)
else:
    print(f"Ошибка: {response.status_code}")


#
# Задание 3: Отправка данных
# 1. Используйте API, которое принимает POST-запросы для создания новых данных
# (например, https://jsonplaceholder.typicode.com/posts).
# 2. Создайте словарь с данными для отправки (например, `{'title': 'foo', 'body': 'bar', 'userId': 1}`).
# 3. Отправьте POST-запрос с этими данными.
# 4. Распечатайте статус-код и содержимое ответа.

print(50*"**")
print("Задание 3: Отправка данных")
#  Создание данных для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.post(url, json=data)

print("Статус-код ответа:", response.status_code)
print("Содержимое ответа:")
print(response.json())
