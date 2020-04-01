#00 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
def back_to_head(word):
    for i in range(len(word)-1,-1,-1):
        print(word[i])

def back_to_head2(word):
    ordered_word = sorted(word, reverse = True)
    print(ordered_word)

def back_to_head3(word):
    ordered_word = word[::-1]
    print(ordered_word)

#01 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

def get_s_letters(word):
    letters = word[0:len(word) -1 : 2]
    print(letters)

def get_s_letters2(word):
    letters =slice(0,len(word) -1 , 2)
    print(word.__getitem__(slice(0,len(word) -1 , 2)))


#02 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
def combine_two_words(word1,word2):
    comb_word = word1[0]+word[0]


def main():
    get_s_letters2("パタトクカシーー")

if __name__ == "__main__":
    main()
