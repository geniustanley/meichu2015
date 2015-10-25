# coding=utf-8
import json, csv
import urllib2
import datetime
from random import randint
def getjson():
    denguejson = json.loads(open('dengue_daily.json', 'r').read())

    dengue = [{k: v for k, v in d.iteritems() if (k==u'發病日' or k==u'最小統計區中心點X' or k==u'最小統計區中心點Y' or k==u'年齡層')} for d in denguejson]

    for i in range(0, len(dengue)):
        dengue[i]['time'] = dengue[i][u'發病日']
        del dengue[i][u'發病日']
        date = dengue[i]['time'].split('/')
        dengue[i]['time'] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), randint(0,23))
        dengue[i]['longitude'] = dengue[i][u'最小統計區中心點X']
        del dengue[i][u'最小統計區中心點X']
        if (dengue[i]['longitude']==None):
            dengue[i]['longitude'] = 0
        dengue[i]['latitude'] = dengue[i][u'最小統計區中心點Y']
        del dengue[i][u'最小統計區中心點Y']
        if (dengue[i]['latitude']==None):
            dengue[i]['latitude'] = 0
        dengue[i]['bornyear'] = dengue[i][u'年齡層']
        del dengue[i][u'年齡層']
        if (len(dengue[i]['bornyear'])==1):
            dengue[i]['bornyear'] = 1911 + 104 - int(dengue[i]['bornyear'])
        elif (len(dengue[i]['bornyear'])==3):
            if (dengue[i]['bornyear'][0]=='5'):
                dengue[i]['bornyear'] = 1911 + 104 - 7
            else:
                dengue[i]['bornyear'] = 1911 + 104 - 75
        elif (len(dengue[i]['bornyear'])==4):
            dengue[i]['bornyear'] = 1911 + 104 - int((int(dengue[i]['bornyear'][0:1])+int(dengue[i]['bornyear'][2:4]))/2)
        elif (len(dengue[i]['bornyear'])==5):
            dengue[i]['bornyear'] = 1911 + 104 - int((int(dengue[i]['bornyear'][0:2])+int(dengue[i]['bornyear'][3:5]))/2)
        
    return dengue


def getcsv():
    with open('dengue_age.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        data = [{k: v for k, v in d.iteritems() if (k=='發病年份' or k=='發病月份' or k=='年齡層')} for d in reader]
        
        j=0
        while (j<len(data)):
            data[j]['time'] = str(data[j]['發病年份'])+'/'+str(data[j]['發病月份'])
            del data[j]['發病年份']
            del data[j]['發病月份']
            date = data[j]['time'].split('/')
            data[j]['time'] = datetime.datetime(int(date[0]), int(date[1]), randint(1,30), randint(0,23))
            data[j]['bornyear'] = data[j]['年齡層']
            del data[j]['年齡層']
            if (len(data[j]['bornyear'])>5):
                del data[j]
                j-=1
        
            j+=1
        
        for i in range(0, len(data)):
            if (len(data[i]['bornyear'])==1):
                data[i]['bornyear'] = 1911 + 104 - int(data[i]['bornyear'])
            elif (len(data[i]['bornyear'])==3):
                if (data[i]['bornyear'][0]=='5'):
                    data[i]['bornyear'] = 1911 + 104 - 7
                else:
                    data[i]['bornyear'] = 1911 + 104 - 75
            elif (len(data[i]['bornyear'])==4):
                data[i]['bornyear'] = 1911 + 104 - int((int(data[i]['bornyear'][0:1])+int(data[i]['bornyear'][2:4]))/2)
            elif (len(data[i]['bornyear'])==5):
                data[i]['bornyear'] = 1911 + 104 - int((int(data[i]['bornyear'][0:2])+int(data[i]['bornyear'][3:5]))/2)
        
        return data
