a = input()
s = ""
for i in range(-1,-len(a)-1,-1):
    s += a[i]

if s == a:
    print(True)
else:
    print(False)