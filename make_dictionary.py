from polyglot.text import Text
from polyglot.detect import Detector

from body_extract import importDataTexts

import gensim
from gensim import corpora, models, similarities

import pickle
import math

# 文書群（実際にはこういった文書が100万以上あるイメージです）
documents = importDataTexts()
print('extracting nouns')

progress = 0  # 進捗度
count = 0  # 抽出完了数

for doc in documents:

    # 進捗度が0.1変化したらコンソール出力する
    if(math.floor(count / len(documents) * 10 - progress * 10) >= 1):
        progress = count / len(documents)
        print('extracting progress = ' + str(round(progress, 1) * 100) + ' %')

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
    count += 1

words = [x['nouns'] for x in documents]

# 'words' list の保存
f = open('data/dictionary/words_of_nouns_list', 'wb')
pickle.dump(words, f)

print('making dictionary')
dictionary = corpora.Dictionary(words)

# 出現頻度の20回以下の単語は除外
# 5割の文書に出現している単語は除外
dictionary.filter_extremes(no_below=20, no_above=0.5)

# 必要であれば辞書データを保存しておいてください。
dictionary.save_as_text('data/dictionary/dict.txt')

# 保存した辞書のロード
# dictionary = corpora.Dictionary.load_from_text('dict.txt')
