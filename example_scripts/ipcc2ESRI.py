# ipcc2ESRI.py
# Purpose: Convert an IPCC .dat format file to ESRI ASCII .txt format.
#         Then call ESRI's ASCIItoRaster tool to convert the ascii file to a GRID raster.
# Usage: fullpath_filename output_directory
# Output: A modified IPCC data file in ESRI ASCII format and an ESRI GRID raster.
# Example input: C:/Temp/precipitation6190.dat C:/Temp/scratch/

import arcpy, os, sys

def modifyLine(line):
    '''Read the line, split at every nth character,
     and insert space delimitation in output file'''
    n = 5
    line = line.rstrip()
    #Split the string every 5th character.
    lineList = []
    for i in range(0, len(line), n):
        val = line[i:i+n]
        lineList.append(val)
    newLine = ' '.join(lineList) + '\n'
    return newLine
    
    
def readHeader(inf):
    '''Read metadata header and return a dictionary 
       of header field names and values''' 
    dict = {}
    try:  
        ### 1. Read a line of the input file and set the 'line1' to the return value
        ###
        line1 = line1.split()
        
        ### 2. Read another line of the input file and set the 'line2' to the return value
        ###
        line2 = line2.split()
        for index, value in enumerate(line1):
                dict[value] = line2[index]
    except:
        print 'Warning: unable to read header.'
    return dict

def writeHeader(outfl, ldict, lcellsize, lflag):
    '''Write an ESRI ASCII file format header.'''
    try:
        wordList = ['cols','rows','xmin', 'ymin']
        outwordList = ['ncols', 'nrows', 'xllcorner', 'yllcorner']
        #write ncols, ncols, xllcorner, and yllcorner
        for index,value in enumerate(wordList):
            key = wordInKey(ldict, value)
            headerElement = '{0} {1}\n'.format(outwordList[index] , ldict[key])
            outfl.write(headerElement)
        cellSizeStr = 'cellsize {0}\n'.format(str(lcellsize))
        outfl.write(cellSizeStr)
        nodataStr = 'nodata_value  {0}\n'.format(str(lflag)) 
        ### 3. write 'nodataStr' to the output file 'outfl'
        ###
    except:
        print 'Warning: The header may not have been successfully written.'
    
def wordInKey( ldict, word):
    '''Return key containing 'word' as a substring
    (if there's more than one, the last one encountered is returned)'''
    val = ''
    for key in ldict.keys():
        if word in key:                
            val = key
    return val

#~~~~~~~~~~Begin main program (end proc definitions) ~~~~~~~

#Set input and output file names
try:
    inputFile = sys.argv[1]
    inputDir = os.path.dirname(inputFile) + '/'
    outDir = sys.argv[2]
except IndexError:
    inputFile = 'precipitation6190.dat'
    inputDir = 'C:/Temp/'
    outDir = 'C:/Temp/scratch'
    print '''Warning: no input provided.
            Attempting to use default file: {0}/{1}'''.format(inputDir, inputFile)

if not os.path.exists(inputFile):
    print 'Usage: <input directory> <input file name>'
    sys.exit(0)
 
try:
    flag = -9999
    cellsize = .5
        
    print 'Converting IPCC format file {0}{1} to ESRI ascii format'.format(inputDir,inputFile)
    ### 4. Write a WITH statement that opens the input file for reading and creates a file object named 'inf'.
    ### 
        print 'Processing header:'
        dict = readHeader(inf)
        key = wordInKey(dict,'cols')
        numcols = int(dict[key])
        key = wordInKey(dict,'rows')
        numrows = int(dict[key])
        output = outDir + 'ASCIIout.txt'
        ### 5. Write a WITH statement that opens the 'output' file for
        ###    writing and creates a file object named 'outf'.
        ###
            writeHeader(outf, dict, cellsize, flag)
            print 'Processing rows...'
            for line in inf:
                spaceLine = modifyLine(line)
                outf.write(spaceLine)
            ### 6. close the input file 
            ###
            ### 7. close the output file
            ###
            print 'ASCII file created. View {0} in Windows Explorer.'.format(output) 

except IOError:
    print 'Could not open {0}{1}'.format(inputFile)

try:
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = inputDir
    print 'Converting ASCII to Raster'
    baseN = os.path.basename(inputFile)
    basenameSize = min([len(baseN),4])
    outRaster = outDir + baseN[:basenameSize] + 'GRID'
    ### 8. Call the ArcGIS ASCII to Raster conversion tool to convert the 
    ###    'output' text file to 'outRaster', setting the data type of the output raster to INTEGER. 
    ###
    print 'Conversion complete.  View {0} in ArcCatalog.'.format(outRaster)
except:
    print arcpy.GetMessages()
    
    