opcao = 0
frances = 0
integral = 0
doce_liso = 0
doce_farofa = 0
forma = 0
valor_frances = 0
valor_integral = 0
valor_doce_liso = 0
valor_doce_farofa = 0
valor_forma = 0
valor_total = 0
quantidade = int
while opcao !=6:
    print ("===Padaria===")
    print ("1 - Pão francês")
    print ("2 - Pão Integral")
    print ("3 - Pão Doce Liso")
    print ("4 - Pão Doce Farofa")
    print ("5 - Pão de Forma")
    print ("6 - Fim da Compra")
    print ("----------------------")
    opcao = int(input("Digite a opção escolhida: ")) 
    if opcao ==1:
        quantidade =  int(input("Digite a quantidade desejada de Pão Francês: "))
        frances = frances  + quantidade
        valor_frances = frances + (quantidade * 1.04)
    elif opcao ==2:
        quantidade = int(input("Digite a quantidade desejada de Pão Integral: "))
        integral = quantidade + integral
        valor_integral = integral  + (quantidade* 1.04)
    elif opcao ==3:
        quantidade = int(input("Digite a quantidade desejada de Pão Doce Liso: "))
        doce_liso = quantidade +doce_liso
        valor_doce_liso = doce_liso + (quantidade * 1.08)
    elif opcao ==4:
        quantidade = int(input("Digite a quantidade desejada Pão Doce Farofa: "))
        valor_doce_farofa = doce_farofa + (quantidade * 1.11)
    elif opcao ==5:
        quantidade = int(input("Digite a quantidade desejada de Pão De Forma "))
        valor_forma = forma + (quantidade* 0.95)
    elif opcao ==6:
        valor_total = valor_frances + valor_integral + valor_doce_liso + valor_doce_farofa + valor_forma
        break
print ("===RECIBO===")
if (frances >0):
     print (f"-Pão Francês - Quantidade {frances} | valor R$ {valor_frances:.2f}")
if (integral >0):
    print (f"-Pão Integral - Quantidade {integral} | valor R$ {valor_integral::.2f}")
if (doce_liso >0):
    print (f"-Pão Doce Liso - Quantidade {doce_liso} | valor R$ {valor_doce_liso:.2f}")
if (doce_farofa >0):
    print (f"-Pão Doce Liso - Quantidade {doce_liso} | valor R$ {valor_doce_liso:.2f}")
if (forma >0):
    print (f"-Pão De Forma - Quantidade {forma} | valor R$ {valor_forma:.2f}")
    print (f"-Valor total da compra: R$ {valor_total:.2f}")