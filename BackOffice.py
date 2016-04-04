import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

while (True):

    print"\nBASE DE DADOS PASTELTUGA\n*****Back Office******\n1 - Registar cliente\n2 - Registar distribuidor\n0 - Sair da aplicacao"
        
    b_opcao=input(">>")
        
    if b_opcao==1:
        
        nome_cliente=raw_input("Nome:")
        cur.execute("SELECT * FROM clientes WHERE nome_cliente='" + nome_cliente.upper() + "'")
        
        if cur.rowcount==0:
            
            morada=raw_input("Morada:")
            cidade=raw_input("Cidade:")
            telefone=raw_input("Telefone:")
            
            cur.execute("INSERT INTO clientes (nome_cliente,morada,telefone,cidade) VALUES ('" + nome_cliente.upper() + "','" +  morada.upper() + "','" + telefone + "','" + cidade.upper() + "')")
            print("\n>>Novo cliente registado!")
                        
        else:
            print ("\n>>Cliente ja existe na base de dados!")        
        
        conn.commit()

    elif b_opcao==2:
        
        nome_distribuidora=raw_input("Nome:")
        cur.execute("SELECT * FROM distribuidoras WHERE nome_distribuidora='" + nome_distribuidora.upper() + "'")
        
        if cur.rowcount==0:
            
            cur.execute("INSERT INTO distribuidoras(nome_distribuidora) VALUES('" + nome_distribuidora.upper() + "')")
            print ("\nNova distribuidora registado!") 
        
        else:
            print ("\nDistribuidora ja existe na base de dados!")
            conn.commit()
        
        cur.execute("SELECT id_distribuidora from distribuidoras WHERE nome_distribuidora='"+nome_distribuidora.upper()+"'")
        id_distribuidora=cur.fetchone()
        id_distribuidora,=id_distribuidora
        
        while(True):
            
            capital=raw_input("\nCidade:")
            distancia=raw_input("Distancia[KM]:")
            duracao=raw_input("Duracao[HORAS]:")
            preco=raw_input("Preco[EUROS]:")
            
            cur.execute("INSERT INTO capitais (id_distribuidora,capital,distancia,duracao,preco) VALUES('"+str(id_distribuidora)+"','" + capital.upper() + "','" + distancia + "','" + duracao + "','" + preco + "')")
            conn.commit()
            
            print ("\n>>Informacao actualizada!")
            print("\n1-Introduzir cidade\n0-Sair")
            mais=input(">>")
            
            if mais==0:
                break
    
    elif b_opcao==0:
        print(">>Terminado")
        cur.close()
        conn.close()        
        break

