#!/usr/bin/python3.6
from easysnmp import Session
import re
import pprint

class HardwareIDreader(object):
    def __init__(self):
        self.siteMap={}

    def readInput(self,inputfile):
        with open(inputfile) as ifile:
            itemList=[]
            site=""
            self.siteMap={}
            for line in ifile:
#               print(line)
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
                        self.siteMap[siteName]=itemList
                        itemList=[]

    def printMap(self):
        pprint.pprint(self.siteMap)

    def getSNSW(self):
        print("Site,TX Name,IP Address,Serial Number,SW/FW/Bios")
        for site, devices in self.siteMap.items():
            for device in devices:
                #print(site+","+device[0]+","+device[1])
                #get the snmp values
                IP=(device[1])[7:]
                #print(IP)
                try:
                    session = Session(hostname=IP, community='BANMSRO', version=2)
                    SN = session.get('.1.3.6.1.2.1.47.1.1.1.1.11.1')
                    SW = session.get('.1.3.6.1.2.1.47.1.1.1.1.9.1')
                    print(site+","+device[0]+","+device[1]+","+SN.value+","+SW.value)
                except Exception as e:
                    try:
                        session2 = Session(hostname=IP, community='public', version=2)
                        SN2 = session2.get('.1.3.6.1.2.1.47.1.1.1.1.11.1')
                        SW2 = session2.get('.1.3.6.1.2.1.47.1.1.1.1.9.1')
                        print(site+","+device[0]+","+device[1]+","+SN2.value+","+SW2.value)
                    except Exception as e:
                        print(site+","+device[0]+","+device[1]+","+str(e)+","+str(e))

if __name__ == "__main__":
    myreader=HardwareIDreader()
    myreader.readInput("THVU9.txt")
#myreader.printMap()
    myreader.getSNSW()
