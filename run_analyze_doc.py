import gensim
from gensim import corpora, models

import pickle

# 保存したnounsのlistのロード
f = open('data/dictionary/words_of_nouns_list', "rb")
words = pickle.load(f)

# 保存した辞書のロード
dictionary = corpora.Dictionary.load_from_text('data/dictionary/dict.txt')

corpus = []
for word in words:
    bow = dictionary.doc2bow(word)
    corpus.append(bow)

lda = gensim.models.ldamodel.LdaModel.load('model/cf_lda.model')

topic_label = [
    "Company",
    "Profit",
    "Market",
    "Oil"
]

target_record = 1000  # 分析対象のドキュメントインデックス

for topics_per_document in lda[corpus[target_record]]:
    print("{0:30s}{1}".format(
        topic_label[topics_per_document[0]], topics_per_document[1]))
