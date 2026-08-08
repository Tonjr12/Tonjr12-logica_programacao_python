# 📊 Processador Financeiro - Documentação do Projeto

Ferramenta de análise e gerenciamento financeiro desenvolvida em Python, evoluída de forma gradual a partir de conceitos fundamentais até uma arquitetura modular com menu interativo, validação de dados e controle de fluxo.

---

## 🎯 Contexto do Negócio
A diretoria da empresa solicitou uma ferramenta de análise para o fechamento de caixa diário, visando monitorar métricas financeiras cruciais e identificar variações nos tickets de venda.

---

## 🚀 Histórico de Evolução do Sistema

### 📌 Versão 1.0 - Indicadores Básicos (MVP)
* **Foco:** Processamento de vendas simples com laço de repetição fixo.
* **Recursos:** Cálculo do faturamento total e contagem de vendas de alto valor (> R$ 100,00).

### 📌 Versão 2.0 - Análise de Extremos
* **Foco:** Monitoramento da variação de ticket.
* **Recursos:** Identificação da maior e da menor venda registrada no lote.

### 📌 Versão 3.0 - Processamento Dinâmico e Validação
* **Foco:** Controle de fluxo contínuo.
* **Recursos:** Laço `while` com parada comandada pelo usuário e trava contra valores zerados ou negativos ($\le 0$).

### 📌 Versão 4.0 - Análise Estatística Expandida
* **Foco:** Métricas agregadas e filtragens.
* **Recursos:** Cálculo automatizado do Ticket Médio, `min()`, `max()`, `sum()` e filtragem com *List Comprehension*.

### 📌 Versão 5.0 - Ordenação e Rastreamento
* **Foco:** Relatórios cronológicos e ranking.
* **Recursos:** Histórico com `enumerate()` e ranking de vendas ordenado da maior para a menor com `sorted(reverse=True)`.

### 📌 Versão 6.0 - Estruturas Compostas e Unpacking
* **Foco:** Múltiplas informações por transação.
* **Recursos:** Armazenamento em listas aninhadas `[descricao, valor]`, desempacotamento (*unpacking*) e uso de *Generator Expression*.

### 📌 Versão 7.0 - Dicionários e Categorização
* **Foco:** Mapeamento estruturado de dados.
* **Recursos:** Mapeamento em Dicionários `{'descricao', 'reais', 'categoria'}` e tabela alinhada com formatadores de string.

### 📌 Versão 8.0 - Arquitetura Modular
* **Foco:** Organização em funções reutilizáveis.
* **Recursos:** Isolação de responsabilidades nas funções `ler_transacao()`, `calcular_estatisticas()` e `mostrando_posicao()`.

### 📌 Versão 9.0 - Tratamento de Erros e Validação Robusta
* **Foco:** Blindagem da entrada de dados.
* **Recursos:** Uso de `try / except ValueError` para ignorar letras em campos numéricos e tratamento com `strip()` contra campos vazios.

### 🏆 Versão 10.0 - Menu Interativo e Controle de Fluxo UX (Versão Atual)
* **Foco:** Transformação do script em uma aplicação navegável.
* **Recursos:**
  * Menu interativo no console (`exibir_menu()`).
  * Navegação livre entre cadastro, consulta de extrato, exibições estatísticas e encerramento.
  * Pausas de navegação estratégicas (`input()`) para garantir leitura confortável do extrato antes do retorno ao menu.

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3.x
* **Paradigma:** Programação Procedural / Modular
* **Estruturas de Dados:** Listas, Dicionários, Tuplas
* **Tratamento de Exceções:** Bloco `try / except` (`ValueError`)
* **Interface:** Terminal Interativo com controle de fluxo UX