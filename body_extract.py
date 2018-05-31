import bs4

with open('reut2-000.sgm', 'r', encoding='utf-8') as file:
    text = file.read()

soup = bs4.BeautifulSoup(text, "html.parser")
elems = soup.select('body')
for elem in elems:
    print(elem)