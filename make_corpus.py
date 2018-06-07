import gensim
from gensim import corpora, models, similarities

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

print('corpus size:' + str(len(corpus)))

topic_N = 4  # トピックの数（これは恣意的に設定できる。対象文書群が大きいなら数字は10にするなど）

lda = gensim.models.ldamodel.LdaModel(
    corpus=corpus, num_topics=topic_N, id2word=dictionary
)

# モデルを保存する
lda.save('model/cf_lda.model')

# 見やすく出力
for i in range(topic_N):
    print("\n")
    print("="*80)
    print("TOPIC {0}\n".format(i))
    topic = lda.show_topic(i)
    for t in topic:
        print("{0:20s}{1}".format(t[0], t[1]))
