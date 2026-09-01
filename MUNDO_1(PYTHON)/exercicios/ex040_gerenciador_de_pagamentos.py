# Entrada do valor total das compras
preco = float(input('Digite o valor total das compras: R$ '))

# Exibição do menu de formas de pagamento
print('=' * 10, 'FORMAS DE PAGAMENTO', '=' * 10)
print('[ 1 ] à vista dinheiro/PIX (10% de desconto)')
print('[ 2 ] à vista no cartão (5% de desconto)')
print('[ 3 ] em até 2x no cartão (preço formal)')
print('[ 4 ] 3x ou mais no cartão (20% de juros)')

opcao = int(input('Qual é a opção? '))

# Processamento das regras de negócio com condicionais
if opcao == 1:
    total = preco - (preco * 0.10)
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} com 10% de desconto.')
elif opcao == 2:
    total = preco - (preco * 0.05)
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} com 5% de desconto.')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.')
    print(f'Sua compra vai custar R$ {total:.2f}.')
elif opcao == 4:
    totpar = int(input('Quantas parcelas? '))
    total = preco + (preco * 0.20)
    parcela = total / totpar
    print(f'Sua compra será parcelada em {totpar}x de R$ {parcela:.2f} COM JUROS.')
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.')
else:
    print('OPÇÃO INVALÍDA de pagamento. Tente novamente!')