nome = (input("Digite seu nome: "))
peso = int(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso/(altura*altura)
if imc <18.5:
    print ("Você está abaixo do peso!")
elif imc >18.5 and imc <24.9:
    print ("Peso normal!")
elif imc >25.0 and imc <29.9:
    print ("Sobrepeso!")
else :
    print("Obesidade!")