import bs4
import re


def importDataTexts():

    texts = []

    for index in range(0, 2):

        if index < 10:
            with open('data/reut2-00' + str(index) + '.sgm', 'r', encoding='utf-8') as file:
                text = file.read()
                text = text.replace('\n', ' ')
                # text = re.sub(r'\x.{1,2}', '', text)　未実装(\x**の置換)
                text = re.sub('&.{0,3};', '', text)

        else:
            with open('data/reut2-0' + str(index) + '.sgm', 'r', encoding='utf-8') as file:
                text = file.read()
                text = text.replace('\n', ' ')
                # text = re.sub(r'\x.{1,2}', '', text)　未実装(\x**の置換)
                text = re.sub('&.{0,3};', '', text)

        soup = bs4.BeautifulSoup(text, "html.parser")
        elems = soup.select('body')
        texts.append(elems)

    return texts
