import requests


url = 'https://playground.learnqa.ru/api/homework_header'


def test_ex12():
    print(requests.head(url).headers)
    assert requests.head(url).headers['x-secret-homework-header'] == 'Some secret value', "Couldn't find header"

