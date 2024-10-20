from datetime import datetime

# Lista para armazenar as missões
missoes = []

def adicionar_missao(nome, data_lancamento, destino, estado, tripulacao, carga, duracao, custo, status):
    
    try:
        # Verifica se todos os campos estão preenchidos
        if not all([nome, data_lancamento, destino, estado, tripulacao, carga, duracao, custo, status]):
            raise ValueError("Todos os campos devem ser preenchidos.")

        # Tenta converter a data de lançamento para o formato correto
        data_lancamento = datetime.strptime(data_lancamento, "%d/%m/%Y")
        
        # Cria um novo dicionário para a missão
        nova_missao = {
            "id": len(missoes) + 1,  # Gera um ID único
            "nome": nome,
            "data": data_lancamento,
            "destino": destino,
            "estado": estado,
            "tripulacao": tripulacao.split(','),
            "carga": carga,
            "duracao": duracao,
            "custo": float(custo),
            "status": status
        }

        # Adiciona a nova missão à lista
        missoes.append(nova_missao)
        return True
    except ValueError as e:
        print(f"Erro ao adicionar missão: {e}")
        return False

def listar_missoes():
    
    return sorted(missoes, key=lambda x: x['data'], reverse=True)

def buscar_missao_por_id(id_missao):
    
    for missao in missoes:
        if missao['id'] == id_missao:
            return missao
    return None

def buscar_missoes_por_intervalo_data(data_inicial, data_final):
    
    data_inicial = datetime.strptime(data_inicial, "%d/%m/%Y")
    data_final = datetime.strptime(data_final, "%d/%m/%Y")
    return [missao for missao in missoes if data_inicial <= missao['data'] <= data_final]

def atualizar_missao(id_missao, estado, destino, tripulacao, carga, duracao, custo, status):
    
    missao = buscar_missao_por_id(id_missao)
    if missao:
        # Atualiza os campos da missão
        missao['estado'] = estado
        missao['destino'] = destino
        missao['tripulacao'] = tripulacao.split(',')
        missao['carga'] = carga
        missao['duracao'] = duracao
        missao['custo'] = float(custo)
        missao['status'] = status
        return True
    return False

def excluir_missao(id_missao):
    
    global missoes
    missoes = [missao for missao in missoes if missao['id'] != id_missao]
    return len(missoes) < len(missoes) + 1  # Retorna True se a missão foi excluída
