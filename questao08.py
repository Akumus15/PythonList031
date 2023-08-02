'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro.
'''
per = print("Informe a distância a percorrer em km e o valor do consumo médio do automóvel, em km/l, que lhe mostarie a quantidade de litros que seu automóvel vai gastar")
dis = int(input("Informe a distâcia aqui "))
val = int(input("Informe o valor do consumo médio do automovél "))
l = dis / val
print("A quantidade de litros que o seu automóvel gastará em uma viagem será ", l)