import requests


url = ' https://playground.learnqa.ru/ajax/api/user_agent_check'

requests.get(url, headers={"User-Agent": "Some value here"})