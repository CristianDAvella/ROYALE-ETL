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

        comands.execute(sql_insert,data)
        conection.commit()

        comands.execute("Delete from card where costo = -1;")
        conection.commit()

        comands.close()
        conection.close()
        print("Datos insertados en postgres")
    
    except psycopg2.Error as e:
        print("Error al insertar los datos:")
        print(e)

if __name__ == '__main__':
    pass