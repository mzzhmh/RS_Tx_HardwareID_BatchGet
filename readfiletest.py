#!/usr/bin/python3.6
import re
import pprint

with open("THVU9.txt") as ifile:
    itemList=[]
    site=""
    siteMap={}
    for line in ifile:
#        print(line)
        r1 = re.search(r'TD.*TH(V|U)',line)
        if r1 != None:
            deviceName=line.split("><")[2].split(">")[1].split("<")[0]
            #print(deviceName)
            deviceIP=line.split("><")[5].split(">")[1].split("<")[0]
            #print(deviceIP)
            tmpList=[deviceName,deviceIP]
            itemList.append(tmpList)
        r2 = re.search(r'<Type dt:dt="ui4">1<\/Type>',line)
        if r2 != None:
            siteName=line.split("><")[2].split(">")[1].split("<")[0]
            if(len(itemList)>0):
                siteMap[siteName]=itemList
                itemList=[]
pprint.pprint(siteMap)

        


