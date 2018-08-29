import sys, arcpy, os

def printArc(message):
    print message
    arcpy.AddMessage(message)

#Check incoming arguments
for index, value in enumerate(sys.argv):
    m = "Arg {0} = {1}".format(index, value)
    print m
print

#Set input variables
datafile = sys.argv[1]
fieldname = sys.argv[2]
fieldvalue = sys.argv[3]

#Get count
whereClause = "%s = \'%s\'" % (fieldname, fieldvalue)
sc = arcpy.SearchCursor(datafile, whereClause)
count = 0
for row in sc:
    count = count + 1
del row

#Print results
m = "The {0} field in {1} contains {2} occurances of {3}.".format( fieldname,
                                                                     datafile,
                                                                     count,
                                                                     fieldvalue)
print m
