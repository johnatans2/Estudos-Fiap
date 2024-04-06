#Apresentação
print("Verificador de frequência cardíaca\n".upper())
#Inputs
idade=int(input("Digite sua idade: "))
BPM=int(input("Digite o número de batimentos cardíacos por minuto: "))
#Processamento de dados e Outputs
if 0<=idade<=2:
    if 120<=BPM<=140:
        print("Batimentos dentro da faixa adequada")
    elif BPM<120:
        print("Batimentos abaixo da faixa adequada")
    else:
        print("Batimentos acima da faixa adequada")
elif 8<=idade<=17:
    if 80<=BPM<=100:
        print("Batimentos dentro da faixa adequada")
    elif BPM<80:
        print("Batimentos abaixo da faixa adequada")
    else:
        print("Batimentos acima da faixa adequada")
elif 18<=idade<60:
    if 70<=BPM<=80:
        print("Batimentos dentro da faixa adequada")
    elif BPM<70:
        print("Batimentos abaixo da faixa adequada")
    else:
        print("Batimentos acima da faixa adequada")
elif idade>=60:
    if 50<=BPM<=60:
        print("Batimentos dentro da faixa adequada")
    elif BPM<50:
        print("Batimentos abaixo da faixa adequada")
    else:
        print("Batimentos acima da faixa adequada")
else:
    print("Idade digitada não é válida")