# Python Practice Question
# Swastik Debesh Patnaik
# 24BME0133


inp_list = [] #state and capital pair list initialised
length = 1
while length:
    item = input()
    length = len(item)
    a = item.lower()
    if length>=1:
        inp_list.append(a.split(": "))
    else:
        break
# print(inp_list)

inp_dict = {} #state and capital dict initiated
for i in inp_list:
    inp_dict[i[0]]=i[1]
# print(inp_dict)

dict_key = list(inp_dict.keys()) #list of states provided by the user

# print(dict_key)

while True:
    state = input("Capital of State?")
    lstate = state.lower()
    if lstate != "exit":
        if lstate in dict_key:
            disp = inp_dict[lstate]
            print(disp.capitalize())
        else:
            print("Not Found")
    else:
        break        
# end of code