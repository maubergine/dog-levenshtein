import requests as requests
from lxml import html
from Levenshtein import distance as lev

name = 'Your name here'

r = requests.get('https://www.thekennelclub.org.uk/search/breeds-a-to-z')
page = html.fromstring(r.text)

breeds = list(map(lambda x: x.text, page.xpath("//strong[@class='m-breed-card__title']")))

levenshteined = list(map(lambda x: (x, lev(name, x)), breeds))
sorted = sorted(levenshteined, key=lambda tup: tup[1])

print(*sorted, sep="\n")

