from array import array
from operator import is_not
import pandas as pd
import numpy as np

# Estado actual: crear una funcion que detecte si los datos de una columna son numericos y retornar la posicion. 
# Siguiente paso: cambiar el tipo de cada columna segun corresponda.
# Objetivo del dia: 

def is_number(colum:pd.Series):
    numbers = ['1','2','3','4','5','6','7','8','9','10','0']
    positions = []
    accountant = 0 

    for data in colum:
        if data not in numbers:
            positions.append(accountant)

        accountant = accountant+1

    return positions



if __name__ == '__main__':

    data =  pd.read_csv('../scrapy_royale/cards.csv')
    
    positions_notnumbers = is_number(data['cost'])
    simbol = data['cost'].get(positions_notnumbers[0])
    data['cost'] = data['cost'].replace({simbol:np.nan})

    data = data.astype({'cost':'int32'}, copy=True, errors='ignore')
    data.astype({'rarity':'category'})

    print(data.info())
    

# Bifurcacion
# Problema: el motor mysql no responde
# intentar: https://medium.com/el-acordeon-del-programador/iniciando-mysql-manualmente-en-windows-47a987aa6cff
