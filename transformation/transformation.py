from operator import is_not
import pandas as pd

# Estado actual: imprime una lista de booleanos afirmando si existe en esa posicion uno de los primeros 11 numeros naturales incluyendo el 0.
# Siguiente paso: crear una funcion que detecte si los datos de una columna son numericos y retornar la posicion. 
# Objetivo del dia: 

def is_number(colum:pd.Series):
    numbers = ['1','2','3','4','5','6','7','8','9','10','0']
    positions = colum.isin(numbers)

    return positions


if __name__ == '__main__':

    data =  pd.read_csv('../scrapy_royale/cards.csv')

#    data_transformed = data.astype({'rarity':'category'})

 #   print(data_transformed.info())

    print(is_number(data['cost']))

# Bifurcacion
# Problema: el motor mysql no responde
# intentar: https://medium.com/el-acordeon-del-programador/iniciando-mysql-manualmente-en-windows-47a987aa6cff
