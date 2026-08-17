import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from financas.arquivo import carregar_dados, salvar_dados
from financas.operacoes import calcular_estatisticas, normalizar


class ProcessadorFinanceiroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Processador Financeiro - Versão Gráfica")
        self.root.geometry("750x500")
        self.root.minsize(650, 450)

        # Carrega os dados do arquivo JSON
        self.transacoes = carregar_dados()

        # --- TÍTULO ---
        titulo_label = tk.Label(root, text="Processador Financeiro", font=("Arial", 16, "bold"))
        titulo_label.pack(pady=10)

        # --- ÁREA DA TABELA (EXTRATO) ---
        self.tree_frame = tk.Frame(root)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        # Configuração da tabela (Treeview)
        colunas = ("Nº", "Estabelecimento", "Categoria", "Valor")
        self.tree = ttk.Treeview(self.tree_frame, columns=colunas, show="headings", selectmode="browse")

        self.tree.heading("Nº", text="Nº")
        self.tree.heading("Estabelecimento", text="Estabelecimento")
        self.tree.heading("Categoria", text="Categoria")
        self.tree.heading("Valor", text="Valor (R$)")

        self.tree.column("Nº", width=50, anchor=tk.CENTER)
        self.tree.column("Estabelecimento", width=250, anchor=tk.W)
        self.tree.column("Categoria", width=180, anchor=tk.W)
        self.tree.column("Valor", width=120, anchor=tk.E)

        # Barra de rolagem para a tabela
        scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # --- PAINEL DE BOTÕES ---
        botoes_frame = tk.Frame(root)
        botoes_frame.pack(fill=tk.X, padx=20, pady=15)

        # Linha 1 de botões
        btn_cadastrar = tk.Button(botoes_frame, text="➕ Nova Transação", bg="#4CAF50", fg="white",
                                  font=("Arial", 10, "bold"), command=self.cadastrar)
        btn_cadastrar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        btn_editar = tk.Button(botoes_frame, text="✏️ Editar", bg="#FF9800", fg="white", font=("Arial", 10, "bold"),
                               command=self.editar)
        btn_editar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        btn_excluir = tk.Button(botoes_frame, text="🗑️ Excluir", bg="#F44336", fg="white", font=("Arial", 10, "bold"),
                                command=self.excluir)
        btn_excluir.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        btn_estatisticas = tk.Button(botoes_frame, text="📊 Estatísticas", bg="#2196F3", fg="white",
                                     font=("Arial", 10, "bold"), command=self.estatisticas)
        btn_estatisticas.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        # Linha 2 de botões
        btn_filtrar = tk.Button(botoes_frame, text="🔍 Filtrar Categoria", bg="#9C27B0", fg="white",
                                font=("Arial", 10, "bold"), command=self.filtrar)
        btn_filtrar.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        btn_relatorio = tk.Button(botoes_frame, text="📋 Relatório Sintético", bg="#607D8B", fg="white",
                                  font=("Arial", 10, "bold"), command=self.relatorio)
        btn_relatorio.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        btn_atualizar = tk.Button(botoes_frame, text="🔄 Atualizar Lista", bg="#00BCD4", fg="white",
                                  font=("Arial", 10, "bold"), command=self.atualizar_tabela)
        btn_atualizar.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        btn_sair = tk.Button(botoes_frame, text="❌ Sair", bg="#9E9E9E", fg="white", font=("Arial", 10, "bold"),
                             command=root.quit)
        btn_sair.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

        # Ajustar pesos das colunas do grid de botões para redimensionarem bem
        for i in range(4):
            botoes_frame.columnconfigure(i, weight=1)

        # Atualiza a tabela com os dados iniciais
        self.atualizar_tabela()

    def atualizar_tabela(self, dados=None):
        """Limpa e preenche a tabela visual com a lista de transações."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        lista_exibicao = dados if dados is not None else self.transacoes
        for pos, item in enumerate(lista_exibicao, start=1):
            self.tree.insert("", tk.END,
                             values=(f"{pos:02d}°", item["descricao"], item["categoria"], f"R$ {item['reais']:.2f}"))

    def cadastrar(self):
        """Janela interativa para cadastrar uma nova transação."""
        descricao = simpledialog.askstring("Cadastro", "Digite o nome do estabelecimento:")
        if not descricao:
            return

        valor_str = simpledialog.askstring("Cadastro", "Digite o valor do gasto (ex: 25.50):")
        if not valor_str:
            return

        try:
            valor = float(valor_str.replace(',', '.'))
            if valor <= 0:
                messagebox.showerror("Erro", "O valor deve ser maior que zero.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido.")
            return

        categoria = simpledialog.askstring("Cadastro", "Digite a categoria do estabelecimento:")
        if not categoria:
            return

        nova_transacao = {
            'descricao': descricao.strip().title(),
            'reais': valor,
            'categoria': categoria.strip().title()
        }

        self.transacoes.append(nova_transacao)
        salvar_dados(self.transacoes)
        self.atualizar_tabela()
        messagebox.showinfo("Sucesso", "Transação cadastrada e salva com sucesso!")

    def excluir(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma transação na tabela!")
            return

        # Pega o índice da linha selecionada
        item_index = self.tree.index(selecionado[0])

        # Confirmação antes de deletar
        if messagebox.askyesno("Confirmar", "Deseja realmente excluir esta transação?"):
            removido = self.transacoes.pop(item_index)
            salvar_dados(self.transacoes)
            self.atualizar_tabela()
            messagebox.showinfo("Sucesso", f"'{removido['descricao']}' excluído!")

    def editar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma transação para editar!")
            return

        item_index = self.tree.index(selecionado[0])
        item = self.transacoes[item_index]

        # Edição simples (Pode ser melhorada com janelas customizadas depois)
        nova_desc = simpledialog.askstring("Editar", "Nova descrição:", initialvalue=item['descricao'])
        if nova_desc:
            item['descricao'] = nova_desc.strip().title()
            salvar_dados(self.transacoes)
            self.atualizar_tabela()
    def estatisticas(self):
        """Exibe o total e a média dos gastos."""
        if not self.transacoes:
            messagebox.showwarning("Aviso", "Nenhuma transação registrada.")
            return

        total, media = calcular_estatisticas(self.transacoes)
        messagebox.showinfo("Estatísticas Gerais",
                            f"Total dos Lançamentos: R$ {total:.2f}\nMédia por Lançamento: R$ {media:.2f}")

    def filtrar(self):
        """Filtra e exibe transações de uma categoria específica."""
        busca = simpledialog.askstring("Filtrar por Categoria", "Digite a categoria que deseja buscar:")
        if not busca:
            return

        busca_limpa = normalizar(busca)
        filtrados = [t for t in self.transacoes if busca_limpa in normalizar(t['categoria'])]

        if not filtrados:
            messagebox.showinfo("Filtro", f"Nenhuma transação encontrada para '{busca}'.")
            self.atualizar_tabela()
        else:
            self.atualizar_tabela(filtrados)
            tot = sum(t["reais"] for t in filtrados)
            messagebox.showinfo("Filtro", f"Encontradas {len(filtrados)} transações.\nTotal da Categoria: R$ {tot:.2f}")

    def relatorio(self):
        """Gera e exibe um relatório sintético por categoria."""
        if not self.transacoes:
            messagebox.showwarning("Aviso", "Nenhuma transação registrada.")
            return

        resumo = {}
        for t in self.transacoes:
            cat = t['categoria']
            resumo[cat] = resumo.get(cat, 0) + t['reais']

        texto_relatorio = "Relatório Sintético por Categoria:\n\n"
        for cat, tot in resumo.items():
            texto_relatorio += f"• {cat}: R$ {tot:.2f}\n"

        messagebox.showinfo("Relatório Sintético", texto_relatorio)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProcessadorFinanceiroApp(root)
    root.mainloop()