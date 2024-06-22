import os
import re
import openpyxl

file_name = "TAB362HV00-VDM001-AM.xlsx"
folder_path = "/home/amrserver/Documents/KDCV-m104/xlsx"

# sheet = pd.read_excel(folder_path+file_name, engine="pyxlsb", sheet_name="NVTT 1", usecols='A:J' , header=None)

class StructForm:
    def __init__(self) -> None:
        self.operationName = "A1"
        self.year = [1,1]
        self.speciesName = [1,3]
        self.month = [2,1]
        self.shiftStage = [2,3]
        self.deviceName = "A5"
        self.no = [4,2]
        self.category = [3,2]
        self.method = [3,3]
        self.position = [3,4]
        self.confirm = [3,5]
        self.type = [3,6]

# def find_all_xlsb_in_folder(folder_path):
#     listFile = []
#     for filename in os.listdir(folder_path):
#         # Kiểm tra xem file có phần mở rộng .xlsb hay không
#         if filename.endswith(('.xlsb','.XLSB')):
#             # Tạo đường dẫn đầy đủ tới file .xlsb
#             xlsb_file = os.path.join(folder_path, filename)
#             listFile.append(xlsb_file)
#     return listFile

# allFileXLSB = find_all_xlsb_in_folder(folder_path)

# Verify if files are supported
def is_excel_file(files):
    supported_files = ['.xls', '.xlsx', '.xlsb', '.XLSB']

    for file in files:
        file_type = os.path.splitext(file)[1]
        if file_type not in supported_files:
            return False
    
    return True


structForm = StructForm()
column_index = 2
sheetNameNhanvien = []
workbook = openpyxl.load_workbook(os.path.join(folder_path, file_name))
sheetNames = workbook.sheetnames
for name in sheetNames:
    if name.startswith('N'):
        print(f"Sheet name: {name} -----------------/")
        sheet = workbook[name]
        # Lấy tất cả giá trị trong cột và vị trí của chúng
        non_nan_values = []
        # column_values = [cell.value for cell in sheet['H']]
        # print(f"Phân khu column({len(column_values)}): {column_values}")

        # for row in range(5, sheet.max_row + 1):
        #     cell_value = sheet.cell(row=row, column=column_index).value
        #     if (cell_value is not None and
        #         isinstance(cell_value, int)):
        #         print("///////////////////////////////////////////////")
        #         print(f"Hạng mục điểm kiểm {cell_value}: {sheet.cell(row=row, column=3).value}")
        #         print(f"  Phương pháp điểm kiểm: {sheet.cell(row=row, column=4).value}")
        #         print(f"  Phương pháp xác nhận & bản TMKT: {sheet.cell(row=row, column=6).value}")
        merged_cells = sheet.merged_cells.ranges
        merged_cells_filter = {}
        for merged_cell in merged_cells:
            addr = merged_cell.coord
            match = re.match(r"([A-Za-z]+)\d+:[A-Za-z]+\d+", addr).group(1)
            if match not in merged_cells_filter:
                merged_cells_filter[match] = [merged_cell.coord]
            else:
                merged_cells_filter[match].append(merged_cell.coord)
        # print(merged_cells_filter)

        for row in range(5, sheet.max_row + 1):
            cell_value = sheet.cell(row=row, column=column_index).value
            if (cell_value is not None):
                non_nan_values.append((cell_value, row))

        for value, row in non_nan_values:
            if isinstance(value, int):
                print(f"Vị trí: Hàng {row}, Cột {column_index} - Giá trị: {value}")
                category_merged = merged_cells_filter["C"]
                for cell in category_merged:
                    start = int(cell.split(':')[0][1:])
                    end = int(cell.split(':')[1][1:])
                    if start == row:
                        print("   START: ",start)
                        print("   END: ",end)

# Đóng workbook
workbook.close()