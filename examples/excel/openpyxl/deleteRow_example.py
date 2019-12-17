import openpyxl

try:
    book = openpyxl.load_workbook('laserJobs_inxls.xlsx')
    worksheet = book['LaserJobs']

    for row in worksheet.iter_rows(min_row=1, min_col=1):
        for cell in row:
            print(cell.value, end="|")
        print()

    worksheet.delete_rows(5,1)
    book.save('laserJobs_inxls.xlsx')


except Exception as e:
    print(e)

