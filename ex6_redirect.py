import requests


r = requests.get('https://playground.learnqa.ru/api/long_redirect')

redirects = len(r.history)  # Считаем редиректы
print(redirects)

final_url = r.history[-1].url
print(final_url)

