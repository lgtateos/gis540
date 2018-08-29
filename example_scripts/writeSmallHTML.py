#writeSnazzyPage.py
import arcpy, os
baseDir = 'C:/gispy/'
fc = 'data/ch20/park.shp'
baseName = os.path.basename(fc)
fieldName = 'COVER'
image = '../data/ch20/pics/park.png'
output = baseDir + 'scratch/smallHTML.html'

def python2htmlList(myList, listType, attrs=''):
    '''Convert a Python list to HTML list.
    For example, convert [rast1,rast2] to:
    <ul>
       <li>rast1</li>
       <li>rast2</li>
    </ul>
    '''
    # Wrap items in item tags.
    htmlItems = ['<li>' + str(item) + '</li>' for item in myList]

    # Join the item list into a string with a line break after each item.
    itemsString = '''\n        '''.join(htmlItems)

    # Wrap the string of items in the list tag.
    htmlList = '''
    <{0} {1}>
        {2}
    </{0}>
    '''.format(listType, attrs, itemsString)
    return htmlList

def getFieldValues(tableName, theFieldName):
    '''Given the full path file name (tableName) of a feature class or
    other SearchCursor accessible table, get a Python list
    of values in a field named, theFieldName
    '''
    try:
        sc = arcpy.da.SearchCursor(tableName, [theFieldName])
        valueList = [row[0] for row in sc]
        del sc
    except:
        valueList = []
        print 'An error occurred in \
        getFieldValues accessing {1} in {0}.'.format(
            tableName, theFieldName)
        del sc
        
    return valueList

def getUniqueListValues(theList):
    '''Return the unique values in theList (a Python list).'''
    uniqueValueSet = set(theList)
    uniqueValueList = list(uniqueValueSet)
    return uniqueValueList 

## Get values for the given field

## Get unique values for the given field
uniqueValueList = ["Empty", "List"]

## Create HTML bullet list from the unique value list.
htmlList = python2htmlList(uniqueValueList, "ol")

## Write code to create a string for an html image tag
imageCode = '&nbsp;&nbsp;&nbsp;&nbsp;Your <br />&nbsp;&nbsp;&nbsp;&nbsp;picture<br />&nbsp;&nbsp;&nbsp;&nbsp; here'
#Wrap in items in ul tag (and add the first li which is missing).
body = """
   <table border="1">
       <tr>
           <td>
               {0}
            </td>
           <td>
               {1}
           </td>
       </tr>
   </table>
""".format(htmlList, imageCode)

#Create header with title
header = """<!DOCTYPE html>
<html>
 <body>
  ##Place HTML code here for the dynamic page header
""".format() ##Place variables inside the parenthesis to create dynamic page header

#Create footer to close body and html tags
footer ="""
 </body>
</html>
"""
outf = open(output,'w')
outf.write(header + body + footer)
outf.close()
print '{0}  created.'.format(output)
