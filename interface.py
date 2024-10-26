import tkinter as tk
from tkinter import messagebox, simpledialog
from gerenciador import (
    adicionar_missao, listar_missoes, buscar_missao_por_id,
    atualizar_missao, excluir_missao, pesquisar_missoes_por_data
)

def janela_criar_missao():

    janela = tk.Toplevel()
    janela.title("Adicionar Nova Missão")

    # Campos para entrada de dados
    tk.Label(janela, text="Nome:").grid(row=0, column=0)
    nome_entry = tk.Entry(janela)
    nome_entry.grid(row=0, column=1)

    tk.Label(janela, text="Data de Lançamento:").grid(row=1, column=0)
    data_entry = tk.Entry(janela)
    data_entry.grid(row=1, column=1)

    tk.Label(janela, text="Destino:").grid(row=2, column=0)
    destino_entry = tk.Entry(janela)
    destino_entry.grid(row=2, column=1)

    tk.Label(janela, text="Estado:").grid(row=3, column=0)
    estado_entry = tk.Entry(janela)
    estado_entry.grid(row=3, column=1)

    tk.Label(janela, text="Tripulação:").grid(row=4, column=0)
    tripulacao_entry = tk.Entry(janela)
    tripulacao_entry.grid(row=4, column=1)

    tk.Label(janela, text="Carga Útil:").grid(row=5, column=0)
    carga_entry = tk.Entry(janela)
    carga_entry.grid(row=5, column=1)

    tk.Label(janela, text="Duração:").grid(row=6, column=0)
    duracao_entry = tk.Entry(janela)
    duracao_entry.grid(row=6, column=1)

    tk.Label(janela, text="Custo:").grid(row=7, column=0)
    custo_entry = tk.Entry(janela)
    custo_entry.grid(row=7, column=1)

    tk.Label(janela, text="Status:").grid(row=8, column=0)
    status_entry = tk.Entry(janela)
    status_entry.grid(row=8, column=1)

    def confirmar_criacao():

        adicionar_missao(
            nome_entry.get(),
            data_entry.get(),
            destino_entry.get(),
            estado_entry.get(),
            tripulacao_entry.get(),
            carga_entry.get(),
            duracao_entry.get(),
            custo_entry.get(),
            status_entry.get()
        )
        janela.destroy()  # Fecha a janela
        messagebox.showinfo("Sucesso", "Missão adicionada com sucesso!")

    tk.Button(janela, text="Adicionar", command=confirmar_criacao).grid(row=9, column=0, columnspan=2)

def janela_listar_missoes():

    missoes = listar_missoes()  # Obtém a lista de missões
    janela = tk.Toplevel()
    janela.title("Listar Missões")
    for i, missao in enumerate(missoes):
        # Exibe cada missão em um label
        tk.Label(janela, text=f"{missao[0]}: {missao[1]} | {missao[3]} | {missao[4]}").pack()

def janela_buscar_missao():

    missao_id = simpledialog.askinteger("Input", "Digite o ID da missão:")
    if missao_id is not None:
        missao = buscar_missao_por_id(missao_id)
        janela = tk.Toplevel()
        janela.title("Detalhes da Missão")
        if missao:
            # Exibe os detalhes da missão encontrada
            detalhes = f"ID: {missao[0]}\nNome: {missao[1]}\nData de Lançamento: {missao[2]}\nDestino: {missao[3]}\nEstado: {missao[4]}\nTripulação: {missao[5]}\nCarga Útil: {missao[6]}\nDuração: {missao[7]}\nCusto: {missao[8]}\nStatus: {missao[9]}"
            tk.Label(janela, text=detalhes).pack()
        else:
            messagebox.showwarning("Não encontrado", "Missão não encontrada!")

def janela_pesquisar_missoes_por_data():

    janela = tk.Toplevel()
    janela.title("Pesquisar Missões por Data")

    tk.Label(janela, text="Data Inicial:").grid(row=0, column=0)
    data_inicial_entry = tk.Entry(janela)
    data_inicial_entry.grid(row=0, column=1)

    tk.Label(janela, text="Data Final:").grid(row=1, column=0)
    data_final_entry = tk.Entry(janela)
    data_final_entry.grid(row=1, column=1)

    def confirmar_pesquisa():

        data_inicial = data_inicial_entry.get()
        data_final = data_final_entry.get()
        missoes = pesquisar_missoes_por_data(data_inicial, data_final)
        janela_resultado = tk.Toplevel()
        janela_resultado.title("Resultados da Pesquisa")
        for missao in missoes:
            # Exibe os resultados encontrados
            tk.Label(janela_resultado, text=f"{missao[0]}: {missao[1]} | {missao[3]} | {missao[4]}").pack()

    tk.Button(janela, text="Pesquisar", command=confirmar_pesquisa).grid(row=2, column=0, columnspan=2)

