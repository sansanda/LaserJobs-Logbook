import openpyxl

def readRowValuesByOpenpyxl(worksheet, nRow, min_col, max_col):
    columnNames = []
    for row in worksheet.iter_cols(min_row=nRow, max_row=nRow, min_col=min_col, max_col=max_col):
        for cell in row:
            columnNames.append(cell.value)
    return columnNames

def _insertRowAtSheetByOpenpyxl(worksheet, rowToInsert_Index, jobData):

    columnNames = readRowValuesByOpenpyxl(worksheet, 1, 1, None)

    if rowToInsert_Index==-1:   #Then the row job is new. We will insert at the end of the sheet
        rowToInsert_Index = sheet.nrows
    for columnName_Index, columnName in enumerate(columnNames):
        writable_sheet.write(rowToInsert_Index, columnName_Index, jobData[columnName])


book = openpyxl.load_workbook('..\..\..\Data\laserJobs_inxls.xlsx')
worksheet = book.active

# for row in worksheet.iter_rows(min_row=1, min_col=1):
#     for cell in row:
#         print(cell.value, end="|")
#     print()

jobIdToFind = 10
jobIdToFind_RowIndex = -1

for rowIndex in range(1, worksheet.max_row): #row_count in excel starts with 1
    columnValues = readRowValuesByOpenpyxl(worksheet, rowIndex + 1, 1, None)  # read the other rows. Row index + 1 because we skip the header
    print(columnValues,rowIndex + 1)
    if jobIdToFind==int(columnValues[0]):
        jobIdToFind_RowIndex = rowIndex + 1
        break
print(jobIdToFind_RowIndex)


