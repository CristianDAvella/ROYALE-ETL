import pandas as pd

# Estado actual: arroja el error -> ValueError: invalid literal for int() with base 10: '? '
# Siguiente paso: probar transformando la columna names. 
# Objetivo del dia: 

data =  pd.read_csv('../scrapy_royale/cards.csv')

data_transformed = data['cost'].astype('int64', copy=True, errors='raise')


print(data_transformed.info())