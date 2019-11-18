#! /usr/bin/env python
#backup.py - backup versions of python source files
import sys, os
from shutil import copy
from string import lower
from filecmp import cmp

targetdir=""
try:
    targetdir=sys.argv[1]
except:
    targetdir="."

files=os.listdir(targetdir)

#Backup directory
for file in files:
    ext=lower((os.path.splitext(file))[1])

    if ext in ('.py', '.ht'):
        abspath=os.path.abspath(os.path.join(targetdir, file))
        print 'Backing up file ', file ,'...'
        #check for existence of previous versions
        index=0
        while os.path.exists(abspath + '.bak.' + str(index)):
            index += 1
        if not index==0:
            #no need to backup if file and last version are identical
            if cmp(abspath, abspath + '.bak.' + str(index-1), shallow=False):
                continue
        copy(abspath, abspath + '.bak.' + str(index))