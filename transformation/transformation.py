from operator import is_not
import pandas as pd

# Estado actual: arroja el error -> ValueError: invalid literal for int() with base 10: '? '
# Siguiente paso: probar transformando la columna names. 
# Objetivo del dia: crear una funcion que detecte si los datos de una columna son numericos.

def is_number(colum:pd.Series):
    positions = []
    numbers = ['1','2','3','4','5','6','7','8','9','10','0']

    for data in  colum:
        if not(data in numbers):
            positions = colum.isin([data])

    return positions


if __name__ == '__main__':

    data =  pd.read_csv('../scrapy_royale/cards.csv')

#    data_transformed = data.astype({'rarity':'category'})

 #   print(data_transformed.info())

    print(is_number(data['cost']))

# Bifurcacion
# Problema: el motor mysql no responde
# intentar: https://medium.com/el-acordeon-del-programador/iniciando-mysql-manualmente-en-windows-47a987aa6cff
