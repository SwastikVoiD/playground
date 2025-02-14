def min_moves(N,flavour):
    ingredient_matrix ={
        't': [1,0,0],
        'o': [0,1,0],
        'b': [0,0,1],
        'y': [0,1,1],
        'p': [1,1,0],
        'c': [1,0,1],
        's': [1,1,1]
    }
    tomato_seq = [ingredient_matrix[f][0] for f in flavour]
    onion_seq = [ingredient_matrix[f][1] for f in flavour]
    bellpepper_seq = [ingredient_matrix[f][2] for f in flavour]

    def count_max(arr):
        count = 0
        arr_simp = []
        for i in range(N):
            if len(arr_simp) == 0:
                arr_simp.append(arr[i])
            elif arr_simp[-1] == arr[i]:
                pass
            else:
                arr_simp.append(arr[i])
        for i in arr_simp:
            if i:
                count += 1
            else:
                pass
        
        return count

    moves = count_max(tomato_seq)+count_max(onion_seq)+count_max(bellpepper_seq)
    return moves

T = int(input())
for i in range(T):
    a = int(input())
    seq = input().split()
    print(min_moves(a,seq))