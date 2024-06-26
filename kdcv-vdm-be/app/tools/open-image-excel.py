from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader

# Đường dẫn đến file Excel của bạn
file_path = '/home/amrserver/Documents/KDCV-m104/xlsx/T24Y003V00-VDM001-AB.xlsx'

# Mở workbook
wb = load_workbook(filename=file_path)

# Chọn sheet bạn muốn đọc
ws = wb['KTV (2)']  # Thay 'Sheet1' bằng tên sheet của bạn

# Tạo một SheetImageLoader
image_loader = SheetImageLoader(ws)

# Lấy danh sách các vùng ô hợp nhất
merged_cells = ws.merged_cells.ranges

# Hàm để kiểm tra xem một ô có nằm trong vùng ô hợp nhất hay không
def get_merged_cell_range(cell):
    for merged_range in merged_cells:
        if cell.coordinate in merged_range:
            return merged_range
    return None

# Danh sách các ô có chứa hình ảnh
image_cells = list(image_loader._images.keys())

# Duyệt qua các ô có chứa hình ảnh và lưu chúng
for cell in image_cells:
    merged_range = get_merged_cell_range(ws[cell])
    if merged_range:
        print(merged_range.coord)
        cell_address = merged_range.coord.split(':')[0]
    else:
        cell_address = cell
    image = image_loader.get(cell)
    image_path = f'image_from_{cell_address}_{image_cells.index(cell)}.png'
    # image.save(image_path)
    print(f'Hình ảnh từ ô {cell_address} đã được lưu tại {image_path}')

# Đóng workbook
wb.close()