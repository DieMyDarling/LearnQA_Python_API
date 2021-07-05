import requests


url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
method = ('GET', 'POST', 'PUT', 'DELETE')

head = requests.head(url, data={'method':'HEAD'}).text
empty_get = requests.get(url, params={}).text
print(head)
print(empty_get)

for i in range(0, 4):
    get = requests.get(url, params={"method": method[i]}).text
    post = requests.post(url, data={"method": method[i]}).text
    put = requests.put(url, data={"method": method[i]}).text
    delete = requests.delete(url, data={"method": method[i]}).text
    print(i, "|", method[i], "|", get,"|",  post,"|",  put,"|",  delete,"|")

    