compra = int(input("Digite o valor total da compra: "))
parcelas = int(input("Digite a quantidade desejada de parcelas: "))
total = compra/parcelas
print (f"O valor total da sua compra será de:{compra}")
print(f"Cada parcela sairá por:{total:.2f}")