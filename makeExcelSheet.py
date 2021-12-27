from openpyxl import Workbook


def makeExcelSheet(rawData):
    wb = Workbook()
    ws = wb.active

    for i in rawData:
        ws.append(i)
    wb.save("extractedFile/justfortesting.xlsx")
