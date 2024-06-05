import pandas as pd
import os

file_name = "T19Y001V00-VDM001-AE.xlsb"
folder_path = "/home/tannhat/Documents/KDCV"

formStruct = {
    'operationName': [0,0],
    'year': [1,1],
    'speciesName': [1,3],
    'month': [2,1],
    'shift': [2,3],
    'deviceName': [3,0],
    'no': [3,1],
    'category': [3,2],
    'method': [3,3],
    'position': [3,4],
    'confirm': [3,5]
}

full_dir_name = os.path.join(folder_path, file_name)

sheetNames = pd.ExcelFile(full_dir_name, engine="pyxlsb").sheet_names
col = formStruct["no"][1]
for name in sheetNames:
    if name.startswith('N'):
        sheet = pd.read_excel(full_dir_name, engine="pyxlsb", sheet_name=name, usecols="A:J", header=None)
        print(sheet.at[formStruct["operationName"][0], formStruct["operationName"][1]])
        notNanValue = sheet[col].dropna().index
        for i in notNanValue:
            if i > formStruct["no"][0]:
                print("///////////////////////////////////////////////")
                print(f"Hạng mục điểm kiểm {sheet.at[i,col]}: {sheet.at[i,col+1]}")
                print(f"  Phương pháp điểm kiểm: {sheet.at[i,col+2]}")
                # print(f"  Vị trí điểm kiểm: {sheet.at[i,col+3]}")
                print(f"  Phương pháp xác nhận & bản TMKT: {sheet.at[i,col+5]}")
