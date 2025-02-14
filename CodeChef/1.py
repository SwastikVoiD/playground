# Long Words
def wordchr(wrd):
    if len(wrd)<=10:
        return wrd
    else:
        pref = wrd[0]
        suff = wrd[-1]
        abb = pref+str(len(wrd)-2)+suff
        return abb
    
if __name__ == "__main__":
    num = int(input())
    wlist = []
    for i in range(num):
        word = input()
        wlist.append(word)
    for i in wlist:
        out = wordchr(i)
        print(out)