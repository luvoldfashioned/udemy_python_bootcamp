from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)

movie_archive_site = response.text
soup = BeautifulSoup(movie_archive_site, "html.parser")

movie_titles = [title.getText()
                for title in soup.find_all(name="h3", class_="title")[::-1]]

with open(file="movies.txt", mode="a", encoding='UTF-8') as file:
    for title in movie_titles:
        file.write(title+"\n")
