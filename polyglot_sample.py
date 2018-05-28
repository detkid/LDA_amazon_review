from polyglot.detect import Detector
from polyglot.text import Text

t = "Hi! I'm Ken. Great to meet you."
detector = Detector(t)
print(detector)

tokens = Text(t)
print(tokens.words)

for token in tokens.pos_tags:
    print(token)