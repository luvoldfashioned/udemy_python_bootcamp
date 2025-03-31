from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,  "html.parser")

sitebit_comhead = soup.find_all(name='span', class_="sitebit comhead")
for sites in sitebit_comhead:
    sites.decompose()

title_a_tag = soup.select(selector=".titleline a")
article_titles = []
article_links = []

for title_tag in title_a_tag:
    title = title_tag.getText()
    article_titles.append(title)
    link = title_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0])
                   for score in soup.select(selector=".score")]

upvote_max_index = article_upvotes.index(max(article_upvotes))

best_article_title = article_titles[upvote_max_index]
best_article_link = article_links[upvote_max_index]

print(best_article_title)
print(best_article_link)
print(max(article_upvotes))

# article_link = title_a.get("href")
# subline = soup.select_one(selector=".score")
# article_upvote = subline.getText()

# # import lxml

# with open(file="index.html", encoding="UTF-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# all_anchor_tags = soup.find_all(name="a")

# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
# # heading = soup.find(name="h1", id="name")
# # print(heading)

# # h3_heading = soup.find(name="h3", class_="heading")
# # print(h3_heading)

# name = soup.select_one(selector="#name")
# print(name)
