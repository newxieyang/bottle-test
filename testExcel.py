# encoding: utf-8
import xlrd


# table = data.sheets()[0]
# nrows = table.nrows
# ncols = table.ncols
# for i in range(nrows ):
#     print table.row_values(i)
# for i in range(ncols ):
#     print table.col_values(i)
# print table.col_values(4)

# cols = table.col_values(4)
# for item in cols:
#     print item



def calV(fileName):
    global mb
    global kb
    data = xlrd.open_workbook(fileName)
    for sheets in data.sheets():
        table = sheets
        cols = table.col_values(4)
        for item in cols:
            if("MB" in item):
                # print item.split("MB", 1)[0]
                mb += int(item.split("MB", 1)[0])
                kb += int(item.split("MB", 1)[0].split("KB", 1)[0])
                # print item.split("MB", 1)[0].split("KB", 1)[0]
                # print item
            else:
                if("KB" in item):
                    # print item.split("KB", 1)[0]
                    kb += int(item.split("KB", 1)[0])

mb = 0
kb = 0
calV('queryBill.xls')
calV('queryBill1.xls')
    # print mb + kb/1024
print  (mb + kb/1024)
    # print "kb;合计:" + (mb + kb/1024) + "MB"
