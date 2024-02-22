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

"""clear_table_query = "DELETE FROM member"
cursor.execute(clear_table_query)
connect.commit()
# Verificar se a tabela foi limpa
if  cursor.rowcount == 0:
    print("Tabela 'member' limpa!")

reset_autoincrement_query = "ALTER TABLE member AUTO_INCREMENT = 1"
cursor.execute(reset_autoincrement_query)
connect.commit()"""


def presence():
    member_id = int(input("Informe seu número de membro (ou digite 0 para cadastrar novo): "))
    if member_id != 0:
        cursor.execute("SELECT * FROM member WHERE id = %s", member_id)
        result_member = cursor.fetchone()
        if result_member[0] == 0:
            print(f"O número de membro {member_id} não foi encontrado!")
            return member_id

presence()