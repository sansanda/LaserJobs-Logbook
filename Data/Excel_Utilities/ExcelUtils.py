import xlrd
from xlrd import open_workbook
from xlutils.copy import copy


def loadJobsFromExcel(laserJobsBook, sourceURL):
    workbook = xlrd.open_workbook(sourceURL, on_demand=True)
    worksheet = workbook.sheet_by_index(0)
    columns_row = []  # The row where we stock the name of the column

    for col in range(worksheet.ncols):
        columns_row.append(worksheet.cell_value(0, col))

    # tronsform the workbook to a list of dictionnary
    for row in range(1, worksheet.nrows):
        elm = {}
        for col in range(worksheet.ncols - 1):
            elm[columns_row[col + 1]] = str(worksheet.cell_value(row, col + 1))
        laserJobsBook.append(elm)

def updateExcel(updatedJobData, sourceURL):  #updatedJobData is a dictionary

    rb = open_workbook(sourceURL)
    r_sheet = rb.sheet_by_index(0)  # read only copy to introspect the file
    wb = copy(rb)  # a writable copy (I can't read values out of this, only write to it)
    w_sheet = wb.get_sheet(0)  # the sheet to write to within the writable copy

    jobIdToFind_RowIndex = getRowIndexByJobId(r_sheet, updatedJobData['jobId'])   #0 is the column index of the jobId
    columnNames = readColumnNames(r_sheet)
    for columnName_Index,columnName in enumerate(columnNames):
        w_sheet.write(jobIdToFind_RowIndex, columnName_Index, updatedJobData[columnName])
    wb.save(sourceURL)

#Auxiliar functions


def readColumnNames(sheet):
    columnNames = []
    for i in range(sheet.ncols):
        columnNames.append(sheet.cell_value(0, i))
    return columnNames

def getRowIndexByJobId(r_sheet, jobIdToFind):
    jobIdToFind_RowIndex = -1
    for row_index in range(1, r_sheet.nrows):         #start from 1. 0 is reserved for columns header
        colValue = r_sheet.cell(row_index, 0).value   #0 is the number of column of the jobId
        if int(colValue) == jobIdToFind:
            jobIdToFind_RowIndex = row_index
            break
    return jobIdToFind_RowIndex

