
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
webpage_yc = response.text
soup = BeautifulSoup(webpage_yc, "html.parser")
print(soup.prettify())

print("\n")
print("Exercise 1:")
# Find and print all titles of the links:
titles_all = soup.find_all(name="a", class_="titlelink")
for _ in titles_all:
    print(_.string)

print("\n")
print("Exercise 2:")  # Find the first title of the links:
first_article_tag = soup.find(name="a", class_="titlelink")
print(first_article_tag)
print(first_article_tag.string)  # Option 1

first_article_text = first_article_tag.getText()  # Option 2
print(first_article_text)

print("\n")
print("Exercise 3:")  # Print the article link:
print(first_article_tag.get("href"))

print("\n")
print("Exercise 4:")  # Print the article upvote count:
first_article_upvote = soup.find(name="span", class_="score").getText()  # Option 1
print(first_article_upvote)
first_article_upvote = soup.find(name="span", class_="score")  # Option 2
print(first_article_upvote.string)


print("\n")
print("Exercise 5:")  # Get a list of all article texts, links, and their upvote count:
all_articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for _ in all_articles:
    article_texts.append(_.getText())
    article_links.append(_.get("href"))
articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]  # This creates a list.
print(article_texts)
print(article_links)
print(articles_upvotes)  # Integers

print("\n")
print("Exercise 6:")  # Get the title and link for the article with the highest upvote count:
highest_upvote = max(articles_upvotes)
highest_index = articles_upvotes.index(highest_upvote)
print(article_texts[highest_index])
print(article_links[highest_index])
