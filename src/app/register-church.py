# Projeto ainda em desenvolvimento (Algumas funções podem ou não apresentar erros)
# Atualizações semanais.

import mysql.connector
from datetime import datetime
import time

import mysql.connector

class Database:
    def __init__(self, host="localhost", user="root", password="03092002", database="launch_WS", port=3306, ssl_disabled=True):
        self.connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="03092002",
            database="launch_WS",
            port="3306",
            ssl_disabled=False
        )
        self.cursor = self.connect.cursor()

    def close(self):
        self.cursor.close()
        self.connect.close()

    def close(self):
        self.cursor.close()
        self.connect.close()

class Member:
    def __init__(self, db):
        self.db = db

    def add(self, name, email, birth, adress, phone, baptims):
        birth_datetime = datetime.strptime(birth, "%Y-%m-%d")
        try:
            insert_data = """
            INSERT INTO member (name, email, birth, adress, phone, baptims)
            VALUES(%s, %s, %s, %s, %s, %s);
            """
            data = (name, email, birth_datetime, adress, phone, baptims)
            self.db.cursor.execute(insert_data, data)
            self.db.connect.commit()
            print("\nDados inseridos com sucesso!\n")
        except mysql.connector.errors.ProgrammingError as e:
            print("\nHouve um erro na gravação dos dados:\n", str(e))
            return False
        except Exception as e:
            print(f"\nAlgo errado aconteceu:\n{str(e)}")
            return False

    def find_member_by_id(self, member_id):
        query = 'SELECT * FROM member WHERE id = %s'
        self.db.cursor.execute(query, (member_id,))
        result = self.db.cursor.fetchone()
        if result:
            print(f"Membro encontrado: {result[1]} - ID: {result[0]}")
        else:
            print("Membro não encontrado.")

class Event:
    def __init__(self, db):
        self.db = db


    def find_event_by_id(self, event_id):
        query = 'SELECT * FROM event WHERE event_id = %s'
        self.db.cursor.execute(query, (event_id,))
        result = self.db.cursor.fetchone()
        if result[0] == 0:
            print('Código de evento inexistente!')
            return False
        else:
            if result:
                print(f"Evento encontrado: {result[1]} - ID: {result[0]}")
            else:
                print("Evento não encontrado.")

    def insert_new_event(self, title, description, date, place):
        date = datetime.strptime(date, '%Y-%m-%d')
        try:
            insert_date = '''INSERT INTO event (title, description, date, place) VALUES(%s, %s, %s, %s)'''
            self.db.cursor.execute(insert_date, (title, description, date, place))
            self.db.connect.commit()
            print("\nEvento inserido com sucesso!\n")
        except Exception as e:
            print("\nErro ao inserir novo evento no banco de dados!\n", str(e))
            return False


    def show_events(self):
        query = 'SELECT * FROM event'
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchall()
        x = 0
        while x <  len(result):
            for r in result :
                print(f'\n ID do evento: {r[0]} \n Título: {r[1]} \n Data: {r[3]} \n Local: {r[4]}')
                x += 1
        

class Presence:
    def __init__(self, db):
        self.db = db

    def add_presence(self, member_id, event_id, status):
        try:
            insert_data = """
            INSERT INTO presence (member_id, event_id, status, date, created_at)
            VALUES(%s, %s, %s, CURDATE(), CURRENT_TIMESTAMP);
            """
            data = (member_id, event_id, status)
            self.db.cursor.execute(insert_data, data)
            self.db.connect.commit()
            print("\nPresença adicionada com sucesso!\n")
        except mysql.connector.errors.ProgrammingError as e:
            print("\nHouve um erro na gravação dos dados:\n", str(e))
            return False
        except Exception as e:
            print(f"\nAlgo errado aconteceu:\n{str(e)}")
            return False

# Criar uma instância da classe Database para conectar ao banco de dados
db = Database()

# Verificar se a conexão foi realizada com sucesso
if db.connect.is_connected():
    print("Conectado \n")

# Função para interagir com o usuário
def interact_with_user(db):
    while True:
        time.sleep(2.5) # Aguarda 1,5 segundos
        print("""\nEscolha uma opção\n 
Digite 1 para ir à seção de eventos \n 
Digite 2 para ir à seção de membros \n
Digite 3 para adicionar presença \n
Digite 4 para consultar membros ou eventos \n
Digite 0 para encerrar\n""")
        choice = int(input(""))
        
        if choice == 1:
            event_id = int(input(""" Digite 1 para consultar evento\n Digite 2 para criar novo evento\n Digite 3 para ver todos os eventos:\n"""))
            event = Event(db)
            if event_id == 1:
                find_event = int(input("Digite o id do evento: "))
                event = Event(db)
                event.find_event_by_id(find_event)
            elif event_id == 2:
                name = input("Nome do evento: ")
                description = input("Descrição do evento: ")
                date = input("Data do evento: ")
                place = input("Local do evento: ")
                event.insert_new_event(name, description, date, place) 
            elif event_id == 3:
                event.show_events()
        elif choice == 2:
            member = Member(db)
            name = input("Digite o nome: ")
            email = input("Digite o email: ")
            birth = input("Digite a data de nascimento no formato AAAA-MM-DD: ")
            adress = input("Digite o endereço: ")
            phone = int(input("Digite o telefone (apenas números): "))
            baptism = input("Foi batizado? [S/N]: ").upper()
            member.add(name, email, birth, adress, phone, baptism)
        elif choice == 3:
            presence = Presence(db)
            member_id = int(input("Informe o ID do membro: "))
            event_id = int(input("Informe o ID do evento: "))
            status = input("Confirme presença ou falta (Use apenas P ou F): ").upper()
            presence.add_presence(member_id, event_id, status)
        elif choice == 4:
            print("Digite 1 para consultar membros por ID, 2 para consultar membros por nome, 3 para consultar eventos por ID, ou 0 para voltar ao menu principal.")
            sub_choice = int(input(""))
            if sub_choice == 1:
                member_id = int(input("Digite o ID do membro: "))
                member = Member(db)
                member.find_member_by_id(member_id)
            elif sub_choice == 2:
                name = input("Digite o nome do membro: ")
                member = Member(db)
                member.find_member_by_name(name) #TODO: Implement this method
            elif sub_choice == 3:
                event_id = int(input("Digite o ID do evento: "))
                event = Event(db)
                event.find_event_by_id(event_id)
            elif sub_choice == 0:
                pass # Voltar ao menu principal
            else:
                print("Opção inválida. Tente novamente.")
        elif choice == 0:
            print("Encerrando...\n")
            break
        else:
            print("Opção Inválida! Tente novamente.\n")

# Executar a função de interação
interact_with_user(db)

# Fechar conexão após a interação
db.close()
