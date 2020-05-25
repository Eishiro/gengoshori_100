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
import re

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

def json_get_topic2(title):
    import pandas as pd
    df = pd.read_json('ch03/jawiki-country.json.gz', lines=True)
    ukText = df.query('title=="イギリス"')['text'].values[0]
    print(ukText)


#21 カテゴリ名を含む行を抽出
#記事中でカテゴリ名を宣言している行を抽出せよ．
#e.g. [[Category:イギリス|*]]

def get_line_category():
    import re
    with open('england_wiki.txt') as f:
        data = f.readlines()
        category_line = list(filter(lambda x: re.findall(r'Category', x), data))
        print(category_line)
        #for line in category_line:
        #    print(line)



#22. カテゴリ名の抽出
#https://medium.com/better-programming/lambda-map-and-filter-in-python-4935f248593

def get_category_name():
    """
    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
    """
    import re
    with open('england_wiki.txt') as f:
        data = f.readlines()
        category_name = list(map(lambda x: re.findall(r"\[\[Category:(.*)", x), data))
        print(category_name)


def get_category_name2():
    """
    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
    """
    import re
    with open('england_wiki.txt') as f:
        data = f.read()
        # Could process the file line-by-line, but regex on the whole text at once is even easier.
        category_name = re.findall(r"\[\[Category:(.*)", data)
        print(category_name)


#23. セクション構造
def get_structure_level():
    """
    記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
    """
    import re
    with open('england_wiki.txt') as f:
        data = f.read()
        # get section name surrounded by more than 2 '='
        section = re.findall(r"(==+)(.*?)(==+)", data)
        # count the num of '=' and

        for line in section:
            level = len(line[0]) -1
            print('{indent}{section} - {level}' .format(
                indent='\t' * (level - 1), section=line[1], level=level))

        print(level)

def get_structure_level2():
    """
    記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
    """
    with open('england_wiki.txt') as f:
        data = f.read()
        for section in re.findall(r'(==+)(.*?)(==+)', data):
            print(f'{section[1].strip()} \t --{len(section[0]) - 1}')




#24. ファイル参照の抽出
def get_file_link():
    """
    記事から参照されているメディアファイルをすべて抜き出せ．
    """
    with open('england_wiki.txt') as f:
        data = f.read()
        # no need to take file or ファイル　so ?:
        media_file = re.findall(r'\[\[(?:ファイル:|File:)(.+?)\|', data)
        print(media_file)


#25. テンプレートの抽出
def get_template_data():
    """
    記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
    辞書オブジェクトとして格納せよ
    """
    with open('england_wiki.txt') as f:
        data = f.read()
        # the start of the line  is a bar ^|
        template = re.findall(r'^|(.*)\s=\s(.*)', data)
        dict_template = {} #{field, data}
        for field in template:
            dict_template[template[0]] = template[1]

        print(template)
def main():

    #json_get_topic2('イギリス')
    #get_line_category()
    print("-------------")
    get_template_data()

with open('england_wiki.txt') as f:
    data = f.read()
    # the start of the line  is a bar ^|
    template = re.findall(r'^|(.*)\s=\s(.*)', data)


if __name__ == "__main__":
    main()
