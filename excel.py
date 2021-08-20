import pandas as pd

excel_data_df = pd.read_excel('./files/1/catalog2.xlsx', sheet_name='Sheet1')

# print whole sheet data
# print(excel_data_df)

# print(excel_data_df.columns.ravel())
for i in range(len(excel_data_df)):
    print(list(excel_data_df.iloc[i]))