# 📊 Projeto Data Sales — v3.0

Módulo avançado de recepção, processamento em lote e consolidação de vendas em Python.

## 🎯 EVOLUÇÃO DO PROJETO

### 🔹 Funcionalidades da v1.0
* **Higienização de Entrada:** Remoção de espaços e padronização de nomes de clientes (`.title()`) e produtos (`.upper()`).
* **Geração de Hash/ID:** Criação de ID aleatório único de transação via biblioteca `random`.
* **Cálculos Logísticos:** Arredondamento com `math.ceil()`.
* **Fatiamento de Nomes:** Isolamento do primeiro nome do cliente.

### 🔹 Funcionalidades da v2.0
* **Sanitização de Entrada:** Formatação automática com `.strip()`, `.title()` e `.upper()`.
* **Validação de Dados:** Bloqueio de processamento caso valores e quantidades sejam `<= 0`.
* **Política Comercial de Descontos:** Aplicação condicional de 10% de desconto para compras acima de R$ 500,00.

### 🚀 Novidades da v3.0 (Módulo 7 - Laços de Repetição)
* **Processamento em Lote:** Leitura de múltiplas vendas consecutivas utilizando a estrutura de repetição `for`.
* **Acumuladores Financeiros:** Cálculo do faturamento total acumulado do lote (`soma_total += valor_liquido`).
* **Métricas Consolidadas:** Geração de relatório final com faturamento total líquido e média por venda.

## 🚀 Como Executar
```bash
python main.py