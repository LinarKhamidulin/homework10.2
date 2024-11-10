import csv

import pandas as pd

def reading_a_file_csv(parameters: list)-> list:
    '''функция для открытия и обратки csv файла'''
    datas_ = []
    file_csv = "data/transactions.csv"
    with open(file_csv, encoding="utf-8") as file:
        readers = csv.DictReader(file, delimiter=';')
        for reader in readers:
            if reader != {}:
                if parameters["currency"].lower() == "да":
                    if reader["state"] == parameters["status"].upper() and reader["currency_code"] == "RUB":
                            datas_.append(reader)
                elif parameters["currency"].lower() == "нет":
                    if reader["state"] == parameters["status"].upper():
                        datas_.append(reader)
        if parameters["data"] == "да" and parameters["ascending_or_descending"] == "по возрастанию":
            datas_.sort(key=lambda i: i["date"])
        elif parameters["data"] == "нет" and parameters["ascending_or_descending"] == "по возрастанию":
            datas_.sort(key=lambda i: i['id'])
        elif parameters["data"] == "да" and parameters["ascending_or_descending"] == "по убыванию":
            datas_.sort(key=lambda i: i["date"], reverse=True)
        elif parameters["data"] == "нет" and parameters["ascending_or_descending"] == "по убыванию":
            datas_.sort(key=lambda i: i['id'], reverse=True)

    return datas_


def read_excel_file(parameters: list)-> list:
    '''функция для открытия и обратки excel файла'''

    file_excel = "data/transactions_excel.xlsx"
    excel_data = pd.read_excel(file_excel)
    if parameters["currency"].lower() == "да":
        df = excel_data .loc[(excel_data.state == parameters["status"]) & (excel_data.currency_code == "RUB")]
    else:
        df = excel_data.loc[(excel_data.state == parameters["status"])]
    dict_list = df.to_dict(orient='records')
    if parameters["data"] == "да" and parameters["ascending_or_descending"] == "по возрастанию":
        dict_list.sort(key=lambda i: i["date"])
    elif parameters["data"] == "нет" and parameters["ascending_or_descending"] == "по возрастанию":
        dict_list.sort(key=lambda i: i['id'])
    elif parameters["data"] == "да" and parameters["ascending_or_descending"] == "по убыванию":
        dict_list.sort(key=lambda i: i["date"], reverse=True)
    elif parameters["data"] == "нет" and parameters["ascending_or_descending"] == "по убыванию":
        dict_list.sort(key=lambda i: i['id'], reverse=True)

    return dict_list
