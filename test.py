from dbutlis2 import update
import xlrd

wd = xlrd.open_workbook(filename=r"C:\Users\微软微软\Desktop\python学习新\day7\任务\2020年每个月的销售情况.xlsx", encoding_override=True)
wd_len = len(wd.sheets())
for i in range(wd_len):
    st = wd.sheet_by_index(i)
    rows = st.nrows
    for j in range(1, rows):
        data = st.row_values(j)
        print(data[0], data[1], data[2], data[3], data[4])
        sql = "insert into month_%s value(%s,%s,%s,%s,%s)"
        param = [i+1, data[0], data[1], data[2], data[3], data[4]]
        update(sql, param)

# st = wd.sheet_by_index(0)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0],data[1],data[2],data[3],data[4])
#     sql= "insert into month_1 value(%s,%s,%s,%s,%s)"
#     param = [data[0],data[1],data[2],data[3],data[4]]
#     update(sql, param)
# st = wd.sheet_by_index(1)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0],data[1],data[2],data[3],data[4])
#     sql= "insert into month_2 value(%s,%s,%s,%s,%s)"
#     param = [data[0],data[1],data[2],data[3],data[4]]
#     update(sql, param)
#
# st = wd.sheet_by_index(2)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0], data[1], data[2], data[3], data[4])
#     sql = "insert into month_3 value(%s,%s,%s,%s,%s)"
#     param = [data[0], data[1], data[2], data[3], data[4]]
#     update(sql, param)
#
# st = wd.sheet_by_index(3)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0], data[1], data[2], data[3], data[4])
#     sql = "insert into month_4 value(%s,%s,%s,%s,%s)"
#     param = [data[0], data[1], data[2], data[3], data[4]]
#     update(sql, param)
#
# st = wd.sheet_by_index(4)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0], data[1], data[2], data[3], data[4])
#     sql = "insert into month_5 value(%s,%s,%s,%s,%s)"
#     param = [data[0], data[1], data[2], data[3], data[4]]
#     update(sql, param)
#
# st = wd.sheet_by_index(5)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0], data[1], data[2], data[3], data[4])
#     sql = "insert into month_6 value(%s,%s,%s,%s,%s)"
#     param = [data[0], data[1], data[2], data[3], data[4]]
#     update(sql, param)
#
# st = wd.sheet_by_index(6)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0], data[1], data[2], data[3], data[4])
#     sql = "insert into month_7 value(%s,%s,%s,%s,%s)"
#     param = [data[0], data[1], data[2], data[3], data[4]]
#     update(sql, param)
#
# st = wd.sheet_by_index(7)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0], data[1], data[2], data[3], data[4])
#     sql = "insert into month_8 value(%s,%s,%s,%s,%s)"
#     param = [data[0], data[1], data[2], data[3], data[4]]
#     update(sql, param)
#
# st = wd.sheet_by_index(8)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0], data[1], data[2], data[3], data[4])
#     sql = "insert into month_9 value(%s,%s,%s,%s,%s)"
#     param = [data[0], data[1], data[2], data[3], data[4]]
#     update(sql, param)
#
# st = wd.sheet_by_index(9)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0], data[1], data[2], data[3], data[4])
#     sql = "insert into month_10 value(%s,%s,%s,%s,%s)"
#     param = [data[0], data[1], data[2], data[3], data[4]]
#     update(sql, param)
#
# st = wd.sheet_by_index(10)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0], data[1], data[2], data[3], data[4])
#     sql = "insert into month_11 value(%s,%s,%s,%s,%s)"
#     param = [data[0], data[1], data[2], data[3], data[4]]
#     update(sql, param)
#
# st = wd.sheet_by_index(11)
# rows = st.nrows
# cols = st.ncols
# for j in range(1, rows):
#     data = st.row_values(j)
#     print(data[0], data[1], data[2], data[3], data[4])
#     sql = "insert into month_12 value(%s,%s,%s,%s,%s)"
#     param = [data[0], data[1], data[2], data[3], data[4]]
#     update(sql, param)
