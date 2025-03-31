from bs4 import BeautifulSoup
import requests

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

date = str(input(
    "Which year do you want to teravel to? Type the date in this format YYYY-MM-DD: "))  # noqa
date_specified_URL = BILLBOARD_URL+date

response = requests.get(url=date_specified_URL)
plain_billboard_website = response.text
soup = BeautifulSoup(plain_billboard_website, "html.parser")

top100_musics = [tag.getText().strip()
                 for tag in soup.select(selector="li ul li h3")]
print(top100_musics)
