from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)
print(html)
doc = BeautifulSoup(html.text, 'html.parser')
content = doc.select('.heading-primary')[0].contents[0]
# Remove Whitespace
cleaned = content.strip()

# courses
courses = doc.select('.heading-25-extrabold.color-black')

print(cleaned)
# print(courses)

for course in courses:
    print(course.contents[0].strip())