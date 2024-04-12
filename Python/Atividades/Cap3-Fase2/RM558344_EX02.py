#Apresentação
print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱┃┃╱╱╱╱╱╱┃┃╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱┃╭━╮┃
┃┃╱╰╋━━┫┃╭━━┳╮╭┫┃╭━━╮╭━╯┣━━╮┃╰━╯┣━┳━━┳━━┳━━╮╭━╯┣━━╮┃┃╱╰╋━━┳━┳━┳━━╮
┃┃╱╭┫╭╮┃┃┃╭━┫┃┃┃┃┃╭╮┃┃╭╮┃┃━┫┃╭━━┫╭┫┃━┫╭━┫╭╮┃┃╭╮┃╭╮┃┃┃╱╭┫╭╮┃╭┫╭┫╭╮┃
┃╰━╯┃╭╮┃╰┫╰━┫╰╯┃╰┫╰╯┃┃╰╯┃┃━┫┃┃╱╱┃┃┃┃━┫╰━┫╰╯┃┃╰╯┃╰╯┃┃╰━╯┃╭╮┃┃┃┃┃╰╯┃
╰━━━┻╯╰┻━┻━━┻━━┻━┻━━╯╰━━┻━━╯╰╯╱╱╰╯╰━━┻━━┻━━╯╰━━┻━━╯╰━━━┻╯╰┻╯╰╯╰━━╯

      
""")
#input
precoCarro=input("Digite o preço do carro: ")
#Processamento de Dados e Outputs
while precoCarro.isdigit()==False:
    precoCarro=input("\nO preço informado não é válido, por favor, digite novamente: ")
precoCarro=float(precoCarro)
porcentagem=20/100
precoFinal=precoCarro-(precoCarro*porcentagem)
print("\nO preço do carro à vista é de: R${:.2f}".format(precoFinal))
print("""
Para a opção parcelada, temos:
___________________________________________________________
| Preço Final | Quantidade de Parcelas | Valor da Parcela |""")
for parcela in range(6,61,6):
    porcentagem=(parcela/2)/100
    precoFinal=precoCarro+(precoCarro*porcentagem)
    valorParcela=precoFinal/parcela
    print(f"""________________________________________________________
|  {precoFinal:.2f}   |          {parcela}             |    {valorParcela:2.2f}    |""")
#Obs.: Como era para entregar uma tabela, assim o fiz mas, como também era pra utilizar uma estrutura de loop, a tabela não sairá com a estrutura perfeita no output.