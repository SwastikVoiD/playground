'''Write a Python program to combine two dictionary by adding values for 
common keys. 
d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200, 'd':400} 
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})'''

d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200, 'd':400} 

d_net = {}
key_list1 = list(d1.keys())
key_list2 = list(d2.keys())
key_set = set(key_list1+key_list2)
# print(key_set)

for i in key_set:
    if i in key_list1:
        if i in key_list2:
            d_net[i] = d1[i] + d2[i]
        else:
            d_net[i] = d1[i]
    elif i in key_list2:
        d_net[i] = d2[i]

print(f"Counter({d_net})")