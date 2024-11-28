# Factorial
def fact(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return False
    else:
        f = 1
        for i in range(1,num+1):
            f = f * i
        return f
    
while __name__ == "__main__":
    num = int(input())
    res = fact(num=num)
    if res:
        print(res)
        break
    else:
        print('You have entered an invalid number.')
        print("Do you want to try again? Y?N")
        choice = input()
        if choice in "Yesyes":
            continue
        else:
            break