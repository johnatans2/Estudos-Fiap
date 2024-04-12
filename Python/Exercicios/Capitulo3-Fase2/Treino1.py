#Apresentação
print("Contador de calorias diárias\n".upper())
#Criação de Variáveis
totalCaloria=0
posicao=0
#Input
quantidadeDeAlimentos=int(input("Quantos alimentos você consumiu hoje?\n"))
#Processamento de Dados
while posicao!=quantidadeDeAlimentos:
    posicao+=1
    caloria=float(input(f"Quantidade de calorias do {posicao}º alimento: "))
    totalCaloria+=caloria
#Output
print(f"A quantidade total de calorias consumidas hoje é de {totalCaloria}")