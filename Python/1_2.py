'''Write a Python program to replace the last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]'''

# Solution

def tup_rep(tlist,pos,rep):
    nlist = []
    for i in tlist:
        a = list(i)
        a[pos] = rep
        nlist.append(tuple(a))
    return nlist


tl = eval(input())
print(tup_rep(tl,2,100))