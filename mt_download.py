# !/usr/bin/env python3'
# -*- coding: utf-8 -*-

# download and collecrt different versions of minsktrans

import os
import shutil
import urllib.request
import hashlib
from datetime import datetime, date

BLOCKSIZE = 65536  # need for hashing


stops = 'http://www.minsktrans.by/city/minsk/stops.txt'
routes = 'http://www.minsktrans.by/city/minsk/routes.txt'
times = 'http://www.minsktrans.by/city/minsk/times.txt'

urls = (('stops', stops),
        ('routes', routes),
        ('times', times))

data_folder = 'data'
temp_folder = '/tmp/'
versionFile = 'lastVersion.txt'
today = datetime.strftime(datetime.now(), "%Y%m%d")


def checkDataFolder():
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

        
def checkFilesFolder():
    if not os.path.exists(data_folder + '/' + today):
        os.mkdir(data_folder + '/' + today)


def createFileName(name):
    return data_folder + '/' + today + '/' + name + '_' + today + '.csv'


def createTempName(name):
    return temp_folder + '/' + name + '.csv'


# read lastversion file or create it if it not exists
def lastVersionFile(name):
    version = '0'
    try:
        with open(data_folder+'/'+versionFile, 'r') as verFile:
            version = verFile.readline()

    except:
        # TODO make shure that the last directory format YYYYNMDD
        for d in os.listdir(data_folder):
            if os.path.isdir(data_folder + '/' + d) and int(d) <= int(today) and int(d) > int(version):
                version = d
        with open(data_folder+'/'+versionFile, 'w') as verFile:
            verFile.write(version)

    return data_folder + '/' + version + '/' + name + '_' + version + '.csv'


def download():

    difference = 0  # how much downloaded files differ from already stored

    # download new files, create md5 hash and compare hashes with old files
    for name, url in urls:
        tempName = createTempName(name)

        urllib.request.urlretrieve(url, tempName)

        hasher = hashlib.md5()
        with open(tempName, 'rb') as file_to_check:

            buf = file_to_check.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = file_to_check.read(BLOCKSIZE)

            # write hash file
            with open(tempName + '.md5', 'w') as file_with_hash:
                file_with_hash.write(hasher.hexdigest())

            # open last hash file and compare
            with open(lastVersionFile(name) + '.md5', 'r') as lastVerHash:
                if hasher.hexdigest() != lastVerHash.readline():
                    difference = +1
                    print(name)


    # print(lastVersionFile(stops))

    # move new files to folders and update lastVersionFile

    if difference:
        checkFilesFolder()

        if not os.path.exists(data_folder + '/' + today):
            os.mkdir(data_folder + '/' + today)

        for name, url in urls:
            fileName = createFileName(name)
            tempName = createTempName(name)

            shutil.move(tempName, fileName)
            shutil.move(tempName + '.md5', fileName + '.md5')
        
        #update version file    
        with open(data_folder+'/'+versionFile, 'w') as verFile:
            verFile.write(today)
    else:
        for name, url in urls:
            tempName = createTempName(name)
            os.remove(tempName)
            os.remove(tempName + '.md5')
        


if __name__ == "__main__":
    checkDataFolder()  
    download()
