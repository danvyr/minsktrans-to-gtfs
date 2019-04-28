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
    urllib.request.urlretrieve(url, name+'.csv') 
       
   
    with open(name+".csv") as file_to_check:

        data = file_to_check.read()    
        #md5_returned = hashlib.md5(data).hexdigest()
        # hashList(name)= 
        # pipe contents of the file through
        #print (md5_returned)

