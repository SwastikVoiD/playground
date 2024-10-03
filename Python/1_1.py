'''Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]'''

# Solution
# So basically by looking at the input we can say that we need to sort the tuples in a decreasing order.
# we have to sort them based on their first index
# for this we are going to define a function to sort tuples inside a list with reference to a element of the tup.
# we use a user-def function to increase the understanding and to make the code flexible to work under various situations.
# so let's get into the code.


def tuple_sort(tuplist,ind):
    sorter = []
    sorted_tup = []

    for i in tuplist:
        sorter.append(i[ind])
    sorter.sort(reverse=True)
    for i in sorter:
        for j in tuplist:
            if i == j[ind]:
                a = tuplist.pop(tuplist.index(j))
                sorted_tup.append(a)
                continue
    return sorted_tup



tup_input = eval(input())
print(tuple_sort(tup_input,1))

# WE CAN DO THE SAME CODE IN A SHORTER FORMAT USING A LAMBDA FUNCTION
# WE SHALL GET INTO THAT LATER AS CURRENTLY IT IS OUT OF OUR EXPERTIES
