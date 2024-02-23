#RESET DATABASE

import mysql.connector

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

def presence():
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
presence()