##!/usr/bin/env python3'
## -*- coding: utf-8 -*-

#download and collecrt different versions of minsktrans


import hashlib
import urllib.request


stops  = 'http://www.minsktrans.by/city/minsk/stops.txt'
routes = 'http://www.minsktrans.by/city/minsk/routes.txt'
times = 'http://www.minsktrans.by/city/minsk/times.txt'

urls =(('stops', stops),
      ('routes', routes), 
      ('times', times))


for name, url  in urls:
    urllib.request.urlretrieve(url, name) 
       
    hashList(name)= hashlib.md5(name).hexdigest()

