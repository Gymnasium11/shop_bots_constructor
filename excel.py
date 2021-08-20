import pandas as pd
import database

def read_excel(path):
    excel_data_df = pd.read_excel(path)
    # excel_data_df = excel_data_df.replace(pd.NA, 'null')
    for i in range(len(excel_data_df)):
        line = list(excel_data_df.iloc[i])
        print(line, line[1].strip())
        id_shop = int(path.split('/')[-2])
        database.insert(f"INSERT INTO product (id_shop, article, name, price, category, short_description, description, url_picture, color )  VALUES  ('{id_shop}', '{line[0]}', '{line[1]}', '{line[2]}', '{line[3]}','{line[4]}','{line[5]}','{line[6]}', '{line[7]}')")


read_excel('./files/1/catalog2.xlsx')

# price, category, short_description, description, url_picture
# , {line[2]}, {line[3]},{line[4]},{line[5]},{line[6]}