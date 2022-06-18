import psycopg2
import pandas as pd

def conect():
    try:
        conection = psycopg2.connect("dbname=royale")
        print("Conectado a la base de datos")
    except psycopg2.Error as e:
        print("Error al intentar conectarce a la base de datos:")
        print(e)

    return conection

def get_info():
    data = pd.read_csv("/mnt/f/proyectos/mi_primer_etl/scrapy_royale/cards.csv")
    
    names = data["names"][0]
    costs = data["cost"][0]
    descriptions = data["description"][0]
    raritys = data["rarity"][0]

    return [names, costs, descriptions, raritys]

def push_in_database():
    conection = conect()
    comands = conection.cursor()

    sql_insert = "Insert into card(nombre, costo, descripcion, calidad)\
                            values(%s, %s, %s, %s)"
    data = get_info()

    comands.execute(sql_insert,data)
    comands.close()

if __name__ == '__main__':
    push_in_database()