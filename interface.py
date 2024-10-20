import tkinter as tk
from tkinter import messagebox, simpledialog
from gerenciador import (adicionar_missao, listar_missoes,
                         buscar_missao_por_id, buscar_missoes_por_intervalo_data,
                         atualizar_missao, excluir_missao)

def adicionar_missao_interface(entrada_nome, entrada_data, entrada_destino, entrada_estado, 
                                entrada_tripulacao, entrada_carga, entrada_duracao, 
                                entrada_custo, entrada_status):
    
    resultado = adicionar_missao(
        entrada_nome.get(),
        entrada_data.get(),
        entrada_destino.get(),
        entrada_estado.get(),
        entrada_tripulacao.get(),
        entrada_carga.get(),
        entrada_duracao.get(),
        entrada_custo.get(),
        entrada_status.get()
    )
    if resultado:
        messagebox.showinfo("Sucesso", "Missão adicionada com sucesso!")
        for entrada in [entrada_nome, entrada_data, entrada_destino, entrada_estado,
                        entrada_tripulacao, entrada_carga, entrada_duracao, 
                        entrada_custo, entrada_status]:
            entrada.delete(0, tk.END)  # Limpa os campos após a adição
    else:
        messagebox.showerror("Erro", "Falha ao adicionar a missão.")

def listar_missoes_interface():
    
    janela_listar = tk.Toplevel()
    janela_listar.title("Lista de Missões")
    
    missoes = listar_missoes()
    if missoes:
        for missao in missoes:
            tk.Label(janela_listar, text=f"ID: {missao['id']} - Nome: {missao['nome']} - Destino: {missao['destino']} - Estado: {missao['estado']}").pack()
    else:
        tk.Label(janela_listar, text="Nenhuma missão registrada.").pack()

def pesquisar_por_id_interface():
    
    id_missao = simpledialog.askinteger("Buscar Missão", "Digite o ID da missão:")
    if id_missao is not None:
        missao = buscar_missao_por_id(id_missao)
        if missao:
            messagebox.showinfo("Detalhes da Missão", f"ID: {missao['id']}\nNome: {missao['nome']}\nDestino: {missao['destino']}\nEstado: {missao['estado']}\nTripulação: {', '.join(missao['tripulacao'])}\nCarga: {missao['carga']}\nDuração: {missao['duracao']}\nCusto: {missao['custo']}\nStatus: {missao['status']}")
        else:
            messagebox.showerror("Erro", "Missão não encontrada.")

def pesquisar_por_intervalo_data_interface():
    
    janela_intervalo = tk.Toplevel()
    janela_intervalo.title("Pesquisar Missões por Intervalo de Datas")

    tk.Label(janela_intervalo, text="Data Inicial (DD/MM/YYYY):").grid(row=0, column=0)
    entrada_data_inicial = tk.Entry(janela_intervalo)
    entrada_data_inicial.grid(row=0, column=1)

    tk.Label(janela_intervalo, text="Data Final (DD/MM/YYYY):").grid(row=1, column=0)
    entrada_data_final = tk.Entry(janela_intervalo)
    entrada_data_final.grid(row=1, column=1)

    def buscar_missoes():
        data_inicial = entrada_data_inicial.get()
        data_final = entrada_data_final.get()
        try:
            missoes_encontradas = buscar_missoes_por_intervalo_data(data_inicial, data_final)
            janela_resultados = tk.Toplevel()
            janela_resultados.title("Resultados da Pesquisa")
            if missoes_encontradas:
                for missao in missoes_encontradas:
                    tk.Label(janela_resultados, text=f"ID: {missao['id']} - Nome: {missao['nome']} - Destino: {missao['destino']} - Data: {missao['data'].strftime('%d/%m/%Y')}").pack()
            else:
                tk.Label(janela_resultados, text="Nenhuma missão encontrada neste intervalo.").pack()
        except ValueError as e:
            messagebox.showerror("Erro", f"Data inválida: {e}")

    tk.Button(janela_intervalo, text="Pesquisar", command=buscar_missoes).grid(row=2, column=0, columnspan=2)

def atualizar_missao_interface():
    
    id_missao = simpledialog.askinteger("Atualizar Missão", "Digite o ID da missão a ser atualizada:")
    if id_missao is not None:
        missao = buscar_missao_por_id(id_missao)
        if missao:
            janela_atualizar = tk.Toplevel()
            janela_atualizar.title("Atualizar Missão")

            tk.Label(janela_atualizar, text="Novo Estado:").grid(row=0, column=0)
            entrada_estado = tk.Entry(janela_atualizar)
            entrada_estado.grid(row=0, column=1)

            tk.Label(janela_atualizar, text="Novo Destino:").grid(row=1, column=0)
            entrada_destino = tk.Entry(janela_atualizar)
            entrada_destino.grid(row=1, column=1)

            tk.Label(janela_atualizar, text="Nova Tripulação (separada por vírgula):").grid(row=2, column=0)
            entrada_tripulacao = tk.Entry(janela_atualizar)
            entrada_tripulacao.grid(row=2, column=1)

            tk.Label(janela_atualizar, text="Nova Carga:").grid(row=3, column=0)
            entrada_carga = tk.Entry(janela_atualizar)
            entrada_carga.grid(row=3, column=1)

            tk.Label(janela_atualizar, text="Nova Duração:").grid(row=4, column=0)
            entrada_duracao = tk.Entry(janela_atualizar)
            entrada_duracao.grid(row=4, column=1)

            tk.Label(janela_atualizar, text="Novo Custo:").grid(row=5, column=0)
            entrada_custo = tk.Entry(janela_atualizar)
            entrada_custo.grid(row=5, column=1)

            tk.Label(janela_atualizar, text="Novo Status:").grid(row=6, column=0)
            entrada_status = tk.Entry(janela_atualizar)
            entrada_status.grid(row=6, column=1)

            def atualizar():
                resultado = atualizar_missao(
                    id_missao,
                    entrada_estado.get(),
                    entrada_destino.get(),
                    entrada_tripulacao.get(),
                    entrada_carga.get(),
                    entrada_duracao.get(),
                    entrada_custo.get(),
                    entrada_status.get()
                )
                if resultado:
                    messagebox.showinfo("Sucesso", "Missão atualizada com sucesso!")
                    janela_atualizar.destroy()
                else:
                    messagebox.showerror("Erro", "Falha ao atualizar a missão.")

            tk.Button(janela_atualizar, text="Atualizar", command=atualizar).grid(row=7, column=0, columnspan=2)

        else:
            messagebox.showerror("Erro", "Missão não encontrada.")

def excluir_missao_interface():
   
    id_missao = simpledialog.askinteger("Excluir Missão", "Digite o ID da missão a ser excluída:")
    if id_missao is not None:
        resultado = excluir_missao(id_missao)
        if resultado:
            messagebox.showinfo("Sucesso", "Missão excluída com sucesso!")
        else:
            messagebox.showerror("Erro", "Missão não encontrada.")
