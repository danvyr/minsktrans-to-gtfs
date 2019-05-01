##!/usr/bin/env python3'
## -*- coding: utf-8 -*-

#download and collecrt different versions of minsktrans

import os
import urllib.request
import hashlib
from datetime import datetime, date

BLOCKSIZE = 65536




stops  = 'http://www.minsktrans.by/city/minsk/stops.txt'
routes = 'http://www.minsktrans.by/city/minsk/routes.txt'
times = 'http://www.minsktrans.by/city/minsk/times.txt'

urls =(('stops', stops),
      ('routes', routes), 
      ('times', times))

data_folder = 'data'



if not os.path.exists(data_folder):
      os.mkdir(data_folder)


def createFileName(name):

      today = datetime.strftime(datetime.now(), "%Y%m%d") 
      if not os.path.exists(data_folder+ '/' +today):
            os.mkdir(data_folder+ '/' +today)
         
      name = data_folder+ '/' +today+ '/' +name +'_'+ today + '.csv'
      print (name)
      return name




for name, url  in urls:
      fileName = createFileName(name)

      urllib.request.urlretrieve(url, fileName) 

      hasher = hashlib.md5()      
      with open(fileName,'rb') as file_to_check:

            buf = file_to_check.read(BLOCKSIZE)
            while len(buf) > 0:
                  hasher.update(buf)
                  buf = file_to_check.read(BLOCKSIZE)

            with open(fileName+'.md5','w') as file_with_hash:     
                  file_with_hash.write(hasher.hexdigest())             


