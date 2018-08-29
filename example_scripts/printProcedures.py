#################################################
#Example of defining a procedure (no arguments)
def printYears():
    """Print every five years between 1980 and 2005."""
    yrs = range(1980,2005,5)
    for yr in yrs:
        print yr

#Example of calling a procedure (no arguments)
print "Call printYears()"
printYears( )
print "----"
#################################################

#################################################
#Example of defining a procedure (WITH arguments)
def printMyYears(start, stop):
    """Print every year between start and stop."""
    yrs = range(start, stop + 1)
    for yr in yrs:
        print yr


#Example of calling a procedure (WITH arguments)
print "----"
print "Call printMyYears(1920,1926)."
printMyYears(1920,1926)
#################################################




#List to use for texting the printShp procedure
testList = ['a.shp', 'a.txt', 'cRaster']



