# Base de testes para testar novas formas de realizar o projeto

import mysql.connector
from datetime import datetime

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="03092002",
            database="launch_WS"
        )
        return connection
    except mysql.connector.Error as error:
        print("Erro ao conectar ao banco de dados:", error)
        return None

def close_connection(connection, cursor):
    try:
        cursor.close()
        connection.close()
        print("Conexão com o banco de dados fechada.")
    except mysql.connector.Error as error:
        print("Erro ao fechar a conexão com o banco de dados:", error)

def cap_data(connection):
    try:
        cursor = connection.cursor()

        # Captura de dados dos membros
        name = input("Digite o nome: ")
        email = input("Digite o email: ")
        birth_datetime = get_valid_datetime_input("Digite a data de nascimento no formato AAAA-MM-DD: ")
        address = input("Digite o endereço: ")
        phone = get_valid_integer_input("Digite o telefone (apenas números): ")
        baptism = get_valid_baptism_input()

        # Executar a inserção no banco de dados
        insert_data = """
            INSERT INTO member (name, email, birth, address, phone, baptism)
            VALUES(%s, %s, %s, %s, %s, %s);
        """
        data = (name, email, birth_datetime, address, phone, baptism)
        cursor.execute(insert_data, data)
        connection.commit()
        print("\nDados inseridos com sucesso!\n")
    except mysql.connector.Error as error:
        print("Erro ao inserir dados no banco de dados:", error)
    finally:
        cursor.close()

def get_valid_datetime_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            datetime_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return datetime_obj
        except ValueError:
            print("Data inválida! Tente novamente no formato AAAA-MM-DD.")

def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Valor inválido! Utilize somente números.")

def get_valid_baptism_input():
    while True:
        baptism = input("Foi batizado? [S/N]: ").upper()
        if baptism in ["S", "N"]:
            return baptism
        else:
            print("Opção Inválida! Utilize S ou N.")

def chose(connection, cursor):
    while True:
        print("""Escolha uma opção\n 
Digite 1 para ir à seção de eventos \n 
Digite 2 para ir à seção de membros \n
Digite 0 para encerrar\n""")
        chose_option = input("")
        if chose_option == '1':
            event(connection, cursor)
        elif chose_option == '2':
            presence(connection, cursor)
        elif chose_option == '0':
            print("Encerrando...")
            break
        else:
            print("Opção Inválida! Tente novamente.")

def presence(connection, cursor):
    try:
        member_id = input("Informe seu número de membro, ou digite 0 para cadastrar um membro: ")
        if member_id == '0':
            cap_data(connection)
        else:
            # Consultar membro no banco de dados e exibir informações
            pass
    except ValueError:
        print("Valor inválido! Digite um número ou 0 para cadastrar um membro.")
    except Exception as error:
        print("Erro:", error)

def event(connection, cursor):
    try:
        event_id = int(input("Digite o código do evento: "))
        if event_id != 0:
            # Consultar evento no banco de dados e realizar ações
            pass
    except ValueError:
        print("Valor inválido! Digite um número.")
    except Exception as error:
        print("Erro:", error)

# Conectar ao banco de dados
connection = connect_to_database()

if connection is not None:
    cursor = connection.cursor()
    chose(connection, cursor)
    close_connection(connection, cursor)
else:
    print("Falha ao conectar ao banco de dados. Encerrando o programa.")
