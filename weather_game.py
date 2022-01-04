
from bs4 import BeautifulSoup
import requests 


url = "https://weather.com/weather/tenday/l/El+Paso+TX?canonicalCityId=552876d5a8f59d6b73195d777bad2e41c80efd7366158821b6c62bc0b5537624"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

temperature = doc.find("span", {"class":"styles--temperature--3MBn3"})
print(temperature)

# for container in containers:
#     weather = container.div.span
# print(weather)