import xlrd

workbook = xlrd.open_workbook('..\..\Data\laserJobs.xlsx', on_demand = True)
worksheet = workbook.sheet_by_index(0)
first_row = [] # The row where we stock the name of the column

for col in range(worksheet.ncols):
    first_row.append( worksheet.cell_value(0,col) )

# tronsform the workbook to a list of dictionnary
data =[]
for row in range(1, worksheet.nrows):
    elm = {}
    for col in range(worksheet.ncols):
        elm[first_row[col]]=str(worksheet.cell_value(row,col))
        print(elm)
    data.append(elm)

print(data)