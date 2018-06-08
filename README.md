# LDA_reuter_news

ロイターニュース記事をダウンロードして
トピック分類を行う

## sample files

    polyglotのサンプル検証（sample/~.py）

## LDA Files

* Howto
1. make_dictionary.py

    body_extract.pyでデータセットから記事部分を抜き出す

    辞書を作成する

1. make_corpus.py

    gensimに辞書を渡してcorpusを作成する
    LDA Modelを構築する

1. run_analyze.py

    構築したモデルにコーパスナンバーを渡して判別する
