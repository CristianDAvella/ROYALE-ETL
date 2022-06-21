from operator import is_not
import pandas as pd

# help to fution 'normalize_costs'
def simbols_invalid(colum:pd.Series):
    numbers = ['1','2','3','4','5','6','7','8','9','10','0']
    simbols = []

    for data in colum:
        if (data not in numbers) and (data not in simbols):
            simbols.append(data)

    return simbols


def normalize_costs(data_frame:pd.DataFrame):

    list_simbols_invalid = simbols_invalid(data_frame['cost'])
    data_frame['cost'] = data_frame['cost'].replace(to_replace=list_simbols_invalid, value="-1")
    
    return data_frame


def get_info():
    data = pd.read_csv("/mnt/f/proyectos/mi_primer_etl/scrapy_royale/cards.csv")
    data = normalize_costs(data)

    names = data["names"]
    costs = data["cost"]
    descriptions = data["description"]
    raritys = data["rarity"]

    return [names, costs, descriptions, raritys]


