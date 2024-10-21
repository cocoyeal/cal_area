from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from rect_calculator import rect_data, total_area #导入上一步的结果


def create_excel(rect_data, total_area, filename="rect_areas.xlsx"):
    """
    Creates an Excel file with rectangle data and total area.
    """
    workbook = Workbook()
    sheet = workbook.active

    # 写入表头
    sheet.append(["宽度", "高度", "面积"])

    # 写入长方形数据
    for rect in rect_data:
        sheet.append([rect["width"], rect["height"], rect["area"]])

    # 写入总面积
    sheet.append(["", "", "总面积"])
    sheet.append(["", "", total_area])

    # 自动调整列宽
    for col in sheet.columns:
        max_length = 0
        column = col[0].column_letter  # 获取列字母
        for cell in col:
            try:  # Necessary to avoid error on empty cells
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2  # Adjust as needed
        sheet.column_dimensions[column].width = adjusted_width

    workbook.save(filename)
    print(f"Excel文件已生成: {filename}")


create_excel(rect_data, total_area)
