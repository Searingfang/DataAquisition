# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json, requests

url = "https://api.dailymotion.com/videos?fields=title,views_total,&sort=recent&limit=100"
r = requests.get(url)

struc = r.json()

f = open('data.txt', 'w')
for x in struc[u'list']:
    f.write(str(x) + '\n')

url = "https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&maxResults=50&key=AIzaSyDMg-eb-hHji1WEF_H_je1SXSt9HsMeofU"
r = requests.get(url)

struc = r.json()
print struc.keys()
f = open('data2.txt', 'w')
for x in struc[u'items']:
    f.write(str(x) + '\n')