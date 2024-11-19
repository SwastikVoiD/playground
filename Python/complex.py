# adding 2 complex numbers

def str_comp(a):
    b = a.split("+")
    c = b[1].removesuffix("j")
    j = 1j
    comp = int(b[0]) + complex(c)*j
    return comp

a = input()
b = input()
c = str_comp(a)
d = str_comp(b)
e = c + d
print(e)