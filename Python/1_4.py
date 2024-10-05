"""Write a Python program to print the employee details with Employee ID as 
keys. 
Employees={'Ajay'=10001, 'Sheela'=10002, 'Goyal'=10003} 
Insert the employees whoever joining further are to get new employee id in the 
sequence order."""

# Solution
import json

length = 1
Employees = {'Ajay':10001,
             'Sheela':10002,
             'Goyal':10003}
while length:
    empnm = input("Enter the name of the employee you want to add:\t")
    length = len(empnm)
    if length:
        idlist = list(Employees.values())
        empid = max(idlist)+1
        Employees[empnm]=empid
    else:
        break

print(json.dumps(Employees,separators=(',','='))) #for formatting in the specified format 
