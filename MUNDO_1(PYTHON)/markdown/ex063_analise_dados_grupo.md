# Exercício 063 — Análise de Dados do Grupo

* **Objetivo:** Ler a idade e o sexo de várias pessoas, perguntando a cada registo se o utilizador deseja continuar. No final, exibir estatísticas de maiores de idade, total de homens e mulheres com menos de 20 anos.
* **Conceito Aplicado:** Laço infinito (`while True`), validação de dados com filtros `in 'MF'` e `in 'SN'`, contadores condicionais múltiplos e estruturação de relatórios finais.

### 💻 Código Solução

```python
tot18 = totH = totM20 = 0

while True:
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Dados inválidos. Digite o sexo: [M/F] ')).strip().upper()[0]
        
    idade = int(input('Digite a idade: '))
    
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
        
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totH}')
print(f'Total de mulheres com menos de 20 anos: {totM20}')