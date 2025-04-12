# # for c == 0
# mat = [[2,4,1],[7,5,0],[3,9,6]]
# trans = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[1]))]
# arr = [[i[::-1]] for i in trans[::-1]]
# for i in arr:
#     print(i)

# # for c = 1
# # plain transpose
# mat = [[19,23,4],[0,3,61]]
# trans1 = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[1]))]
# for i in trans1:
#     print(i)

# #  for c = 2
# mat = [[2,4,1],[7,5,0],[3,9,6]]
# trans2 = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[1]))]
# for i in trans2:
#     print(i)

# # for c = 3
# mat = [[2,4,1],[7,5,0],[3,9,6]]
# trans = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[1]))]
# arr = [[i[::-1]] for i in trans[::-1]]
# for i in arr:
#     print(i)

def reflection(m,n,matrix,c):
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    if c == 0 or c == 3:
        arr = [[i[::-1]] for i in transpose[::-1]]
        return arr
    if c == 1 or c == 2:
        arr = transpose
        return arr

T = int(input())
output = []
for i in range(T):
    order = input().split()
    m = int(order[0])
    n = int(order[1])
    mat = []
    print(m + n)

    for i in range(m):
        a = input().split()
        row = [int(i) for i in a]
        mat.append(row)
    # print(mat)
    c = int(input())

    output.append(reflection(m,n,mat,c))

for i in output:
    for j in i:
        for k in j:
            for l in k:
                print(l , end=" ")
        print()
    