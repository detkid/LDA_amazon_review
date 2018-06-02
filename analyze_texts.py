from polyglot.text import Text
from polyglot.detect import Detector

from body_extract import importDataTexts

# 文書群（実際にはこういった文書が100万以上あるイメージです）
documents = importDataTexts()

for doc in documents:
    for index in range(380, len(doc)):
        print(index)
        text = doc[index].text
        # hint_language_code を指定すると’のエラーが出ない
        text = Text(text, hint_language_code='en')
        nouns = []

        for tag in text.pos_tags:
            word = tag[0]
            word_class = tag[1]

            if word_class != 'NOUN':
                continue

            if len(word) < 3:
                continue

            nouns.append(word.lower())
