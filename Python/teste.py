#Inputs
valorBruto=float(input("Qual é o valor bruto da viagem?\nR$"))
categoria=input("Selecione a categoria:\n1 - Econômica\n2 - Executiva\n3 - Primeira Classe\n")
quantidadePessoas=int(input("Qual é a quantidade de pessoas que viajarão e que moram na mesma residência? "))
#Processamento de dados
if categoria=='1':
    if quantidadePessoas==2:
        valorLiquido=valorBruto*0.97
    elif quantidadePessoas==3:
        valorLiquido=valorBruto*0.96
    elif quantidadePessoas>=4:
        valorLiquido=valorBruto*0.95
    else:
        print("Você não receberá descontos pela viagem")
elif categoria=='2':
    if quantidadePessoas==2:
        valorLiquido=valorBruto*0.95
    elif quantidadePessoas==3:
        valorLiquido=valorBruto*0.93
    elif quantidadePessoas>=4:
        valorLiquido=valorBruto*0.92
    else:
        print("Você não receberá descontos pela viagem")
elif categoria==3:
    if quantidadePessoas==2:
        valorLiquido=valorBruto*0.9
    elif quantidadePessoas==3:
        valorLiquido=valorBruto*0.85
    elif quantidadePessoas>=4:
        valorLiquido=valorBruto*0.8
    else:
        print("Você não receberá descontos pela viagem")
else:
    print("Você não pertence a nenhuma categoria")
#Outputs