##################
######2nd UNIX#####

#hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
#以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
#さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

#wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt

#10 10. 行数のカウント
def count_row(file_path):
    """
    行数をカウントせよ．確認にはwcコマンドを用いよ．
    $ wc -l hightemp.txt
    >>24 hightemp.txt
    """
    #file_path = "hightemp.txt"
    with open(file_path,'r', encoding="utf-8") as f:
        lines= f.readlines()
    return len(lines)

def count_row2(file_path):
    count =0
    with open(file_path, "r",encoding="utf-8") as f:
        for line in f:
            count +=1
    print(count)


#11. タブをスペースに置換

def replace_tab_space(file_path):
    """
    タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
    """
    with open(file_path,encoding="utf-8") as f:
        lines= f.readlines()
        #lines.replace('/t',' ')\
        replaced_lines = map(lambda s: s.replace('\t',' '), lines)
    return list(replaced_lines)


#12 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
def save_file(file_path):
    """
    各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
    確認にはcutコマンドを用いよ．
    """
    with open(file_path, "r", encoding= 'utf-8') as f:
        lines = f.readlines()
        col1 = list(map(lambda line : line.split('\t')[0], lines))
        #print(col1)
    with open ("col1.txt", "w") as file:
        file.write(" ".join(col1))

    with open(file_path, "r", encoding= 'utf-8') as f:
        lines = f.readlines()
        col2 = list(map(lambda line : line.split('\t')[1], lines))
        #print(col2)
    with open ("col2.txt", "w") as file:
        file.write(" ".join(col2))

def save_file2(file_path):
    import pandas as pd
    data = pd.read_table(file_path, header = None, sep = '\t',encoding ='utf-8')
    data[0].to_csv('col1.txt', header =None,index = False)
    data[1].to_csv('col2.txt', header =None,index = False)

#13. col1.txtとcol2.txtをマージ

def merge_txt():
    """
    12で作ったcol1.txtとcol2.txtを結合し，
    元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
    確認にはpasteコマンドを用いよ
    """
    save_file("hightemp.txt")
    with open("col1.txt") as f:
        col1 = f.readline()
        col1 = col1.split(" ")
        #print(col1)

    with open("col2.txt") as f:
        col2 = f.readline()
        col2 = col2.split(" ")
       # print(col2)

    #lines_zip = zip(col1,col2)
    #lines = "".join(map(lambda x: ''.join(x),lines_zip))

    #lines = "{col1}\t{col2}".format(col1=col1,col2=col2)
    lines = ["{0}\t{1}".format(line1, line2) for line1, line2 in zip(col1, col2)]
    print(lines)

#UNIX COMMAND
    # col1の抽出と比較
    #cut --fields=1 hightemp.txt > col1_test.txt
    #diff --report-identical-files col1.txt col1_test.txt


#14. 先頭からN行を出力
def print_n(file_path,n):
    import sys
    with open(file_path) as f:
        lines = f.readlines()
        print(lines[0:n])

#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
#確認にはheadコマンドを用いよ．

def print_n2(file_path):
    #fname = 'hightemp.txt'
    n = int(input('N--> '))

    with open(file_path) as data_file:
        for i, line in enumerate(data_file):
            if i >= n:
                break
            print(line.rstrip())

def print_n3(file_path,n):
    with open("hightemp.txt") as f:
        lines = f.readlines()
        for i in range(0,n):
            print(lines[i].rstrip())

            fname = 'hightemp.txt'

def print_n4(file_path):
    n = int(input('>>> N : '))

    with open(file_path, encoding="utf-8_sigs   ") as hightemp:
        for i, line in enumerate(hightemp):
            if i >= n:
                break
        print(line.rstrip())

#UNIX
#$ head -3 hightemp.txt



#15. 末尾のN行を出力
def print_tail_n(file_path,n):
    with open(file_path) as f:
        lines = f.readlines()
        for i in range( len(lines) -n ,len(lines)):
            print(lines[i].rstrip())
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
#UNIX
#$ head -3 hightemp.txt

#16.ファイルをN分割する
def split_file(file_path):
    """
    自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
    """
    import math
    s = int(input('N--> '))

    with open(file_path) as f:
        lines = f.readlines()
        d = math.ceil(len(lines) / s)

        for j in range(0,s):
            for i in range (0, d):
                file ="split._{:02d}txt".format(j)
                write_file(file, lines[i+j*d])



