from polyglot.text import Text
from polyglot.detect import Detector

# 文書群（実際にはこういった文書が100万以上あるイメージです）
documents = [
    {
        'desc': 'A beach safe for all those who want a carefree beach holiday. The HBT BELSAFER the HBT brings a mobile vault on the market, which offers a premium value protection with smart additional features.'
    },
    {
        'desc': 'The south curve must stay! The SOUTH CURVE is THE place of active FCC fans. Here come for generations the blue-yellow-white trailer together, showing brilliant choreography, are creative and unmistakable behind their team.'
    },
    {
        'desc': 'Darling4me - Video Dating and dating service on the smartphone. Find your soul mate on the smartphone with just one click on your smartphone. Darling4me is the first truly Video Dating app for your smartphone (Iphone, Ipad and Android). Darling4me dating service does not require lengthy questionnaires and extensive information from you to find your soul mate. They are tired of seeing it on various dating sites on the Internet images of singles that look quite different in reality? They also do not believe that you will find his true love with a questionnaire? Then try just the new Video Dating Darling4me! It has never been easier to find love. Get your partner suggestions from your environment and see with just one click on your smartphone, the videos of the singles that could be suitable for you. Live and real!'
    }
]

for doc in documents:
    desc = doc['desc']
    text = Text(desc)
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
    print(nouns)
