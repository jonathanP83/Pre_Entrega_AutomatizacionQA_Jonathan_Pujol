import csv
import json

#creo funcion que abre el archivo csv, lo lea, y convierte todo en una lista
def read_user_csv():
    with open("data/users.csv",newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

#lector del json
def read_products_json():
    with open("data/products.json") as file:
        return json.load(file)
    