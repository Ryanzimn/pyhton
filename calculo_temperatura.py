celsius = int(input("Digite sua temperatura em celsius: "))
print ("Conversor de temperatura")
print ("1 - Celsius para Fahrenheit")
print ("2 - Celsius para Kelvin")
opcao = int(input("escolha a sua opção: "))
if opcao ==1:
    print ("Você escolheu Celsius para Fahrenheit!")
    farnheit = celsius *9/5 + 32
    print (f"A conversão da sua temperatura para Fahrnheit é de: {farnheit}")
elif opcao ==2:
    print ("Você escolheu Celsius para Kelvin!")
    kelvin = celsius + 273.15
    print (f"A sua conversão da sua temperatura de Celsius para Kelvin é igual a: {kelvin}")
else:
    print("Opção inválida, tente novamente!")
