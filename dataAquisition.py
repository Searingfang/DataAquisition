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
for x in struc[u'list']:
    f.write(x[u'title'].encode('utf-8') + '\n')
    f.write('total views: ' + str(x[u'views_total']) + '\n')
    f.write('created time: ' + str(x[u'created_time']) + '\n\n')
    
while struc[u'has_more'] and limit < 10:
    limit += 1
    r = requests.get(url + str(limit))
    struc = r.json()
    for x in struc[u'list']:
        f.write(x[u'title'].encode('utf-8') + '\n')
        f.write('total views: ' + str(x[u'views_total']) + '\n')
        f.write('created time: ' + str(x[u'created_time']) + '\n\n')    


f = open('data2.txt', 'w')
limit = 1
url = "https://www.googleapis.com/youtube/v3/videos?part=statistics%2Csnippet&chart=mostPopular&key=AIzaSyDMg-eb-hHji1WEF_H_je1SXSt9HsMeofU"
r = requests.get(url)
struc = r.json()

for x in struc[u'items']:
    f.write(x[u'snippet'][u'title'].encode('utf-8') + '\n')
    f.write('total views: ' + str(x[u'statistics'][u'viewCount']) + '\n')
    f.write('created time: ' + str(x[u'snippet'][u'publishedAt']) + '\n')
    
while u'nextPageToken' in struc and limit < 10:
    r = requests.get(url + '&pageToken=' + struc[u'nextPageToken'])
    struc = r.json()
    for x in struc[u'items']:
        f.write(x[u'snippet'][u'title'].encode('utf-8') + '\n')
        f.write('total views: ' + str(x[u'statistics'][u'viewCount']) + '\n')
        f.write('created time: ' + str(x[u'snippet'][u'publishedAt']) + '\n')
