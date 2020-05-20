import csv
import os
def fixbandrange(filepaht,delimiter=' ',lim=10):
    with open(filepaht) as debandcsv:
        csvzones = csv.reader(debandcsv, delimiter=delimiter)
        zones=[]
        for row in csvzones:
            zones.append(row)
    newzoens=[]
    newzoens.append(zones[0])
    for i in zones[1:]:
        if int(i[0])-int(newzoens[-1][1])< lim:
            newzoens[-1][1]=i[1]
        else:
            newzoens.append(i)
    path,_=os.path.split(filepaht)
    with open(os.path.join(path,'out.csv'),'w') as debandcsv:
        spamwriter = csv.writer(debandcsv, delimiter=delimiter)
        for i in newzoens:
            spamwriter.writerow(i)




if __name__ == '__main__':
    fixbandrange(r'/Users/hujingyu/Encode/upinthe/用所选项目新建的文件夹 2/merged-banding-frames.csv')