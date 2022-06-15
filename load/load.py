import psycopg2

try:
    conection = psycopg2.connect("dbname=postgres user=comodoro")
    print("Conectado a la base de datos")
except psycopg2.Error as e:
    print("Error al intentar conectarce a la base de datos:")
    print(e)


