import requests
import time

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'
d = requests.get(url).json()
token = d["token"]
seconds = d["seconds"]
print(f"Token is {token}, expected execution time: {seconds} seconds")
task = requests.get(url, params={'token': d['token']}).json()
assert task["status"] == "Job is NOT ready", "Task status is not 'Job is NOT ready'"
time.sleep(seconds)
task = requests.get(url, params={'token': d['token']}).json()
assert task["status"] == "Job is ready", "Task status is not 'Job is ready'"
assert task["result"] == "42", "Result is not 42"
print('Job is done')
