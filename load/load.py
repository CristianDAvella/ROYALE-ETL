import psycopg2

conection = psycopg2.connect(database="royale", user="postgres", password="")
'''
try:
    
    print("Conectado a la base de datos")
except psycopg2.Error as e:
    print("Error:")
    print(e.pgerror)

'''