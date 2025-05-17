print ("Ao alugar o carro cada dia irá custar 90$")
print ("Cada kms rodados irá custar 0.20$")
dias = int(input("Digite a quantidade de dias alugados: "))
kms = int(input("Digite a quantidade de kms rodados: "))
dias = dias * 90
kms = kms * 0.20
total = dias + kms
print ("===RECIBO===")
print(f"O valor total de dias alugados foi de: {dias}$")
print(f"O valor total por kms rodados foi de: {kms}$")
print(f"O total a pagar é de: {total}$")