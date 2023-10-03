import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content , 'html.parser')


descriptions_raw = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = [description.string for description in descriptions_raw]
titres = [div.find('a').string for div in soup.find_all("div", class_="gem-c-document-list__item-title")]

head = ["titre", "description"]


# with open('data.csv', 'w') as fichier_csv:
#     writer = csv.writer(fichier_csv, delimiter=',')
#     writer.writerow(head)
#     for titre, description in zip(titres,descriptions):
#         writer.writerow([titre, description])


