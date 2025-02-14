import math

def max_chaotic_recipes(num, arr):
   max_recipes = math.factorial(num)/(math.factorial(num-2)*math.factorial(2))
   chaoic_pair = 0
   for i in range(num):
      for j in range(2,num):
         pass
num = int(input())
inp = input()
inplst = inp.split()

max_chaotic_recipes(num,inplst)