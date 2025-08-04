# PRIOR --> CHECK WEBSITE CAN BE SCRAPED USING ROBOTS.TXT
import requests # allows downloading of html
from bs4 import BeautifulSoup # allows use html data gathered to scrape
import pprint
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

response = requests.get("https://news.ycombinator.com/news")
response2 = requests.get("https://news.ycombinator.com/news?p=2")

soup = BeautifulSoup(response.text, "html.parser")
soup2 = BeautifulSoup(response2.text, "html.parser")

links = soup.select(".titleline > a")
subtext = soup.select(".subtext")
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories(list):
    return sorted(list, key = lambda k:k["votes"], reverse = True)


def create_custom_hn(links, subtext):
    hn = []

    for index, item in enumerate(links):
        title = item.getText()

        href = item.get("href", None)

        vote = subtext[index].select(".score")

        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))

            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})

    return sort_stories(hn)

# def write_to_pdf(stories, file):
#     canva = canvas.Canvas(file, pagesize = letter)
#
#     for story in stories:
#         title = story["title"]
#         link = story["link"]
#         vote = story["votes"]
#
#         line = [f"Title: {title}, Link: {link}, Votes: {vote}"]
#
#     canva.save()
#     print(f"PDF saved as {file}")

output = create_custom_hn(mega_links, mega_subtext)
pprint.pprint(output)

# write_to_pdf(output, file="results.pdf")