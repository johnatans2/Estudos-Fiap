rm=input("Por favor, digite o se RM: ")
print(rm)
idade=int(input("Por favor, digite a sua idade: "))
print(idade)
if idade>=18:
    print(f"Sua inscrição foi autorizada, aluno de RM {rm}")
    print("Mais instruções serão enviadas ao seu E-mail cadastrado na FIAP!")
else:
    autorizacao=input("Você possui autorização dos seus responsáveis para participar do campeonato? ").lower()
    if autorizacao=="sim":
        print(f"Sua inscrição foi autorizada, aluno de RM {rm}")
        print("Mais instruções serão enviadas ao seu E-mail cadastrado na FIAP!")
    else:
        print("Sua participação não foi autorizada por causa da sua idade")