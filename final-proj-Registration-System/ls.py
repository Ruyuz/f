#!/usr/bin/env python3
import sys
from pathlib import Path
import os
import stat
import datetime
import time


file_path = []
if len(sys.argv) > 1: # if exist new input, overwrite 
    file_path = sys.argv[1:]
else:
    file_path.append(os.getcwd()) # current working directory


def check_path(path):
    for file_name in path:
        if os.path.isfile(file_name):
            p = Path(file_name)
            protection_wrx = stat.filemode(os.stat(file_name).st_mode)
            file_link = os.stat(file_name).st_nlink
            file_size = os.stat(file_name).st_size
            file_time = os.stat(file_name).st_ctime
            file_modi_time = datetime.datetime.fromtimestamp(float(file_time)).strftime("%b %d %H:%M") 
            print('{} {:>10} {:>15} {:>15} {:>10} {:>15} {} '.format( protection_wrx, file_link, p.owner(), p.group(), file_size, file_modi_time, file_name))
        else:
            try:
                os.chdir(file_name)
            except:
                print('ls: cannot access \'{}\': No such file or directory'.format(file_path))
                return
        
            files = os.listdir(file_name) # traverse all files in file_path list, including subdirectories
            files.append('.')
            files.append('..')
            files = sorted(files, key = lambda s: s.lower()) #.replace(r'.', '').lower()
        
            for file_name in files:
                p = Path(file_name)
                protection_wrx = stat.filemode(os.stat(file_name).st_mode)
                file_link = os.stat(file_name).st_nlink
                file_size = os.stat(file_name).st_size
                file_time = os.stat(file_name).st_ctime
                file_modi_time = datetime.datetime.fromtimestamp(float(file_time)).strftime("%b %d %H:%M") 
                print('{} {:>10} {:>15} {:>15} {:>10} {:>15} {} '.format( protection_wrx, file_link, p.owner(), p.group(), file_size, file_modi_time, file_name))


check_path(file_path)