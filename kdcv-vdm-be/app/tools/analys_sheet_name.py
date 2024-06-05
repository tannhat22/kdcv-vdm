import pandas as pd
import os

file_name = "/home/tannhat/Documents/KDCV/T19Y001V00-VDM001-AE.xlsb"
folder_path = "/home/tannhat/Documents/KDCV"

# sheet = pd.read_excel(file_name, engine="pyxlsb", sheet_name="NV")

def find_all_xlsb_in_folder(folder_path):
    listFile = []
    for filename in os.listdir(folder_path):
        # Kiểm tra xem file có phần mở rộng .xlsb hay không
        if filename.endswith(('.xlsb','XLSB')):
            # Tạo đường dẫn đầy đủ tới file .xlsb
            xlsb_file = os.path.join(folder_path, filename)
            listFile.append(xlsb_file)
    return listFile

allFileXLSB = find_all_xlsb_in_folder(folder_path)

i = 1
sheetNameNhanvien = []
for file in allFileXLSB:
    print("name file: ", file)
    sheetNames = pd.ExcelFile(file, engine="pyxlsb").sheet_names
    flag = False
    for name in sheetNames:
        if name.startswith('N'):
            if not flag:
                i += 1
                flag = True
            if name not in sheetNameNhanvien:
                sheetNameNhanvien.append(name)
            
print("Tổng số file có sheetname bắt đầu bằng N: ", i)
print("Tổng hợp tên sheet giành cho Nhân viên: ", sheetNameNhanvien)


