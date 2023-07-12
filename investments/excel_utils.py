import openpyxl
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

from utils.settings import BASE_DIR


class ModifyExcelFile:

    @staticmethod
    def append_separator(filename: str,
                         cell: str,
                         text: str,
                         font_size: int = 12,
                         fill_color: str = None,
                         fill_pattern: str = None) -> None:
        """
        Записывает текст в указанную ячейку в файле Excel.

        :param filename: Путь к файлу
        :param cell: Ячейка, в которую будет записан текст. Напр. "A1"
        :param text: Текст, который будет записан в ячейку
        :param font_size: Размер шрифта. По умолчанию 12
        :param fill_color: Цвет фона ячейки в формате RGB. По умолчанию None
        :param fill_pattern: Тип заполнения фона ячейки: 'solid' или 'gray125'
        По умолчанию None
        :return: None
        """

        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        ws[cell] = text
        ws[cell].font = Font(size=font_size)
        if fill_color:
            fill = PatternFill(fill_type=fill_pattern, fgColor=fill_color)
            ws[cell].fill = fill
        wb.save(filename)

    @staticmethod
    def auto_fit_columns(filename: str) -> None:
        """
        Выравнивает ширину столбцов по содержимому столбца.

        :param filename: Путь к файлу
        выровнять ширину столбцов
        :return: None
        """

        WIDTH_INCREASE = 1.2
        ADJUST = 2

        wb = openpyxl.load_workbook(filename)

        worksheets = wb.sheetnames

        for sheet_name in worksheets:
            for column in wb[sheet_name].columns:
                max_length = 0
                col_letter = get_column_letter(column[0].column)
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(cell.value)
                    except TypeError:
                        pass
                adjusted_width = (max_length + ADJUST) * WIDTH_INCREASE
                wb[sheet_name].column_dimensions[col_letter].width = adjusted_width
        wb.save(filename)


if __name__ == '__main__':
    FILE_PATH = rf"{BASE_DIR}\investments\variant_7_data.xlsx"

    ModifyExcelFile.append_separator(
        FILE_PATH,
        "A50",
        "BlaBla"
    )

    ModifyExcelFile.auto_fit_columns(FILE_PATH)
