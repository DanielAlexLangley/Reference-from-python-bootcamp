
from bs4 import BeautifulSoup

with open("../apps_intermediate_plus/scraping_movies/website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.prettify())

print("\n")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print("\n")
print(soup.a)  # this will give us the first anchor tag
first_anchor_tag = soup.find(name="a")  # find() finds the first one
print(first_anchor_tag)
# What if we wanted to find all anchor tags?

print("\n")
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.getText())
for tag in all_anchor_tags:
    print(tag.get("href"))  # "get" will get the value of any attribute

print("\n")
heading = soup.find(name="h1", id="name")
print(heading)

# This works with a class as well:
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)  # This is called "class_" since "class" is a reserved keyword.
print(section_heading.name)
print(section_heading.get("class"))

print("\n")
# We can search using CSS selectors:
# .select() will give us all matching items.
# .select_one() will give us the first matching item.
company_url = soup.select_one(selector="p a")  # This looks for an "a" tag that sits inside a "p" tag.
print(company_url)
# This also works with class and/or ID in CSS selector.
company_url = soup.select_one(selector="#name")
print(company_url)
headings = soup.select(".heading")  # Searching for a class of "heading".
print(headings)
# This is helpful since many elements you'll want to find will be inside divs that have an "ID",
# so just narrow down on div then drill down on the element you want.
