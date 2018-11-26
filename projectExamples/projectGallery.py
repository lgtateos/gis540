######################################################################
## 
## projectGallery.py
## Purpose: Read a text file with project information:
##             Title, Name, Synopsis, and Keywords
##          and create an html webpage named output.html
##          containing the content given in the file AND
##          the thumbnail located in the same directory
##
######################################################################

import os, sys
import tkFileDialog, Tkinter

test = 0
dataDir = os.path.dirname(sys.argv[0]) #use scripts location as default directory

#Set default values for testing
thumbnail = "http://courses.ncsu.edu/nr595d/common/images/project_icons/2011Spring/njlyons.png"
video1 = "http://courses.ncsu.edu/gis540/common/projectVideos/2011_Spring/jrgreco"
title ="Amazing GIS with Python"
name="Jane Python Doe"
video2 = "http://courses.ncsu.edu/gis540/common/projectVideos/2011_Spring/jrgreco"
synopsis = "The City of Raleigh annually has their planimetric layer updated from aerial photography. \
This tool takes this data and measures the amount of impervious surface for specified properties.  \
The result is a list of the properties and their impervious surface areas broken into categories, \
sub-categories, and sub-types."
keywords = "Impervious Surface, Storm Water, Planimetric Data, City of Raleigh, Property, Union, \
Select Layer by Attributes, Select Layer by Location"

if not test:
    fatherWilliam = Tkinter.Tk()
    fatherWilliam.withdraw()
    projectFile = tkFileDialog.askopenfilename( initialdir =dataDir,
                        title='Choose a synopsis file.',
                        filetypes=[("Text File", "*.txt")] ) 
    fatherWilliam.destroy()

#Find thumbnail in current directory
files = os.listdir(dataDir)
for f in files:
    extension = f[-4:]
    if extension in [".jpg", ".gif", ".png"]:
        thumbnail = "./" + f

fields = {"title":title, "name":name,"synopsis":synopsis,"keywords":keywords}

#Derive input from text file
if not test:
    inf = open(projectFile, 'r')
    for line in inf:
        pieces = line.split(":")
        firstWord = pieces[0].strip().lower()
        if firstWord in fields.keys():
            pieces.pop(0)
            pieces = ":".join(pieces)
            current = firstWord
            fields[firstWord] = pieces
        else:
            fields[current] = fields[current] + line

#Create html string            
projectInfo = '''
<html>
<p><strong>Fall 2011</strong></p>
<hr />
<table width="640" >
  <tr>
    <td scope="row">
      <table width="600" border="0">
        <tr> 
          <td width="67"><img src="%s" alt="a" /></td>
          <td width="523"><strong><a href="%s1.swf">%s - %s (2 part video) Part 1,</a>
          <a href="%s2.swf">Part 2</a></strong></td>
        </tr>
      </table>

      <blockquote>
        <p>%s</p>
        <p><strong>Keywords:</strong> %s</p>
      </blockquote>
  
     </td>
  </tr>
</table>
<hr />
</html>'''  % (
thumbnail,
video1,
fields["title"], 
fields["name"],
video2,
fields["synopsis"],
fields["keywords"])

outf = open(dataDir+ "/output.html", 'w')
outf.write(projectInfo)
outf.close()