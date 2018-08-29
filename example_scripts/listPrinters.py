import arcpy, sys
print sys.argv[1]  #First message
for printerName in arcpy.mapping.ListPrinterNames():
    print sys.argv[2] + ": "+printerName
