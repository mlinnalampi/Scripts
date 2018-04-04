#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib3
import json
import certifi
import shutil
import sys


def getPdfLinks(d):
    urls = []
    titles = []
    print("Getting links")
    for i in d:
        url = 'https://hacker-news.firebaseio.com/v0/item/' + str(i)  + '.json?print=pretty'
        r = http.request('GET', url)
        df=json.loads(r.data.decode('utf-8'))
        if '[pdf]' in df['title'].lower():
            url = df['url']
            urls.append(url)
            titles.append(df['title'])
            i=len(urls)
            print(str(i), "Title:", titles[i-1])#, "\n   Url:", urls[i-1], '\n')
    return urls,titles


def getIndices(alles=False):
    if alles:
        return [i for i in range(1,(len(titles)+1))]

    print("Give titles to fetch")
    nums = input().split(" ")

    if "all" in nums:
        nums2 = [i for i in range(1, len(titles)+1)]

        for f in nums:
            if str(f)[0] == '-':
                nums2.remove(int(f[1:]))
        return nums2
    return nums


if "--all" in sys.argv:
    alles=True
else:
    alles=False

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
r = http.request('GET', 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')

d = json.loads(r.data.decode('utf-8'))

urls, titles = getPdfLinks(d)

nums = getIndices(alles)

for n in nums:
    try:
        print("Fetching pdf number", str(n))
        fn=('/docker/'+(titles[int(n)-1].replace('[pdf]', '').replace('?', '').replace('/', '').replace('\\', '').replace('"', '').replace('“', ''))+'.pdf').replace(' .', '.')
        req = http.request('GET', urls[int(n)-1], assert_same_host=False, preload_content=False,timeout=60)
        if req.status != 200:
            print("Problem with url", urls[int(n)-1], " got status", req.status)
            continue
        with open(fn, 'wb') as f:
           shutil.copyfileobj(req, f)
        req.release_conn()
    except Exception as e:
        print("Failed, title:", titles[int(n)-1], "url", urls[int(n)-1], "and error: ", e)
