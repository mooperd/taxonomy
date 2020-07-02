import requests

r = requests.get('http://127.0.0.1:5000/')

unserialised_data = r.json()

for status in unserialised_data:
    print("{} is {}".format(status["name"], status["status"]))