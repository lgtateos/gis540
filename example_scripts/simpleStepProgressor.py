# simpleDStepProgressor.py
# Purpose:  Demonstrate simple step progressor.
# The time.sleep() stalls the dialog so you can watch what's happening.

import arcpy, os, time

def printArc(message):
    arcpy.AddMessage(message)
    print(message)
    
arcpy.env.workspace = 'C:/Temp'
printArc('Get the file types...')
# Set up step progressor with initial label, min, max, and interval
files =  os.listdir(arcpy.env.workspace)
minimum = 0
maximum = len(files)
interval = 1
arcpy.SetProgressor('step', 'Hurray', minimum, maximum, interval) 
time.sleep(0.5)

#Get the data type for each file in the directory
for f in files:
    describe = arcpy.Describe(f)
    arcpy.SetProgressorLabel('Loop: {0}'.format(i))
    arcpy.SetProgressorPosition()
    printArc('{0} file type: {1}'.format(f,describe.datatype) )
    time.sleep(2)

