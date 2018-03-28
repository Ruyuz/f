#!/usr/bin/env python3

import sys
import stat
import os
import datetime
import time
import sys
from pathlib import Path

if len(sys.argv) == 1:
    print('stat: missing operand\nTry \'stat --help\' for more information.')

else:
    file_name = sys.argv[1]
    if not Path(file_name).exists():
        print('stat: cannot stat \'{}\': No such file or directory'.format(file_name))
    else:
        def file_type(mode): # Reference: From the website recommended by Yang Chen: https://stackoverflow.com/questions/4989431/how-to-use-s-isreg-and-s-isdir-posix-macros
            if stat.S_ISDIR(mode) != 0:
                return 'directory'
            elif stat.S_ISCHR(mode) != 0:
                return 'special file'
            elif stat.S_ISBLK(mode) != 0:
                return 'block special'
            elif stat.S_ISREG(mode) != 0:
                if os.stat(file).st_size == 0:
                    return 'regular empty file' #Ziqing Zhang helped me identify regular empty file.
                return 'regular file' 
            elif stat.S_ISFIFO(mode) != 0:
                return 'FIFO/pipe'
            elif stat.S_ISLNK(mode) != 0:
                return 'symbolic link'
            elif stat.S_ISSOCK(mode) != 0:
                return 'socket'
            elif stat.S_ISDOOR(mode) != 0:
                return 'door'
            elif stat.S_ISPORT(mode) != 0:
                return 'event port'
            elif stat.S_ISWHT(mode) != 0:
                return 'whiteout'


        file_st = os.stat(file_name)
        print('  File:' + '\'' + str(file_name))
        print('  Size: ' + str(file_st.st_size)  + '       BLocks: ' + str(file_st.st_blocks) + '       IO Block: ' + str(file_st.st_blksize)+ ' ' + str(file_type(file_st.st_mode)) )
        print('Device: ' + str(hex(file_st.st_dev)[-2:]) + 'h/' + str(file_st.st_dev) + 'd Inode: ' + str(file_st.st_ino) + '  Links: ' + str(file_st.st_nlink) )
        print('Access: ' + '('+str(oct(os.stat(file_name).st_mode)[-4:]) + '/' + str(stat.filemode(os.stat(file_name).st_mode)) + ')'+ '  Uid: ' + '(' + str(os.stat(file_name).st_uid) + '/  ' + str(Path(file_name).owner())+')' + '   Gid: ' + '(' + str(os.stat(file_name).st_gid) +  '/  ' + str(Path(file_name).group())+')') #Reference: Ziqing Zhang taught me how to find owner and group
        print('Access: ' + str(datetime.datetime.fromtimestamp(float(file_st.st_atime)).strftime('%Y-%m-%d %H:%M:%S.%f')) +'  '+ time.strftime("%z", time.localtime())) #Time Zone Reference: https://stackoverflow.com/questions/1111056/get-time-zone-information-of-the-system-in-python
        print('Modify: ' + str(datetime.datetime.fromtimestamp(float(file_st.st_mtime)).strftime('%Y-%m-%d %H:%M:%S.%f'))+'  '+ time.strftime("%z", time.localtime()))
        print('Change: ' + str(datetime.datetime.fromtimestamp(float(file_st.st_ctime)).strftime('%Y-%m-%d %H:%M:%S.%f'))+'  '+ time.strftime("%z", time.localtime()))
        print(' Birth: -')  
