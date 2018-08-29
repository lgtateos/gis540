import os, sys
## add imports as needed

def saveBinary(localDir, binPath):
    '''Fetches web hosted binary file (at binPath) and saves it with same name (to localDir)'''
    #Fetch the binary file
    #response = ## Use urllib2 to fetch the binary file
    #Read the binary contents
    binContents = response.read()
    response.close()

    #Write the binary file to disk in localDir
    basename = os.path.basename(binPath)
    fullOutName = localDir + "/" + basename
    outf = open(fullOutName,"wb")
    outf.write(binContents)
    outf.close()

def unzip(zip,dest):
    '''Unzip a compressed file (zip) into the destination directory (dest).'''
    print "Unzipping", zip, "to", dest
    #Get a zipfile object
    zip = zipfile.ZipFile(zip, 'r')
    if not os.path.exists(dest):
        os.makedirs(dest)
    #Get a list of files in the archive
    zipList = zip.namelist()
    for filename in zipList:
        #Get the binary file contents and print the byte count in the current file
        binContents = zip.read(filename)
        print '  Unzipping file:', filename, 'with', len(binContents), 'bytes..'
        #Write the binary file to disk
        outf = open(dest + filename, 'wb')
        ## write the binContents to the output file
        outf.close()
    zip.close
    print "Extraction complete."

#Fetch HTML from Wake County Data download website
url = 'http://www.wakegov.com/gis/services/Pages/data.aspx'


response = urllib2.urlopen(url)
html = response.read()
response.close()

#Parse hyperlinks in Data Download page
soup = BeautifulSoup.BeautifulSoup(html)
tags = soup.findAll("a" , href=True)
for t in tags:
    for attr, value in t.attrs:
        if attr == "href":
            if value.startswith("ftp:") and value.endswith(".zip"):
                if "Wake_Streets" in value:
                    print  attr, " = ", value
                    ## Call the saveBinary procedure
                    ## Call the unzip procedure


