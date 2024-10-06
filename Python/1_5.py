"""
Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary. 
 
Sample data : {'1':['a','b'], '2':['c','d']} 
Expected Output: 
ac 
ad 
bc 
bd
"""
dick = {'1':['a','b'], '2':['c','d']}
dick = list(dick.values())
cross_set = set()
for i in dick:
    dick.remove(i)
    for j in dick:
        if i != j:
            for k in range(len(i)):
                for l in range(len(j)):
                    cross_set.add(i[k]+j[l])


for i in cross_set:
    print(i)