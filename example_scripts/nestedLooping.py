def printLineLengths (filename):
    '''Given a full path text file name, print the length of each line'''
    print filename
    inf = open( filename, "r")
    for line in inf:
        print len(line)
#Test
##print "printLineLength"
##printLineLengths("C:/Temp/testNest/lasagna.py")

import os
def getFullFileNames(dirname):
    '''Given directory name, return a list of full path file names for its files'''
    if not dirname.endswith("/") and not dirname.endswith("\\"):
        dirname = dirname + "/"
    files = os.listdir(dirname)
    return [ dirname + i for i in files ]
#Test
##print "getFullFileNames"
##print getFullFileNames("C:/Temp/testNest")

import os
def pyORdir(filename):
    '''Given a full path file name, return py for Pythin scripts and dir for directories'''
    if filename.endswith(".py"):
        return "py"
    elif os.path.isdir(filename):
        return "dir"
    return "other"
#Test
##print "pyORdir"
##print pyORdir("C:/Temp/testNest/dictionary")
##print pyORdir("C:/Temp/testNest/lasagna.py")
##print pyORdir("C:/Temp/testNest/Hello.txt")
##Pseudocode
##GET root directory
##CALL getFullFileNames
##FOR each file
##    CALL pyORdir
##    IF file is Python script
##       CALL printLineLengths
##    ELSEIF file is a directory
##        CALL getFullFileNames
##        FOR file in the subdirectory
##            CALL pyORdir
##            IF file is Python script
##                  CALL printLineLengths

import os

dirName = "C:/Temp/testNest/"
files = getFullFileNames(dirName)
for file in files:
    type = pyORdir(file)
    if type == "py":
        printLineLengths(file)
    elif type == "dir":
        subFiles = getFullFileNames(file )
        for sfile in subFiles:
            type = pyORdir(sfile)
            if type == "py":
                printLineLengths(sfile)

        