# 📊 Projeto Data Sales — v1.0

Módulo de inicialização e recepção de dados de vendas desenvolvido em Python para validação e limpeza de transações comerciais.

## 🎯 Funcionalidades da v1.0
* **Higienização de Entrada:** Remoção de espaços e padronização de nomes de clientes (`.title()`) e produtos (`.upper()`).
* **Geração de Hash/ID:** Criação de ID aleatório único de transação via biblioteca `random`.
* **Cálculos Logísticos e Financeiros:** Arredondamento logístico com `math.ceil()` e cálculo de faturamento bruto.
* **Fatiamento de Nomes:** Isolamento do primeiro nome do cliente para mensagens de confirmação de pedido.

## 🚀 Como Executar
```bash
python projeto_data_sales/main.py
# 📊 Projeto Data Sales — v2.0

Módulo avançado de recepção, validação e aplicação de regras de negócio em transações de vendas desenvolvido em Python.

## 🎯 Funcionalidades da v2.0
* **Sanitização de Entrada:** Formatação automática com `.strip()`, `.title()` e `.upper()`.
* **Validação de Dados:** Bloqueio de processamento caso valores e quantidades sejam `<= 0`.
* **Geração de Hash/ID:** Criação de ID aleatório via `random.randint()`.
* **Cálculos Logísticos:** Arredondamento para caixas via `math.ceil()` e alertas condicionais para transportes de grande porte.
* **Política Comercial de Descontos:** Aplicação condicional de 10% de desconto para compras acima de R$ 500,00.

## 🚀 Como Executar
```bash
python projeto_data_sales/main.py