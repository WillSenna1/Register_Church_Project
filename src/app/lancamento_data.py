import mysql.connector
from datetime import datetime

#ALTERAÇÃO A FAZER, 

#Criando funções

#************************************************************************************************
# Função para decidir se fará consulta, ou cadastro.
def presence():
    member_id = int(input("Informe seu número de membro: "))
    if member_id != 0:
        cursor.execute("SELECT * FROM member WHERE id = %s", (member_id,))
        result_member = cursor.fetchone()
        if result_member is None:
            print(f"O número de membro {member_id} não foi encontrado!")
            return member_id
        else:
            print('Detalhes...')
            print(f'\n Nome:', result_member[1], '\n ID:', result_member[0], '\n Email:', result_member[2], '\n Data de Nascimento:', result_member[3], '\n Endereco:', result_member[4], '\n Telefone:', result_member[5])
    else:
        cap_data()
        return


def event():
    event_id = int(input("Digite o código do evento: "))
    if event_id != 0:
        query = 'SELECT COUNT(*) FROM event WHERE id = %s'
        cursor.execute(query, (event_id,))
        result_event = cursor.fetchone()
        if result_event[0] == 0:
            print('Código de evento inexistente!')
            return event_id
        else:
            pass


def stats():        
    status = input("Confirme presença ou falta (Use apenas P ou F respectivamente: ")
    status_option = ["P", "F"]
    if status.upper() not in status_option:
        print("Opção inválida! Use apenas P ou F.")
        return status
    else:
        insert_data = """
        INSERT INTO status (status)
        VALUES(%s)"""
        data = (status)
        cursor.execute(insert_data, data)
        if insert_data is True:
            print("\n Presença adicionada com sucesso!\n")
            insert_data = """
            INSERT INTO presence (status)
            VALUES(%s);"""
        

        

# Captura de dados dos membros


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
            print("Data inválida! Tente novamente no formato AAAA/MM/DD.")
    adress = input("Digite o endereço: ")
    while True:
        try:
            phone = int(input("Digite o telefone (apenas numeros): "))
            break
        except ValueError:
            print("Valor inválido! Utilize somente números.")
            return phone
        except Exception as e:
            print("Ocorreu um erro ao tentar capturar os dados.\nErro: ", str(e))
        return phone
    baptism = input("Foi batizado? [S/N]: ").upper()
    if baptism not in ["S", "N"]:
        print("Opção Inválida! Utilize S ou N.")
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


# Conectar ao banco de dados
connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="03092002",
    database="launch_WS"
)

# Verificar  se a conexão foi realizada com sucesso
if  connect.is_connected():
    print("Conectado \n")

#  Criar um cursor para executar as querys SQL
cursor = connect.cursor()

connect.commit()

#******************** TESTE  ******************** */
print("""Escolha uma opção\n 
Digite 1 para ir à seção de eventos \n 
Digite 2 para ir à seção de membros \n
Digite 0 para encerrar""")
chose1 = int(input(""))
while chose1 in [1, 2, 0]:
    if chose1 == 1:
        event()
    elif chose1 == 2:
        presence()
    elif chose1 == 0:
        print("Encerrando...")
    else:
        print("Opção Inválida! Tente novamente.")
        

#******************** TESTE  ******************** */

#Fechar conexão
cursor.close()
connect.close()