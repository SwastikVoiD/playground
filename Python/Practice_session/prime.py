# print all prime numers between 1 to 100

for i in range(1,101):
    prime = True
    if i == 1:
        prime = True
    if i == 2:
        prime = True
    else:
        for j in range(2,i):
            if i%j == 0:
                prime = False
                break
            else:
                prime = True
    
    if prime:
        print(i)