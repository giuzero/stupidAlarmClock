#!/usr/bin/env python3
import requests
from subprocess import call
from datetime import date, timedelta

"""
TODO: manage year folder, first day of the year bug.
"""

r= requests.get("http://audio.radio24.ilsole24ore.com/radio24_audio/2018/")

n = 0
for i in range (10):
    checkDay = int((date.today()- timedelta(i)).strftime('%y%m%d'))
    filename = str(checkDay) + "-lazanzara-s.mp3"
    if filename in r.text:
        print("FOUND: "+ filename)
        break
    n+=1

if n>i:
    print("NOT FOUND")
else:
    t = requests.get("http://audio.radio24.ilsole24ore.com/radio24_audio/2018/" + filename, stream=True)
    print(t.status_code)
    with open(filename, "wb") as content:
        for chunk in t.iter_content(chunk_size=1024):
            if chunk:
                content.write(chunk)
    print("PLAY: " + filename)
    call(["omxplayer", filename])
