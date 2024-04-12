#Apresentação
print("""
    ℂ𝕠𝕟𝕥𝕒𝕓𝕚𝕝𝕚𝕕𝕒𝕕𝕖 𝕕𝕖 𝔼𝕞𝕡𝕣𝕖́𝕤𝕥𝕚𝕞𝕠
""")
#Declaração de Variáveis
caso=0
#input
divida=input("Por favor, digite o valor do empréstimo: ")
#Processamento de dados e Outputs
while divida.isdigit()==False:
    divida=input("\nO valor informado não é válido, por favor digite novamente: ")
divida=float(divida)
for parcela in range(0,13,3):
    if parcela==0:
        parcela+=1
        porcentagem=0
    elif parcela==3:
        porcentagem=0.1
    else:
        porcentagem+=0.05
    caso+=1
    juros=divida*porcentagem
    total=divida+juros
    valorParcela=total/parcela
    print(f"""
{caso}ª opção de empréstimo:
------------------------------
Total da dívida:   | R${total:.2f}
Juros:             | R${juros:.2f}
Número de Parcelas | {parcela}
Valor da Parcela   | R${valorParcela:.2f}
-------------------------------
""")