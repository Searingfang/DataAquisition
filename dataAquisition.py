# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
f = open('data.txt', 'w')
limit = 1
url = "https://api.dailymotion.com/videos?fields=created_time,title,views_total,&sort=visited&limit=100&page="
r = requests.get(url + str(limit))
struc = r.json()

while struc[u'has_more'] and limit < 10:
    for x in struc[u'list']:
        f.write(x[u'title'].encode('utf-8') + '\n')
        f.write(str(x[u'views_total']) + '\n')
        f.write(str(x[u'created_time']) + '\n\n')
    limit += 1
    print limit
#    r = requests.get(url + limit)
#    struc = r.json()
    


#url = "https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&maxResults=50&key=AIzaSyDMg-eb-hHji1WEF_H_je1SXSt9HsMeofU"
#r = requests.get(url)
#
#struc = r.json()
#print struc.keys()
#f = open('data2.txt', 'w')
#for x in struc[u'items']:
#    f.write(str(x) + '\n')