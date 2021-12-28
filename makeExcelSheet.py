from openpyxl import Workbook


def makeExcelSheet(rawData, file_name):
    print(rawData)
    wb = Workbook()
    ws = wb.active

    for i in rawData:
        ws.append(i)
    wb.save("extractedFile/" + str(file_name).strip()+".xlsx")
