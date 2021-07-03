import requests


url = 'https://playground.learnqa.ru/api/homework_cookie'


def test_ex11():
    print(requests.get(url).cookies)
    assert requests.get(url).cookies['HomeWork'] == 'hw_value'

