opcao = int
while opcao != 0:
    print("===Calculadora===")
    print ("1 - Somar")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("0 - Fechando a calculadora")
    opcao = int(input("Digite a opção escolhida: "))
    if opcao >=1 and opcao <=4:
        numero1 = int(input("Digite seu primeiro número: "))
        numero2 = int(input("Digite seu segundo número: "))        
    if opcao ==1:
        print ("Você escolheu Soma ")
        soma = numero1+numero2
        print (f"O valor da sua soma é igual a: {soma}")
    elif opcao ==2:
        print ("Você escolheu Subtração")
        subtracao = numero1 - numero2
        print (f"O valor da sua subtração é igual a: {subtracao}")
    elif opcao ==3:
        print ("Você escolheu Multiplicação")
        multiplicacao = numero1 * numero2
        print (f"O valor da sua multiplicação é igual a: {multiplicacao}")
    elif opcao ==4:
        print ("Você escolheu Divisão")
        divisao = numero1 / numero2
        print (f"O valor da sua divisão é igual a é igual a: {divisao}")
    elif opcao ==0:
        print("===Saindo da calculadora===")
        break
    else:
        print ("Opção inválida")