def split_file2(file_path):
    """
    自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
    """
    import math
    s = int(input('N--> '))

    with open(file_path) as f:
        lines = f.readlines()
        d = math.ceil(len(lines) / s)

        for i in range (0, len(lines),d):
            file ="split._{:02d}txt".format(j)
            write_file(file, lines[i:i+d])

def write_file(file_path,str):
    with open (file_path, "a") as file:
        file.write("".join(str))
        #file.write(str)

def split (t,s):
    import math
    d = math.ceil(len(t)/s)
    for i in range(0, len(t), d):
        j = i + d
        print(t[i:j])

"""
UNIX
!/bin/sh

Nを入力
echo -n "N--> "
read n

# 行数算出　wcは行数とファイル名を出力するのでcutで行数のみ切り出し
count=`wc --line hightemp.txt | cut --fields=1 --delimiter=" "`

# 1分割当たりの行数算出　余りがある場合は行数を+1
unit=`expr $count / $n`
remainder=`expr $count % $n`
if [ $remainder -gt 0 ]; then
    unit=`expr $unit + 1`
fi

# 分割
split --lines=$unit --numeric-suffixes=1 --additional-suffix=.txt hightemp.txt child_test_

# 検証
for i in `seq 1 $n`
do
    fname=`printf child_%02d.txt $i`
    fname_test=`printf child_test_%02d.txt $i`
    diff --report-identical-files $fname $fname_test
done
"""

#17.１列目の文字列の異なり
def get_unique(file_path):
    """
    1列目の文字列の種類(異なる文字列の集合)を求めよ．
    確認にはsort, uniqコマンドを用いよ．
    """
    with open(file_path) as f:
        data = f.readlines()
        col1 = list(map(lambda list:list.split("\t")[0], data))
        set_col1 = set(col1)
        print(set_col1)

def get_unique2(file_path):
    import pandas as pd
    data = pd.read_table(file_path, header = None, sep = '\t',encoding ='utf-8')
    col1_unique = set(data[0])

#unix
# 先頭カラムを切り出し、ソート、重複除去
#cut --fields=1 hightemp.txt | sort | uniq > result_test.txt

#18 各行を3コラム目の数値の降順にソート
def sort(file_path):
    """
    各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
    確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
    """
    file_path ="hightemp.txt"
    with open(file_path) as f:
        data = f.readlines()
        data.sort(key=lambda data: float(data.split('\t')[2]), reverse=True)
        return(data)

def get_third(df):
    return df.split('\t')[2]
def sort2(file_path):
    """
    各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
    確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
    """
    file_path ="hightemp.txt"
    with open(file_path) as f:
        data = f.readlines()
        data.sort(key = get_third)
        return(data)


#18 各行を3コラム目の数値の降順にソート
def sort3(file_path,n:int):
    """
    各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
    確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
    """
    import pandas as pd
    data = pd.read_table(file_path, header = None, sep = '\t',encoding ='utf-8')
    data.sort_values(by=n)

#UNIX
## 3カラム目を数値として逆順ソート
#sort hightemp.txt --key=3,3 --numeric-sort --reverse > result_test.txt


#19 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
def freq_sort(file_path):
    """
    各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
    """
    #file_path ="hightemp.txt"
    word_count = {} #{山形県: 2, ....}
    with open(file_path) as f:
        data = f.readlines()
        col1 = list(map(lambda list:list.split("\t")[0], data))
        for element in col1:
            if not element in word_count:
                word_count[element] = 1
            else:
                word_count[element] += 1
        #list_word_count = [ k  for k in word_count ]
        #list_word_count = [ v  for v in word_count(vlaue) ]
        list_word_count = [[ k,v ] for k,v in word_count.items() ]
        list_word_count.sort(key = lambda list:list[1],reverse = True)
    return list_word_count

## 1カラム目でソートし、重複除去して件数付きで出力、その結果をソート
#cut --fields=1 hightemp.txt | sort | uniq --count | sort --reverse


def main():
    #bigram_calc("paraparaparadise","paragraph")
    #count_row2("hightemp.txt")
    #l = [i for i in range(30)]
    #split(l,3)
    #split_file("hightemp.txt")
    #print(l)
    #result = sort2("hightemp.txt")
    #print(result)
    l =freq_sort("hightemp.txt")
    print(l)
if __name__ == "__main__":
    main()
