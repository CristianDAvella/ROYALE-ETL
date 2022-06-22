import psycopg2
from transformation.transformation import get_info

def conect():
    try:
        conection = psycopg2.connect("dbname=royale")
        print("Conectado a la base de datos")
    except psycopg2.Error as e:
        print("Error al intentar conectarce a la base de datos:")
        print(e)

    return conection


def push_in_database():
    try:
        conection = conect()
        comands = conection.cursor()

        sql_insert = "Insert into card(nombre, costo, descripcion, calidad)\
                                values(%s, %s, %s, %s)"
        data = get_info()

        total_inserts = len(data[0])
        insert_number = 0
        while insert_number < total_inserts:
            comands.execute(sql_insert, (data[0][insert_number], data[1][insert_number], data[2][insert_number], data[3][insert_number]))
            conection.commit()
            insert_number += 1

        comands.close()
        conection.close()
        print("Datos insertados en postgres")
    
    except psycopg2.Error as e:
        print("Error al insertar los datos:")
        print(e)

if __name__ == '__main__':
    push_in_database()
    