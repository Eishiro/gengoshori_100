"""
第4章: 形態素解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
curl  https://nlp100.github.io/data/neko.txt -o neko.txt

mecab
http://taku910.github.io/mecab/bindings.html

$mecab neko.txt -o neko.txt.mecab
"""

import MeCab



#30. 形態素解析結果の読み込み

def get_mecab():
    """
    形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
    ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
    をキーとするマッピング型に格納し，
    1文を形態素（マッピング型）のリストとして表現せよ．
    第4章の残りの問題では，ここで作ったプログラムを活用せよ．
    
    """
    original_file = 'neko.txt'
    with open(original_file, encoding="utf-8") as in_f, \
         open('./neko.txt.min_ecab', mode='w') as out_f:
        
        line = in_f.readline()
        while line:
            line = in_f.readline()
            print(line)
            m_line = MeCab.Tagger("-Ochasen").parse(line)
            print(m_line)
    #tagger = MeCab.Tagger("-Ochasen")
    #tagger.parse('')

def get_mecab2():
    original_file = 'neko2.txt'
    with open(original_file, encoding="utf-8") as in_f, \
         open('./neko.txt.min_ecab', mode='w') as out_f:
         lines = in_f.readlines()
         mecab_lines = list(map(lambda x : MeCab.Tagger("-Ochasen").parse(x), lines) )
   # m= MeCab.Tagger("-Ochasen").parse("このファイルを用いて，以下の問に対応するプログラムを実装せよ．")
    return mecab_lines

    
def main():
    #bigram_calc("paraparaparadise","paragraph")
    #count_row2("hightemp.txt")
   l = get_mecab2()
   for i in l:
       print(i.strip())
if __name__ == "__main__":
    main()


