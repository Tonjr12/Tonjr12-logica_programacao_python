## 🎯 Contexto do Negócio
A diretoria da empresa solicitou uma ferramenta de análise para o fechamento de caixa diário, visando monitorar métricas financeiras cruciais e identificar variações nos tickets de venda.

---

## 🚀 Evolução do Projeto

### 📌 Versão 1.0 - Indicadores Básicos (MVP)
* **Objetivo:** Processar o lote inicial de vendas e consolidar faturamento bruto e transações de alto valor.
* **Métricas:**
  * Faturamento Total Bruto.
  * Contagem de vendas acima de R$ 100,00.

### 📌 Versão 2.0 - Análise de Extremos
* **Objetivo:** Atender à solicitação da diretoria para identificar variações de ticket.
* **Novas Funcionalidades:**
  * Identificação da Maior Venda do dia.
  * Identificação da Menor Venda do dia.

### 📌 Versão 3.0 - Processamento Dinâmico e Validação
* **Objetivo:** Permitir o processamento de lotes ilimitados de transações diárias com validação de dados de entrada.
* **Novas Funcionalidades:**
  * Controle dinâmico de fluxo com laço `while` (parada comandada pelo usuário).
  * Validação de dados de entrada para impedir valores nulos ou negativos ($\le 0$).
  * Lógica de inicialização de extrema baseada no contador de transações.
  * Formatação de saída para exibições financeiras.

### 📌 Versão 4.0 - Análise Estatística Expandida
* **Objetivo:** Trazer relatórios automáticos e métricas agregadas.
* **Novas Funcionalidades:**
  * Cálculo automatizado do **Ticket Médio**, **Maior Venda** e **Menor Venda** com `min()`, `max()` e `sum()`.
  * Filtragem de transações de alto valor (acima de R$ 100,00) utilizando *List Comprehension*.
  * Organização das métricas estatísticas em painel formatado no console.

### 🟢 Versão 5.0 - Ordenação e Rastreamento (Versão Atual)
* **Objetivo:** Oferecer rastreamento cronológico de entradas e ranking de performance das vendas.
* **Novas Funcionalidades:**
  * **Histórico Cronológico:** Apresentação numerada de cada transação registrada utilizando `enumerate()`.
  * **Ranking de Vendas:** Exibição ordenada das vendas da maior para a menor usando `sorted(reverse=True)`.
  * **Melhorias de Layout:** Formatação visual refinada e padronização da exibição em moeda (`R$`).