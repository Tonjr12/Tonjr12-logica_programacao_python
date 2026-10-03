# Exercício 065 — Simulador de Caixa Eletrônico

Objetivo: Simular um caixa eletrônico que informa quantas cédulas de R$ 50, R$ 20, R$ 10 e R$ 1 serão entregues para um determinado valor de saque.
Conceito Aplicado: Operadores aritméticos avançados de divisão inteira // e resto de divisão %, laço while True com quebra de fluxo e reatribuição dinâmica de valores de controle.

 💻 Código Solução

'''python
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
tot_ced = 0

while True:
    if total >= ced:
        tot_ced = total // ced
        total %= ced
        print(f'Total de {tot_ced} cédulas de R$ {ced}')
        
    if ced == 50:
        ced = 20
    elif ced == 20:
        ced = 10
    elif ced == 10:
        ced = 1
        
    if total == 0:
        break