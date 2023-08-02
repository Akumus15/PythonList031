'''
Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
a) Resultado de suas adições
b) Resultado de suas multiplicações
'''
num = input("Você deseja que eu inserir  4 números e faça alguns calculos ?")
a = int(input("informe um número: "))
b = int(input("informe um número: "))
c = int(input("informe um número: "))
d = int(input("informe um número: "))
adicao = a + b + c + d
multiplicacao = a * b * c * d
print("O resulta da adição de todos os números informados é ", adicao, "e o resultado da multiplicação de todos os números informados é ", multiplicacao)