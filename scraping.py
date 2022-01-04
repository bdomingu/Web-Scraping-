def start():
    print("Guess El Paso's current temperature.")

    answer = input()

    if answer == delete:
        print("You win!")
        exit()

    else:
        print("You lose!")
        exit()


from bs4 import BeautifulSoup
import requests 

source = requests.get("https://weather.com/weather/tenday/l/El+Paso+TX?canonicalCityId=552876d5a8f59d6b73195d777bad2e41c80efd7366158821b6c62bc0b5537624").text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())


temperature = soup.find('span', class_='DailyContent--temp--3d4dn').text
delete = temperature[0:2]

# print(temperature)

start()
