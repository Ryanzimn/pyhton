#definir notas
nota_prova= float (input("Digite sua nota de prova: "))
nota_trabalho= float (input("Digite sua nota do trabalho:"))
#definir média
media= (nota_prova +nota_trabalho)/2
print (f"Sua média é {media}")
if ("media=>7"):
    print ("Aprovado!")
else:
    print ("Reprovado")