import mysql.connector


con=mysql.connector.connect(
 host = '10.28.1.192',
database = 'ederson_trabalho',
user = 'SUPORTE',
password = 'Bambi123.')
        
registered_list = []
        
if con.is_connected():
    ederson_trabalho = con.get_server_info()
    print ("conecte ao banco = ", ederson_trabalho)


class MYSQL_Info():
    def __init__(self):
        
        pass

    
    def info_getter(self):
        consulta_sql = "select * from user_info"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        registered_list.append(linhas)
        return registered_list
        
        
    def delete_info(self, x):
        delete_sql = f"delete from user_info where ID = {x}"
        cursor = con.cursor()
        cursor.execute(delete_sql)
        con.commit
        
        
    def edit_info(self, x, y, z):
        update_sql = f"update user_info set {x} = {y} where ID = {z}"
        cursor = con.cursor()
        cursor.execute(update_sql)
        con.commit
        
        
    def register_info(self, name, age, cpf):
        insert_sql = f"insert into user_info(Nome, Age, CPF) values ('{name}', {age}, '{cpf}')"
        cursor = con.cursor()
        cursor.execute(insert_sql)
        con.commit
        