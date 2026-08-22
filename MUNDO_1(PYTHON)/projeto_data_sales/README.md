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