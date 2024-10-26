from database import criar_tabela
from interface import iniciar_interface

def main():
    criar_tabela() # Cria a tabela de missões no banco de dados, se necessário
    iniciar_interface() # Inicia a interface gráfica

if __name__ == "__main__":
    main() 
    # Executa a função principal ao rodar o script
