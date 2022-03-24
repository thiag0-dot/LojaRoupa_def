print(' ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢉⣽⣿⡿⠋⣽⣿⣿⠋⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿')
print(' ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠈⢻⡿⠁⠈⠻⣿⠃⠀⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿')
print(' ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⠇⢸⣇⠐⠿⠀⣿⠀⠿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿')
print(' ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣾⣿⣦⣤⣾⣿⣦⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿')
print('---------B E M - V I N D O----------')
print('-------A LOJA DE ROUPAS 666-------')
print('')

nome_cliente = input('Digite seu nome:')
print('-----------------------------------------------')

#fazendo as list /**
nomes_roupas = []
valores_uni = []
quantidades = []
venda_total = 0
#**/

#função /**
def inserindo_dados(nomes_roupas, valores_uni, quantidades):
    nomes_roupas.append(str(input('Digite o nome da peça de roupa:')))
    print('-----------------------------------------------')
    valores_uni.append(float(input('Digite o valor unitário da peça:')))
    print('-----------------------------------------------')
    quantidades.append(int(input('Digite a quantidade de peças de roupa compradas:')))
    print('-----------------------------------------------')
    return

#**/

#Fazendo a loja de roupa /**
while True:
    inserindo_dados(nomes_roupas, valores_uni, quantidades)
    opcao = str(input('Deseja continuar vendendo (S/N):')).upper()
    print('-----------------------------------------------')
    if opcao == 'N':
        break

x = len(nomes_roupas)
print('================ C O M P R A =====================')
for i in range(0, x):
    valor_total_compra = valores_uni[i] * quantidades[i]
    print('Nome da peça:{}'.format(nomes_roupas[i]))
    print('Preço da peça:R${:.2f}'.format(valores_uni[i]))
    print('Quantidade da peça de roupa:{}'.format(quantidades[i]))
    print('Valor total de:R${:.2f}'.format(valor_total_compra))
    print('-----------------------------------------------')
    venda_total += valor_total_compra


#Fazendo o pagamento /**
print('================ P A G A M E N T O =====================')
print("Valor Total da Compra: R${:.2f}".format(venda_total))
pagamento = float(input('Digite o pagamento do cliente:'))

if pagamento > venda_total :
    troco = pagamento - venda_total
    print('O troco vai ser de:R${:.2f}'.format(troco))
elif pagamento < venda_total:
    faltando = venda_total - pagamento
    print('Está faltando R$-{:.2f}!'.format(faltando))
    opcao = str(input('Tem dinheiro para pagar?(S/N)')).upper()
    if opcao == 'S':
        print('Pague:R${:.2f}')
    else :
        print('COMPPRA CANCELADA')
else :
    print('Pagamento está certo!')


#**/

print("")
print("+========================+")
print("| Obrigado volte sempre! |")
print("+========================+")

#**/   
