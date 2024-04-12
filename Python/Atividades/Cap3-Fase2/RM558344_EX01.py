#Apresentação
print("""
    𝓥𝓸𝓽𝓪𝓬̧𝓪̃𝓸 Para a Realização das Lives
""")
#Criação de variáveis
segunda=0
terca=0
quarta=0
quinta=0
sexta=0
maior=0
dia=""
igual=[]
#Input
colaboradores=input("Por favor, informe a quantidade de colaboradores que irão votar: ")
#Processamento de Dados
while colaboradores.isdigit()==False:
    colaboradores=input("\nVocê digitou uma quantidade inválida, por favor, digite novamente: ")
colaboradores=int(colaboradores)
for colaborador in range(1,colaboradores+1):
    escolha=input("""
Por favor, escolha o dia da semana de sua preferência para a realização das lives:

    1 - Segunda-Feira
    2 - Terça-Feira
    3 - Quarta-Feira
    4 - Quinta-Feira
    5 - Sexta-Feira

""")
    if escolha.isdigit()==False:
        while escolha.isdigit()==False:
            escolha=input("""
Você não digitou uma opção válida, por favor selecione uma das opções abaixo:

    1 - Segunda-Feira
    2 - Terça-Feira
    3 - Quarta-Feira
    4 - Quinta-Feira
    5 - Sexta-Feira
                            
    """)
    else:
        escolha=int(escolha)
        while escolha<1 or escolha>5:
            escolha=int(input("""
Você não digitou uma opção válida, por favor selecione uma das opções abaixo:

    1 - Segunda-Feira
    2 - Terça-Feira
    3 - Quarta-Feira
    4 - Quinta-Feira
    5 - Sexta-Feira
                            
"""))
    match escolha:
        case 1:
            print("\nO dia escolhido foi: Segunda-Feira")
            segunda+=1
        case 2:
            print("\nO dia escolhido foi: Terça-Feira")
            terca+=1
        case 3:
            print("\nO dia escolhido foi: Quarta-Feira")
            quarta+=1
        case 4:
            print("\nO dia escolhido foi: Quinta-Feira")
            quinta+=1
        case 5:
            print("\nO dia escolhido foi: Sexta-Feira")
            sexta+=1
#Estrutura para definir qual foi a opção mais votada. Eu poderia utilizar uma estrutura condicional encadeada para isto, mas o código ficaria bem maior e complicado, por isto optei pela estrutura condicional simples e pela utilização de uma variável de marcação, que no caso é a variável "maior".
if segunda>maior:
    maior=segunda
    dia="segunda-feira"
if terca>maior:
    maior=terca
    dia="terça-feira"
if quarta>maior:
    maior=quarta
    dia="quarta-feira"
if quinta>maior:
    maior=quinta
    dia="quinta-feira"
if sexta>maior:
    maior=sexta
    dia="sexta-feira"
#Outputs
if maior==0:
    print("\nNinguém Votou ou participou da votação\n")
else:
#Estrutura para verificar se há dias com a mesma quantidade de votos, ou seja, dias com valores iguais. Para verificar isto, antes eu precisaria observar qual foi o dia mais votado, podendo assim utilizar a variável "maior" para a veraciadade. utilizei também a estrutura condicional simples por ser mais ideal.
    if maior==segunda:
        igual.append("segunda-feira")
    if maior==terca:
        igual.append("terça-feira")
    if maior==quarta:
        igual.append("quarta-feira")
    if maior==quinta:
        igual.append("quinta-feira")
    if maior==sexta:
        igual.append("sexta-feira")
    if igual!=[] and len(igual)!=1:
        print(f"\nCom {maior} voto(s), tivemos mais de um dia escolhido para a realização das lives, ou seja, tivemos um empate! Os dia escolhidos foram: {igual}\n")
    else:
        print(f"\nCom {maior} voto(s), o dia escolhido para a realização das lives foi {dia}\n")