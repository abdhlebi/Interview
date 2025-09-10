import time
import os    #to call the operating system
import pandas as pd



data = {'Website': 'OrangeHRM', 'Information': info}
excel_file = 'output.xlsx'

def write_to_excel(data, excel_file):
    if not os.path.isfile(excel_file):
        # If the file doesn't exist, create a new one with headers
        df = pd.DataFrame([data])  # Wrap data in a list
        df.to_excel(excel_file, index=False)
    else:
        # If the file exists, load the existing data and append new data
        df_existing = pd.read_excel(excel_file)
        df_new = pd.DataFrame([data])  # Wrap data in a list
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_excel(excel_file, index=False)

write_to_excel()


#write_to_excel(data, excel_file)

