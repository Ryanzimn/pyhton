nome = input("Digite seu nome: ")
salario_fixo = int(input("Digite seu salário fixo: "))
vendas = int(input("Digite o número de vendas feitas esse mês: "))
if vendas>= 20:
    vendas = salario_fixo * 0.15
    salario_fixo = salario_fixo + vendas
    print (f"A sua comissão será de: {vendas}")
    print (f"Parabéns você atingiu o número esperado de vendas, seu salário será de {salario_fixo}")
else:
    print (f"Infelizmente você não bateu o número esperado de vendas, seu salário será de:{salario_fixo}")