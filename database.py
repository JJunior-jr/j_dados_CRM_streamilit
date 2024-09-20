import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
# esta lib pega as credenciais que estão setadas no ".env" e exportam para o seu hantime(variáveis de ambiente)
from dotenv import load_dotenv
import os  # esta lib(módulo) trabalha com as questões do sistema operacional

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
# Não se deve colocar as credenciais direto aqui nesta pasta, é necessário criar uma constante e deixa-la na passta ".env" ou outra para que depois seja mencionada no ".gitignore"
# o "getenv()" pega as variaveis que setou no .env e tras para o código
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para salvar os dados validados no PostgreSQL


def salvar_no_postgres(dados: Vendas):
    """
    Função para salvar no postgres
    """
    try:  # este bloco faz a conexão com o BD
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()  # o cursor seria uma sequencia de inserção no BD

        # Inserção dos dados na tabela de vendas
        # Aqui é feito o INSERT como se fosse feito direto no BD

        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))
        conn.commit() #essa salva no postgres
        cursor.close() #Aqui eu fecho o curso
        conn.close() # aqui fecha a conexão
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")