def janela_atualizar_missao():

    janela = tk.Toplevel()
    janela.title("Atualizar Missão")

    missao_id = simpledialog.askinteger("Input", "Digite o ID da missão a ser atualizada:")
    if missao_id is not None:
        missao = buscar_missao_por_id(missao_id)
        if missao:
            # Campos de edição preenchidos com os dados da missão existente
            tk.Label(janela, text="Nome:").grid(row=0, column=0)
            nome_entry = tk.Entry(janela)
            nome_entry.insert(0, missao[1])
            nome_entry.grid(row=0, column=1)

            tk.Label(janela, text="Data de Lançamento:").grid(row=1, column=0)
            data_entry = tk.Entry(janela)
            data_entry.insert(0, missao[2])
            data_entry.grid(row=1, column=1)

            tk.Label(janela, text="Destino:").grid(row=2, column=0)
            destino_entry = tk.Entry(janela)
            destino_entry.insert(0, missao[3])
            destino_entry.grid(row=2, column=1)

            tk.Label(janela, text="Estado:").grid(row=3, column=0)
            estado_entry = tk.Entry(janela)
            estado_entry.insert(0, missao[4])
            estado_entry.grid(row=3, column=1)

            tk.Label(janela, text="Tripulação:").grid(row=4, column=0)
            tripulacao_entry = tk.Entry(janela)
            tripulacao_entry.insert(0, missao[5])
            tripulacao_entry.grid(row=4, column=1)

            tk.Label(janela, text="Carga Útil:").grid(row=5, column=0)
            carga_entry = tk.Entry(janela)
            carga_entry.insert(0, missao[6])
            carga_entry.grid(row=5, column=1)

            tk.Label(janela, text="Duração:").grid(row=6, column=0)
            duracao_entry = tk.Entry(janela)
            duracao_entry.insert(0, missao[7])
            duracao_entry.grid(row=6, column=1)

            tk.Label(janela, text="Custo:").grid(row=7, column=0)
            custo_entry = tk.Entry(janela)
            custo_entry.insert(0, missao[8])
            custo_entry.grid(row=7, column=1)

            tk.Label(janela, text="Status:").grid(row=8, column=0)
            status_entry = tk.Entry(janela)
            status_entry.insert(0, missao[9])
            status_entry.grid(row=8, column=1)

            def confirmar_atualizacao():

                atualizar_missao(missao_id, 
                    nome_entry.get(), 
                    data_entry.get(), 
                    destino_entry.get(), 
                    estado_entry.get(), 
                    tripulacao_entry.get(), 
                    carga_entry.get(), 
                    duracao_entry.get(), 
                    custo_entry.get(), 
                    status_entry.get())
                janela.destroy()  # Fecha a janela
                messagebox.showinfo("Sucesso", "Missão atualizada com sucesso!")

            tk.Button(janela, text="Atualizar", command=confirmar_atualizacao).grid(row=9, column=0, columnspan=2)

        else:
            messagebox.showwarning("Não encontrado", "Missão não encontrada!")

def janela_excluir_missao():

    janela = tk.Toplevel()
    janela.title("Excluir Missão")

    missao_id = simpledialog.askinteger("Input", "Digite o ID da missão a ser excluída:")
    if missao_id is not None:
        excluir_missao(missao_id)  # Exclui a missão pelo ID
        messagebox.showinfo("Sucesso", "Missão excluída com sucesso!")

def iniciar_interface():
    
    root = tk.Tk()
    root.title("Sistema de Gerenciamento de Expedições Espaciais")

    # Botões da interface principal
    tk.Button(root, text="Adicionar Nova Missão", command=janela_criar_missao).pack(pady=10)
    tk.Button(root, text="Listar Missões", command=janela_listar_missoes).pack(pady=10)
    tk.Button(root, text="Buscar Missão por ID", command=janela_buscar_missao).pack(pady=10)
    tk.Button(root, text="Pesquisar Missões por Data", command=janela_pesquisar_missoes_por_data).pack(pady=10)
    tk.Button(root, text="Atualizar Missão", command=janela_atualizar_missao).pack(pady=10)
    tk.Button(root, text="Excluir Missão", command=janela_excluir_missao).pack(pady=10)

    root.mainloop()  # Inicia o loop da interface gráfica
