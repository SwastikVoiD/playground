# password checker moodle
# regno and password char checker code
# 10-10-2024
# moodle python

a = input()
b = input()
output = 0
regno = 0
if len(a) == 9:
    a1 = a[:2]
    a2 = a[2:5]
    a3 = a[5:]
    if a1.isdigit():
        if int(a1) >= 10:
            if a2.isalpha():
                if a3.isdigit:
                    if int(a3) >= 1:
                        regno = 1

passw = 0
if 8 <= len(b) <= 16:
    u = 0 
    l = 0
    n = 0
    for i in b:
        if i.isalpha():
            if i.islower():
                l += 1
            else:
                u += 1
        if i.isdigit():
            n += 1
    if u >= 1 and l >= 1 and n >=1:
        passw = 1
if passw == 1 and regno == 1:
    print(1)
else:
    print(0)
        