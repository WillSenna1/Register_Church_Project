import mysql.connector

#Criando funções


def presence():
    member_id = int(input("Informe seu número de membro (ou digite 0 para cadastrar novo): "))
    if member_id != 0:
        query = "SELECT COUNT(*) FROM members WHERE id = %s"
        cursor.execute(query, (member_id,))
        result_member = cursor.fetchone()
        if result_member[0] == 0:
            print(f"O número de membro {member_id} não foi encontrado!")
            return member_id
        else:
            pass


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


    def status():        
        status = input("Confirme presença ou falta (Use apenas P ou F respectivamente: ")
        status_option = ["P", "F"]
        if status.upper() not in status_option:
            print("Opção inválida! Use apenas P ou F.")
            return status
        else:
            return


# Conectar ao banco de dados
connect = mysql.connector.connect(
    host="localhost",
    user="WilliamF",
    password="03092002",
    database="myapp"
)

#Verificar  se a conexão foi realizada com sucesso
if  connect.is_connected():
    print("Conectado")

#  Criar um cursor para executar as querys SQL
cursor = connect.cursor()

# Captura de dados cliente

    
def cap_data():    
    name = input("Digite o nome: ")
    email = input("Digite o email: ")
    birth  = int(input("Digite a idade: "))
    adress =  input("Digite o endereço: ")
    phone = int(input("Digite o telefone: "))
    baptism =  str(input("Foi batizado? [S/N]")).upper()
    tupla = ["S", "N"]
    if baptism not in tupla:
        print("Opção Inválida! Utilize S ou N.")
        return name
    else:
        return

# Inserir dados

    insert_data = """
        INSERT INTO members (name, email, birth, adress, 
        phone, baptsm)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    data = (name, email, birth, adress, phone, baptsm)
    cursor.execute(insert_data, data)
    print("\nDados inseridos com sucesso!\n")

connect.commit()

#Consulta de dados
Consulta = "SELECT * FROM members"
cursor.execute(Consulta)

for linha in cursor.fetchall():
    print(linha)

#Fechar conexão
cursor.close()
connect.close()