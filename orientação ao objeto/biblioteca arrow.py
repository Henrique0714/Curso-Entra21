import arrow

# data = arrow.now().format('DD/MM/YYYY')
# print(data)
#
# dat = arrow.now().format('HH:mm')
# print(data)
#
# data = arrow.get(25)
# print(data)

date_1 = arrow.get('2005-01-02 18:09:48','YYYY-MM-DD HH:mm:ss')
date_2 = arrow.get('2022-07-14 13:16:20','YYYY-MM-DD HH:mm:ss')
diff = date_2 - date_1
print(diff)
