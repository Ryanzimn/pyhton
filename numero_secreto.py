#Declarar variaveis
import random
#Declarar variaveis
numero_secreto = random.randint (1 , 10)
tentativas = 0
contagem_tentativas = 0
#Introdução ao jogo
print ("Bem-vindo ao jogo do Número Secreto")
print ("Tente adivinhar o número secretp entre 1 a 10.")
#Laço repetição
while tentativas != numero_secreto:
    numero= int(input("Digite seu número: "))
    contagem_tentativas= contagem_tentativas+1
    if numero == numero_secreto:
        print ("Parabéns! Você adivinhou o número secreto")
        print (f"Você precisou de{contagem_tentativas} tentativas.")
        break
    elif numero <numero_secreto:
        print ("O número secreto é maior")
    else:
        print ("O número secreto é menor.")
        