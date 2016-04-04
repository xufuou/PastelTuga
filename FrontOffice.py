import datetime
import time
import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

while (True):
    print"\nBASE DE DADOS PASTELTUGA\n*****Front Office*****\n1 -Inserir encomenda\n0 -Sair da aplicacao"
    f_opcao=input(">>")
    
    if (f_opcao==1):
        
        while (True):
            
            nome_cliente=raw_input("\nNome do cliente:")
            cur.execute("SELECT id_cliente,cidade,morada FROM clientes WHERE nome_cliente='"+nome_cliente.upper()+"'")      
            
            if cur.rowcount==0:
                print "\n>>O cliente,",nome_cliente,",nao existe na base de dados!"
                
            else:
                id_cliente,cidade,morada=cur.fetchone()   
                print"\n>>Cliente selecionado com sucesso!"  
                break
    
        
        quantidade=raw_input("\nPeso da encomenda (Kg):")        
        while (quantidade<=0) or (not(quantidade.isdigit())):
            print "\n>>O peso da encomenda deve ser um numero positivo!"
            quantidade=raw_input("\nPeso da encomenda (Kg):")             


        while(True):
            
            print"\nBASE DE DADOS PASTELTUGA\n*****Front Office*****\n1 -Consultar por distancia\n2 -Consultar por duracao\n3- Consultar por preco\n0- Sair"
            ordenar=input(">>")
            
            if ordenar==1 or ordenar==2 or ordenar==3:
                print str('').center(58,'-'),"\n|DISTRIBUIDORA||DISTANCIA[KM]||DURACAO[HORA]||PRECO[EURO]|\n",str('').center(58,'-')

            if ordenar==1:
                cur.execute("SELECT id_distribuidora, distancia,duracao,preco FROM capitais WHERE capital='" + cidade + "' order by distancia")  
                
            elif ordenar==2:
                cur.execute("SELECT id_distribuidora, distancia,duracao,preco FROM capitais WHERE capital='" + cidade + "' order by duracao")
                
            elif ordenar==3:
                
                cur.execute("SELECT id_distribuidora, distancia,duracao,preco FROM capitais WHERE capital='" + cidade + "' order by preco")


            for linha in cur.fetchall():
                
                id_distribuidora,distancia,duracao,preco=linha
        
                cur.execute("SELECT nome_distribuidora FROM distribuidoras WHERE id_distribuidora='"+str(id_distribuidora)+"'")
            
                for nome in cur.fetchall():
                    nome_distribuidora=nome
                    nome_distribuidora,=nome_distribuidora
                    print "|",nome_distribuidora.center(11,' '), "||",str(distancia).center(11,' '),"||",str(duracao).center(11,' '),"||",str(preco).center(9,' '),"|"

            if ordenar==0:
                break

        while (True):
            
            nome_distribuidora=raw_input("\nNome da distribuidora:") 
            cur.execute("SELECT id_distribuidora FROM distribuidoras WHERE nome_distribuidora='"+nome_distribuidora.upper()+"'")        
            id_distribuidora=cur.fetchone()
            
            if id_distribuidora==None:
                print "\n>>Empresa de distribuicao nao existe!"
            
            else:
                id_distribuidora,=id_distribuidora
                print"\n>>Empresa de distribuicao selecionado com sucesso!"  
                break
        while(True):

            print "\nConfirmar encomenda?\n1 - SIM\n2 - NAO"
            confirmar=input(">>")
            
            if confirmar==1:
                
                data= datetime.date.today()
                hora=time.strftime("%H:%M:%S")
                try:
                    cur.execute("INSERT INTO encomendas (id_distribuidora,id_cliente,data,hora,quantidade) VALUES('" + str(id_distribuidora) + "','" + str(id_cliente) + "','"+str(data)+ "','" + str(hora)+ "','" + str(quantidade) + "')")
                        
                    print("\n>>Nova encomenda registada!")
                                    
                except psycopg2.IntegrityError:
                    print ("\n>>Nao foi possivel criar a encomenda!")    
                conn.commit()                                         
                    
                cur.execute("SELECT id_fatura FROM encomendas WHERE id_distribuidora='"+ str (id_distribuidora)+"' AND id_cliente='"+ str (id_cliente)+"' AND data='"+ str(data) + "' AND hora='" + str(hora) + "'" ) 
                id_fatura=cur.fetchone()
                id_fatura,=id_fatura
                cur.execute("SELECT preco,duracao FROM capitais WHERE id_distribuidora='"+str(id_distribuidora)+"'")
                preco,duracao=cur.fetchone()
            
                print "\n",str('PASTELTUGA').center(40,'*'),"\n\nFATURA N:{0:<20}CLIENTE N:{1} \nDATA:{2:<21} HORA:{3} \n\nNOME:{4} \nMORADA:{5} \nCIDADE:{6} \n\nPRECO ENTREGA:{7:20}(EUROS)\nPRECO PASTEIS:{8:20}(EUROS)\nTOTAL:{9:28}(EUROS)".format(id_fatura,id_cliente,str(data),hora,nome_cliente.upper(),morada,cidade,preco,int(quantidade)*10,preco+int(quantidade)*10),"\n\n",str('DADOS DA ENTREGA').center(40,'-'),"\n",str('').center(40,'-'),"\n\nDistribuidora:",nome_distribuidora.upper(),"\nTempo estimado de entrega:",duracao,"(HORAS)\n\n",str('').center(40,'-'),"\n\n",str('***').center(40,' '),"\n\n", str('Obrigado pela preferencia!').center(40,' ')
                break
            
            elif confirmar==2:
                break
                
                
    elif f_opcao==0:
        print(">>Terminado!")
        break
cur.close()
conn.close()