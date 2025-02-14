sample = [1,0,0,1,1,1,0,1,0]
arr = []
count = 0
for i in range(len(sample)):
    if len(arr) == 0:
        arr.append(sample[i])
    elif arr[-1] == sample[i]:
        pass
    else:
        arr.append(sample[i])

print(arr)