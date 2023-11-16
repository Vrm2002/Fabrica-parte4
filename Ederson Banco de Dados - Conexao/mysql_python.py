from os import system as ss
import mysql.connector

con=mysql.connector.connect(
    host = '10.28.1.192',
    database = 'Cadastro',
    user = 'SUPORTE',
    password = 'Bambi123.')

if con.is_connected():
    usuario = con.get_server_info()
    print ("conecte ao banco = ", usuario)


while True:
    
    try:
        opt = int(input("ESCOLHA UMA DAS SEGUINTES OPÇÕES:\n1. Cadastrar\n2. Sair\nEscolha: "))
        
    except:
        ss('cls')
        print('Escolha Inexistente')
        ss('pause')
        ss('cls')
        
    else:
        ss('cls')
        if opt == 1:
            
            try:
                nome = input('Nome:')
                idade = input('Idade: ')
                sexo = input('Sexo: ')
                email = input('Email: ')
                pais = input('País: ')
                estado = input('Estado: ')
                cidade = input('Cidade: ')
                estadocivil = input('Estado Civil: ')
                rg = input('RG: ')
                
            except:
                ss('cls')
                print('Erro nas informações')
                ss('pause')
                ss('cls')
                
            else:
                ss('cls')
                print('Cadastrado com sucesso')
                insert_sql = f"insert into usuario(nome, idade, sexo, email, pais, estado, cidade, estadoCivil, rg) values ('{nome}', {idade}, '{sexo}', '{email}', '{pais}', '{estado}', '{cidade}', '{estadocivil}', '{rg}');"
                print(insert_sql)
                cursor = con.cursor()
                cursor.execute(insert_sql)
                con.commit()
                
                select_sql = 'select * from usuario'
                cursor.execute(select_sql)
                linhas = cursor.fetchall()
                print(linhas)
                
            
        
        elif opt == 2:
            print('Encerrando')
            break
        
    