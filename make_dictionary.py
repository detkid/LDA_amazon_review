from polyglot.text import Text
from polyglot.detect import Detector

from body_extract import importDataTexts

# 文書群（実際にはこういった文書が100万以上あるイメージです）
documents = importDataTexts()
print('extracting nouns')

for doc in documents:
    desc = doc['desc']
    
    # hint_language_code を指定すると’のエラーが出ない。 指定せずworkaroundをとるなら  desc = ''.join(x for x in desc if x.isprintable())
    text = Text(desc, hint_language_code='en')
    nouns = []

    for tag in text.pos_tags:
        word = tag[0]
        word_class = tag[1]

        if word_class != 'NOUN':
            continue

        if len(word) < 3:
            continue

        nouns.append(word.lower())
    doc['nouns'] = nouns

print('making dictionary')
import gensim
from gensim import corpora, models, similarities

words = [x['nouns'] for x in documents]

dictionary = corpora.Dictionary(words)

# 出現頻度の100回以下の単語は除外
# 5割の文書に出現している単語は除外
dictionary.filter_extremes(no_below=20, no_above=0.5)

# 必要であれば辞書データを保存しておいてください。
dictionary.save_as_text('dict.txt')

# 保存した辞書のロード
# dictionary = corpora.Dictionary.load_from_text('dict.txt')
