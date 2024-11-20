def fibonaci(n):
    s = [0,1]
    a = 0
    b = 1
    for i in range(n):
        c = a+b
        s.append(c)
        a = b
        b = c
    for i in s:
        print(i)

fibonaci(10)