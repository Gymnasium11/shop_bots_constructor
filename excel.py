import pandas as pd
import database

def read_excel(excel_data_df, id_shop):
    # excel_data_df = excel_data_df.replace(pd.NA, 'null')
    for i in range(len(excel_data_df)):
        line = list(excel_data_df.iloc[i])
        print(line, line[1].strip())
        database.insert(f"INSERT INTO product (id_shop, article, name, price, category, short_description, description, url_picture, color )  VALUES  ('{id_shop}', '{line[0]}', '{line[1]}', '{line[2]}', '{line[3]}','{line[4]}','{line[5]}','{line[6]}', '{line[7]}')")


