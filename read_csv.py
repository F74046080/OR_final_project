import csv

dis_list = []
with open('distance_all.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        dis_list.append(row)
for i in dis_list:
    i.pop() # pop the last empty element
print(dis_list)
