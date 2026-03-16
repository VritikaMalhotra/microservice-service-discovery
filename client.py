import consul
import random
import requests


c = consul.Consul()


services = c.health.service("my-service", passing=True)[1]


instance = random.choice(services)

address = instance['Service']['Address']
port = instance['Service']['Port']


url = f"http://{address}:{port}"
response = requests.get(url)

print(response.text)