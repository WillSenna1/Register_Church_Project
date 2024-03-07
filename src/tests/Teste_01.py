# Base de teste para testar novas funções

import mysql.connector
import keyboard
import datetime

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="03092002",
    database="launch_WS"
)

# Verificar  se a conexão foi realizada com sucesso
if  connect.is_connected():
    print("Conectado")

#  Criar um cursor para executar as querys SQL
cursor = connect.cursor()

connect.commit()
"""

clear_table_query = "DELETE FROM member"
cursor.execute(clear_table_query)
connect.commit()
# Verificar se a tabela foi limpa
if  cursor.rowcount == 0:
    print("Tabela 'member' limpa!")

reset_autoincrement_query = "ALTER TABLE member AUTO_INCREMENT = 1"
cursor.execute(reset_autoincrement_query)
connect.commit()"""


# TENTANDO FAZER IMPRIMIR APENAS O MEMBRO DO ID CORRESPONDENTE

"""def presence():
    member_id = int(input("Informe seu número de membro (ou digite 0 para cadastrar novo): "))
    if member_id != 0:
        cursor.execute("SELECT * FROM member WHERE id = %s", (member_id,))
        result_member = cursor.fetchone()
        if result_member is None:
            print(f"O número de membro {member_id} não foi encontrado!")
            return member_id
        else:
            print('Detalhes...')
            print(f'\n Nome:', result_member[1], '\n ID:', result_member[0], '\n Email:', result_member[2], '\n Data de Nascimento:', result_member[3], '\n Endereco:', result_member[4], '\n Telefone:', result_member[5])
presence()"""

def event():
    event_id = int(input("Digite o código do evento: \n"))
    if event_id != 0:
        query = 'SELECT COUNT(*) FROM event WHERE id = %s'
        cursor.execute(query, (event_id,))
        result_event = cursor.fetchone()
        if result_event[0] == 0:
            print('Código de evento inexistente!\n')
            return event_id
        else:
            pass

def cap_data():    
    connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="03092002",
    database="launch_WS"
    )
    cursor = connect.cursor()

    name = input("Digite o nome: ")
    email = input("Digite o email: ")
    while True:
        birth_str = input("Digite a data de nascimento no formato AAAA/MM/DD: ")
        try:
            birth_datetime = datetime.strptime(birth_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Data inválida! Tente novamente no formato AAAA/MM/DD.\n")
    adress = input("Digite o endereço: ")
    while True:
        try:
            phone = int(input("Digite o telefone (apenas numeros): "))
            break
        except ValueError:
            print("Valor inválido! Utilize somente números.\n")
            return phone
        except Exception as e:
            print("Ocorreu um erro ao tentar capturar os dados.\nErro: \n", str(e))
        return phone
    baptism = input("Foi batizado? [S/N]: ").upper()
    if baptism not in ["S", "N"]:
        print("Opção Inválida! Utilize S ou N.\n")
        return baptism
    try:
        insert_data = """
        INSERT INTO member (name, email, birth, adress, 
        phone, baptims)
        VALUES(%s, %s, %s, %s, %s, %s);
        """
        data = (name, email, birth_datetime, adress, phone, baptism)
        cursor.execute(insert_data, data)
        print("\nDados inseridos com sucesso!\n")
        connect.commit()

    except mysql.connector.errors.ProgrammingError as e:
        print("\nHouve um erro na gravação dos dados:\n", str(e))
        return False
    except Exception as e:
        print(f"\nAlgo errado aconteceu:\n{str(e)}")
        return False


def on_key_event(event):
    if event.name == 'esc':
        chose()  # Chama a função chose() se a tecla "Esc" for pressionada

def presence():
    while True:
        member_id = input("Informe seu número de membro, ou digite 0 para cadastrar um membro, ou pressione a tecla 'esc' para voltar ao menu principal: \n")
        if member_id.isdigit():  # Verifica se a entrada é um número
            member_id = int(member_id)
            if member_id == 0:
                cap_data()
                return
            else:
                try:
                    cursor.execute("SELECT * FROM member WHERE id = %s", (member_id,))
                    result_member = cursor.fetchone()
                    if result_member is None:
                        print(f"O número de membro {member_id} não foi encontrado!\n")
                    else:
                        print('Detalhes...\n')
                        print(f'\n Nome:', result_member[1], '\n ID:', result_member[0], '\n Email:', result_member[2], '\n Data de Nascimento:', result_member[3], '\n Endereco:', result_member[4], '\n Telefone:', result_member[5])
                except Exception as e:
                    print("Erro na busca por dados do membro!\n", str(e))
        elif member_id.lower() == 'esc':  # Se o usuário digitar "esc" em qualquer caso (maiúsculas ou minúsculas)
            print("\nVoltando ao menu principal...\n")
            chose()
            return
        else:
            print("Entrada inválida. Por favor, insira um número de membro válido ou 'esc' para voltar ao menu principal.\n")


keyboard.on_press(on_key_event)

# Chama a função presence() para iniciar o programa


def chose():
    while True:
        print("""Escolha uma opção\n 
Digite 1 para ir à seção de eventos \n 
Digite 2 para ir à seção de membros \n
Digite 0 para encerrar\n""")
        chose1 = int(input(""))
        while chose1 in [1, 2, 0]:
            if chose1 == 1:
                event()
            elif chose1 == 2:
                presence()
            elif chose1 == 0:
                print("Encerrando...\n")
                break
                return 
            else:
                print("Opção Inválida! Tente novamente.\n")


# Você precisa definir a função chose() em algum lugar, mas ela não está no código fornecido
chose()
