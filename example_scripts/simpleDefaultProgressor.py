# simpleDefaultProgressor.py
# Purpose:  Demonstrate simple default progressor.
# The time.sleep() stalls the dialog so you can watch what's happening.

import arcpy, os, time

def printArc(message):
    arcpy.AddMessage(message)
    print message
    
arcpy.env.workspace = 'C:/Temp'
printArc('Howdy')

# Show the default progress dialog. 
arcpy.SetProgressor('default', 'Using get count')
time.sleep(0.5)  #Suspend execution for 0.5 seconds.

#Get the count for each feature class in the directory
fcs = arcpy.ListFeatureClasses()
for i, fc in enumerate(fcs):
  arcpy.SetProgressorLabel('Get count {0}'.format(i))
  try:
      count = arcpy.GetCount_management(fc)
      printArc('{0} has {1} records.'.format(fc, count) )
  except:
      printArc('Could not get count for ' + fc)
  time.sleep(2)  #Suspend execution for 2.5 seconds.

printArc('Good bye')
arcpy.ResetProgressor()





