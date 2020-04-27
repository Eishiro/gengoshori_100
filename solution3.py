"""
第3章: 正規表現
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
hreh http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz
1行に1記事の情報がJSON形式で格納される
各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
ファイル全体はgzipで圧縮される
以下の処理を行うプログラムを作成せよ．
"""
import json

#20. JSONデータの読み込み
def json_get_topic(title):
    """
    Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
    問題21-29では，ここで抽出した記事本文に対して実行せよ．
    """
    file_path = "jawiki-country.json"
    with open(file_path,'r', encoding="utf-8") as f:
        json_data = f.readline()
        while json_data:
            wiki_dict = json.loads(json_data)
            if wiki_dict['title'] == title:
                break
        return wiki_dict['text']

def json_get_topic2(title):
    import gzip
    fname = "jawiki-country.json.gz"
    with gzip.open(fname, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == title:
                break
        return data_json['text']

def main():
    #json_get_topic2('イギリス')
    en=json_get_topic2('イギリス')
    print(en)

if __name__ == "__main__":
    main()
