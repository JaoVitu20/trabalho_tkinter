import tkinter as tk
from interface import (adicionar_missao_interface, listar_missoes_interface,
                       pesquisar_por_id_interface, pesquisar_por_intervalo_data_interface,
                       atualizar_missao_interface, excluir_missao_interface)

def main():
    # Criação da janela principal
    root = tk.Tk()
    root.title("Sistema de Gerenciamento de Expedição Espacial")

    # Botões para as funcionalidades
    tk.Button(root, text="Adicionar Missão", command=lambda: adicionar_missao_interface(
        entrada_nome, entrada_data, entrada_destino, entrada_estado, 
        entrada_tripulacao, entrada_carga, entrada_duracao, 
        entrada_custo, entrada_status)).pack(pady=10)

    tk.Button(root, text="Listar Missões", command=listar_missoes_interface).pack(pady=10)
    tk.Button(root, text="Pesquisar por ID", command=pesquisar_por_id_interface).pack(pady=10)
    tk.Button(root, text="Pesquisar por Intervalo de Datas", command=pesquisar_por_intervalo_data_interface).pack(pady=10)
    tk.Button(root, text="Atualizar Missão", command=atualizar_missao_interface).pack(pady=10)
    tk.Button(root, text="Excluir Missão", command=excluir_missao_interface).pack(pady=10)

    # Campos de entrada para adicionar uma nova missão
    tk.Label(root, text="Nome da Missão:").pack()
    entrada_nome = tk.Entry(root)
    entrada_nome.pack()

    tk.Label(root, text="Data de Lançamento (DD/MM/YYYY):").pack()
    entrada_data = tk.Entry(root)
    entrada_data.pack()

    tk.Label(root, text="Destino:").pack()
    entrada_destino = tk.Entry(root)
    entrada_destino.pack()

    tk.Label(root, text="Estado:").pack()
    entrada_estado = tk.Entry(root)
    entrada_estado.pack()

    tk.Label(root, text="Tripulação").pack()
    entrada_tripulacao = tk.Entry(root)
    entrada_tripulacao.pack()

    tk.Label(root, text="Carga:").pack()
    entrada_carga = tk.Entry(root)
    entrada_carga.pack()

    tk.Label(root, text="Duração:").pack()
    entrada_duracao = tk.Entry(root)
    entrada_duracao.pack()

    tk.Label(root, text="Custo:").pack()
    entrada_custo = tk.Entry(root)
    entrada_custo.pack()

    tk.Label(root, text="Status:").pack()
    entrada_status = tk.Entry(root)
    entrada_status.pack()

    # Inicia a interface
    root.mainloop()

if __name__ == "__main__":
    main()
