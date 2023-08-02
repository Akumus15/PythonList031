'''
Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta
temperatura convertida em graus Celsius. A fórmula da conversão é c=(f–32)x5:9, onde c é a temperatura
em graus Celsius e f em Fahrenheit.
'''

f = float(input("Me diga uma temperatura em Fahrenheit, que eu irei converter em Celcius "))

c = (f - 32) * 5 // 9

print("A conversão da temperatura ficou como ", c)




