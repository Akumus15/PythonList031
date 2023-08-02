'''
Fazer um algoritmo que pergunte 1 número e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''
import math

num = int(input("Me informe um número lhe mostrei as seguintes coisas: o próprio número, o quadrado deste número e a raiz quadrada deste número "))
b = num * num
c = math.sqrt(num)
print("Aqui está o seu resultado ", num, b, c)
