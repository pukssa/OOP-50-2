# Импортируем библиотеку requests, которая используется для выполнения HTTP-запросов.
# Она позволяет легко взаимодействовать с веб-ресурсами и API.

import requests

# Пример использования библиотеки requests для отправки GET-запроса на сайт.
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Печатаем статусный код ответа от сервера.
print(f"Status Code: {response.status_code}")

# Печатаем содержимое ответа в формате JSON.
# Это будет вывод содержимого первого поста с сайта jsonplaceholder.
print("Response JSON:")
print(response.json())

# Для работы с API или для получения информации с веб-сайтов эта библиотека является очень полезной.
# Она поддерживает методы GET, POST, PUT, DELETE и другие HTTP-методы.

# skjdflkajsldkjflaksjdlfjalsdflskdjflkajsdklfja;slkdjf;lkasjdfqjwaejhdfjkbjarsdgvjashdf