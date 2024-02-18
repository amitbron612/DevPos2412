import requests
from faker import Faker
from selenium import webdriver
from time import sleep
# #1
response = requests.get('https://api.github.com/users/avielb/repos')
actual = len(response.json())
expected = 4
assert actual >= expected

#2
fake = Faker()
for i in range (3):
    full_name = fake.name()
    first_name = full_name.split()[0]  # Extract the first word (the first name)
    response = requests.get('https://api.agify.io/?name=' + first_name)
    json_data = response.json()
    age = (json_data['age'])
    assert (0 <= age <= 120)
#3
response = requests.get('http://universities.hipolabs.com/search?country=Israel')
actual = len(response.json())
expected = 5
assert actual > expected

#4
dr = webdriver.Chrome()
dr.get("https://www.ycombinator.com/")
actual = dr.title
expected = "Y Combinator"
assert actual == expected
sleep(15)

#5
dr = webdriver.Chrome()
dr.get("https://hub.docker.com/")
actual = dr.title
expected = "Docker Hub Container Image Library | App Containerization"
assert actual == expected
sleep(15)