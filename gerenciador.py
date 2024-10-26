from database import conectar

def adicionar_missao(nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status):

    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO missoes (nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status))
        conn.commit()  # Confirma a inserção
        conn.close()  # Fecha a conexão
        print("Missão adicionada com sucesso!")

def listar_missoes():

    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM missoes ORDER BY data_lancamento DESC')  # Busca todas as missões
        missoes = cursor.fetchall()  # Obtém todos os resultados
        conn.close()  # Fecha a conexão
        return missoes
    return []

def buscar_missao_por_id(missao_id):

    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM missoes WHERE id = ?', (missao_id,))  # Busca a missão pelo ID
        missao = cursor.fetchone()  # Obtém o resultado
        conn.close()  # Fecha a conexão
        return missao
    return None

def atualizar_missao(missao_id, nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status):

    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE missoes 
            SET nome = ?, data_lancamento = ?, destino = ?, estado = ?, tripulacao = ?, carga_util = ?, duracao = ?, custo = ?, status = ?
            WHERE id = ?
        ''', (nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status, missao_id))
        conn.commit()  # Confirma as alterações
        conn.close()  # Fecha a conexão
        print("Missão atualizada com sucesso!")

def excluir_missao(missao_id):

    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM missoes WHERE id = ?', (missao_id,))  # Exclui a missão pelo ID
        conn.commit()  # Confirma a exclusão
        conn.close()  # Fecha a conexão
        print("Missão excluída com sucesso!")

def pesquisar_missoes_por_data(data_inicial, data_final):

    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM missoes 
            WHERE data_lancamento BETWEEN ? AND ?
            ORDER BY data_lancamento DESC
        ''', (data_inicial, data_final))  # Busca missões entre as datas
        missoes = cursor.fetchall()  # Obtém todos os resultados
        conn.close()  # Fecha a conexão
        return missoes
    return []
