# Exercício 054 — Criando um Menu de Opções

* **Objetivo:** Criar um programa que leia dois valores e mostre um menu de opções (somar, multiplicar, maior, novos números e sair). O programa deve realizar a operação solicitada e retornar ao menu até que a opção de sair seja escolhida.
* **Conceito Aplicado:** Repetição com `while`, estruturas condicionais aninhadas (`if/elif/else`), atualização dinâmica de variáveis de controle e tratamento de menus interativos.

### 💻 Código Solução

```python
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opcao = 0

while opcao != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}.')
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior é {n1}.')
        elif n2 > n1:
            print(f'O maior é {n2}.')
        else:
            print('Os dois números são iguais.')
    elif opcao == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.')

print('Fim do programa!')