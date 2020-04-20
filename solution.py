# http://www.cl.ecei.tohoku.ac.jp/nlp100/


# 00 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
import re


def back_to_head(word):
    for i in range(len(word) - 1, -1, -1):
        print(word[i])


def back_to_head2(word):
    ordered_word = sorted(word, reverse=True)
    print(ordered_word)


def back_to_head3(word):
    ordered_word = word[::-1]
    print(ordered_word)

# 01 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．


def get_s_letters(word):
    letters = word[0:len(word) - 1: 2]
    print(letters)


def get_s_letters2(word):
    letters = slice(0, len(word) - 1, 2)
    print(word.__getitem__(slice(0, len(word) - 1, 2)))


# 02 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    w1 = "abc"
    w2 = "123"
    l = [w1, w2]
    print(''.join(l))
    zipped = list(zip(w1, w2))
    print(zipped)
    print("".join(zipped))


def combine_two_words(word1: str, word2: str):
    result = []
    for i in range(min(len(w1), len(w2))):
        result.append(w1[i])
        result.append(w2[i])
    print(''.join(result))

# 一行でやるとこうなる
# return ''.join(w1[i] + w2[i] for i in range(len(w1)))


# 03. 円周率
#str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#words = str.split(' ')
def count_char(str):
    """
    Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，
    各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    """
    words = str.split(' ')
    for i in range(len(words)):
        print(len(words[i]))


def count_char2(str):
    # remove "." and
    import re
    str = re.sub('[^A-Za-z0-9 ]+', '', str)
    words = str.split(' ')
    count_char = map(lambda x: len(x), words)
    print(list(count_char))


def count_char3(s:str):

    return list(len(m) for m in re.findall('[a-zA-Z]+', s))

# 04. 元素記号
def get_atomic_sym(str:str):
    """
    "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
    それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
    """
    #str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    str = re.sub('[^A-Za-z0-9 ]+', '', str)
    words = str.split(' ')
    print(words)

    first_chr = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    atomic_sym = []
    for i in range(len(words)):
        if i + 1 in first_chr:
            atomic_sym.append(words[i][:1])
        else:
            atomic_sym.append(words[i][0:2])
    print(atomic_sym)

    chr_pos = {} #['H': 1, 'He': 2]
    i=1
    for word in atomic_sym:
        chr_pos[word] = i
        i = i+1
    print (chr_pos)


def get_atomic_sym2(s: str):
    """
    単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
    取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を返します

    >>> atomic_symbols('Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.')
    {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
    """
    single_char_atomic_symbols = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    word_number = 0
    result = {}

    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':  # 大文字だったらここから単語
            word_number += 1  # 何番目の単語かカウント
            if word_number in single_char_atomic_symbols:
                # 1文字取る
                word = s[i]
            else:
                # 2文字取る
                word = s[i:i+2]
            result[word] = word_number  # 連想配列に入れる

    return result


def get_atomic_sym3(s: str):

    words = target.split(' ')
    for (num, word) in enumerate(words, 1):
        if num in num_first_only:
            result[word[0:1]] = num
        else:
            result[word[0:2]] = num

        print(result)


###enumerate
#my_list = ['apple', 'banana', 'grapes', 'pear']
#for c, value in enumerate(my_list, 1):
#    print(c, value)
# Output:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear


#05. n-gram
def bigram( str:str):
    """
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
    この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    """
    #str= 'I am an NLPer'
    import re
    str = re.sub('[^A-Za-z0-9 ]+', '', str)

    words= str.split(' ')
    bigram =[]
    for i in range(len(words) -1):
        bigram.append(words[i] +"-"+ words[i+1])

    print(bigram)

def ngram_word(str:str, n):
    import re
    str = re.sub('[^A-Za-z0-9 ]+', '', str)
    words= str.split(' ')

    ngram = []
    for i in range(len(words) -n+1):
        ngram.append(words[i:i +n])
    return ngram


def ngram_char(str:str, n:int):
    ngram = []
    for i in range(len(str) -n+1):
        ngram.append(str[i:i +n])
    return ngram

#result = ngram_word('I am an NLPer',3)
#print(result)

def make_ngram(arr: [], n: int):
    """
    渡されたリストからn-gramを作成します

    >>> make_ngram('I am an NLPer', 2)
    [('I', ' '), (' ', 'a'), ('a', 'm'), ('m', ' '), (' ', 'a'), ('a', 'n'), ('n', ' '), (' ', 'N'), ('N', 'L'), ('L', 'P'), ('P', 'e'), ('e', 'r')]

    >>> make_ngram('I am an NLPer'.split(' '), 2)
    [('I', 'am'), ('am', 'an'), ('an', 'NLPer')]
    """
    return list(tuple(arr[i:i + n]) for i in range(len(arr) + 1 - n))

#06 集合
########
#Class set
#https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset
##########

def bigram_calc(str1:str, str2:str):
    """
    “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
    さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
    """
    bigram1 = ngram_char(str1,2)
    bigram2 = ngram_char(str2,2)

    print ("UNION",(set(bigram1) | set(bigram2)))
    print ("INTERSECTION" ,(set(bigram1) & set(bigram2)))
    print ("DIFFEERENCE", (set(bigram1) - set(bigram2)))


#07. テンプレートによる文生成Permalink
def create_template(x:int , y:str, z:int):
    """
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
    さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
    """
    template = '{}時の{}は{}'.format(x, y, z)
    template2 ='{hour}時の{target}は{value}'.format(hour=x, target=y, value=z)
    print(template + "\n" +template2)

    #s = Template('$hour時の$targetは$value')
    #return s.substitute(hour=x, target=y, value=z)


#08. 暗号文
def cipher(str:str):
    """
    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """
    #
    #まずこの「219 - 文字コード」ってどういう意味か考えてみましょう。
    #a の文字コードは 97。219 - 97 = 122 で、文字コード 122 は z。
    #z の文字コードは 122。219 - 97 = 122 で、文字コード 97 は a。
    #つまり、ローマ字小文字 a～z について z～a に入れ替えるという暗号化になっていますね。
    #ちなみに 219 - (219 - n) = n なので、２回cipher関数を通すと元の文字列に戻ります。#
    #
def cipher2(s: str) -> str:
    """
    渡された英文を暗号化します

    >>> cipher('AaBbCc')
    'AzByCx'

    >>> cipher(cipher('She Sells Sea Shells by the Sea Shore'))
    'She Sells Sea Shells by the Sea Shore'
    """
    return ''.join(chr(219 - ord(c)) if 'a' <= c <= 'z' else c for c in s)


#09. Typoglycemia
#random https://note.nkmk.me/python-random-randrange-randint/
def random_sort_word(sentence: str):
    """
    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
    ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
    （例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
    を与え，その実行結果を確認せよ．
    """
    import random
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words = sentence.split(' ')

    shuffle_sentence = []
    for word in words:
        if len (word) < 4:
            shuffle_sentence.append(word)
        else:
            #get the letters from a word except the first and the end
            shuffle_part = list(word[1:-1])
            #random.sample rreturn a new list after shuffled.
            rand = random.sample(shuffle_part, k=len(shuffle_part))
            shuffled_word = word[0:1] + ''.join(rand) + word[-1:]
            shuffle_sentence.append(shuffled_word)

    return print(shuffle_sentence)




def main():
    #bigram_calc("paraparaparadise","paragraph")
    #count_row2("hightemp.txt")
    merge_txt()

if __name__ == "__main__":
    main()
