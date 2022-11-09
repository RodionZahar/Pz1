#Сформировать и вывести целочисленный список разменра 10, содержащий 10 первых
#положительных нечетных чисел: 1,3,5 ... .
import random

N = (10)
print("N = ", N)

a1 = []
for i in range(N):
    a1.append(i*2+1)
print(a1)

a2 = [i*2+1 for i in range(N)]
print(a2)
