import urllib.request
import json
import csv
import time

loc = []
with open('location.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        loc.append(row['location'])

print(loc)

dis_list = []
f = open('distance.csv','w')
for i in range(12, 41):
    new = []
    row_s = ""
    for j in range(41):
        print(i, j, loc[i], loc[j])
        orig_coord = loc[i]
        dest_coord = loc[j]
        url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&&sensor=false".format(str(orig_coord),str(dest_coord))
        result = json.load(urllib.request.urlopen(url))
        # print(json.dumps(result, indent=4, sort_keys=True))
        dis = result['rows'][0]['elements'][0]['distance']['value']
        print(dis)
        row_s += str(dis) + ", "
        new.append(dis)
    f.write(row_s + '\n')
    time.sleep(5)
    dis_list.append(new)

print('\n'.join([''.join(['{:5}'.format(item) for item in row])
      for row in dis_list]))
