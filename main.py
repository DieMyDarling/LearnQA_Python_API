import requests as r

target = 'https://playground.learnqa.ru/api/'

response = r.get(target + 'get_text').text

print(response)
