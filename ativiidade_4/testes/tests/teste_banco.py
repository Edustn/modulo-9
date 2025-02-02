import psycopg2

connection = psycopg2.connect(database = "metabaseappdb", 
                        user = "metabase", 
                        host= 'localhost',
                        password = "mysecretpassword",
                        port = 5432)

conn = connection.cursor()


def inserir_mensagem(mensagem):
    conn.execute("INSERT INTO informacoes (mensagem) VALUES (%s);", (mensagem,))

    connection.commit()
    conn.close()
    connection.close()

