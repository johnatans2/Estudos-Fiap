#Apresentação
print("""
    𝐶𝑎́𝑙𝑐𝑢𝑙𝑜 𝑑𝑒 𝐼𝑚𝑝𝑜𝑠𝑡𝑜 𝑑𝑒 𝑅𝑒𝑛𝑑𝑎
""")
#Declaração de Variáveis
ir=0
#Input e Validação de Dados
valorEntrada=input("Digite o valor que você depositou inicialmente: ")#Estou pedindo o valor do depósito inicial pois o exercício somente solicita que calcule o imposto de renda sobre o valor retirado, entretando, só há imposto de renda no que RENDEU, ou seja, acima do que já estava depositado. E se o usuário decidir retirar o valor depositado também? Ele terá imposto de renda sobre o que já tinha? Não. Por conta disso, também adicionei o input de rendimento, para fazer o montante correto
while valorEntrada.isdigit()==False:
    valorEntrada=input("\nO formato do valor de entrada digitado não é aceito, por favor, digite-o novamente: ")
valorEntrada=float(valorEntrada)
tipoInvestimento=input("""
Escolha a opção correspondente ao tipo de investimento na qual foi feito o depósito:

    1 - Certificado de Depósito Bancário(CDB)
    2 - Letra de Crédito Imobiliário(LCI)
    3 - Letra de Crédito do Agronegócio(LCA)
""")
while tipoInvestimento.isdigit()==False:
    tipoInvestimento=input("""
A opção escolhida não é válida, por favor digite o valor correspondente a uma das opções abaixo:
                           
    1 - Certificado de Depósito Bancário(CDB)
    2 - Letra de Crédito Imobiliário(LCI)
    3 - Letra de Crédito do Agronegócio(LCA)
""")
tipoInvestimento=int(tipoInvestimento)
while tipoInvestimento<1 or tipoInvestimento>3:
    tipoInvestimento=int(input("""
A opção escolhida não é válida, por favor digite o valor correspondente a uma das opções abaixo:
                           
    1 - Certificado de Depósito Bancário(CDB)
    2 - Letra de Crédito Imobiliário(LCI)
    3 - Letra de Crédito do Agronegócio(LCA)
"""))
dias=input("\nQuantos dias o valor foi mantido em investimento? ")
while dias.isdigit()==False:
    dias=input("\nO valor informado não é válido, por favor, digite novamente: ")
dias=int(dias)
rendimento=input("\nDigite a rentabilidade por mês do investimento em porcentagem (utilize somente números inteiros): ")
while rendimento.isdigit()==False:
    rendimento=input("\nVocê não digitou o valor da forma solicitada, digite novamente: ")
rendimento=int(rendimento)
retirar=input("\nQuanto você gostaria de retirar do investimento? ")
while retirar.isdigit()==False:
    retirar=input("\nPor favor, somente use números inteiros para informar a quantia a ser retirada: ")
retirar=float(retirar)
#Processamento de Dados
mes=int(dias/30)
montante=valorEntrada*((1+(rendimento/100))**mes)
juros=montante-valorEntrada
if tipoInvestimento==1:
    if dias<=180:
        ir=22.5
    elif 181<=dias<=360:
        ir=20
    elif 361<=dias<=720:
        ir=17.5
    else:
        ir=15
jurosComIR=juros-(juros*(ir/100))
if ir==0:
    valorFinal=valorEntrada+juros
else:
    valorFinal=valorEntrada+jurosComIR
#outputs
if valorFinal>=retirar:
    saldo=valorFinal-retirar
    if tipoInvestimento==1:
        print(f"""
Infelizmente o seu investimento possui o desconto do imposto de renda, tendo esses dados como resultado:
              
| Tipo de Investimento: | CDB
| Valor de Entrada:     | R${valorEntrada}
| Rendimento:           | {rendimento}% ao mês
| Tempo investido:      | {dias} dias ou {mes} meses
| Lucro sem IR:         | R${juros:.2f}
| Lucro com IR:         | R${jurosComIR:.2f}
| IR:                   | {ir}%
| Valor Antes do Saque: | R${valorFinal:.2f}
| Valor Retirado:       | R${retirar}
| Saldo Final:          | R${saldo:.2f}
--------------------------------
""")
    else:
        print(f"""
Felizmente o seu investimento não possui o desconto do imposto de renda, tendo esses dados como resultado:
              
| Tipo de Investimento: | {"LCI"if tipoInvestimento==2 else "LCA"}
| Valor de Entrada:     | R${valorEntrada}
| Rendimento:           | {rendimento}% ao mês
| Tempo investido:      | {dias} dias ou {mes} meses
| Lucro:                | R${juros:.2f}
| IR:                   | {ir}%
| Valor Antes do Saque: | R${valorFinal:.2f}
| Valor Retirado:       | R${retirar}
| Saldo Final:          | R${saldo:.2f}
--------------------------------
""")
else:
    print("\nA quantidade que você deseja retirar é maior do que a quantia que você tem disponível para saque")