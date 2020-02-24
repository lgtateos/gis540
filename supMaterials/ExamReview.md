# More exam review examples

1. Where's Waldo?  Find a comment, keyword, string literal, string variable, string method, list variable, list method, built-in module,  useless code that should be removed  (if any)

   ```python
   # makeDirectories.py
   # Author: Harry Houdini
   # Purpose: Make subdirectories for each name in a roll.txt doc.
   # Usage: No arguments needed.
   import arcpy, os,sys
   
   mydir = os.path.dirname(sys.argv[0])
   inputFile = mydir + "/roll.txt"
   outputFile = "Rolls-Royce"
   inf = open(inputFile,'r')
   
   for line in inf:
       line = line.rstrip()
       dirpath = mydir + "/" + line
       if not os.path.exists(dirpath):
           os.mkdir(dirpath)
   otherDirs = ['ABSTRACTS', 'THUMBNAILS', 'WRITEUPS']
   otherDirs[0].title()
   otherDirs[1].title()
   otherDirs[2].title()
   for name in otherDirs:
       dirpath = mydir + "/" + name
       if not os.path.exists(dirpath):
           os.mkdir(dirpath)
   currentFiles = os.listdir(mydir)
   print "Directory {0} contains {1} files.".format(mydir,len(currentFiles))
   ```

   Where's Waldo?  Locate the conditional statements,  comparison operator, logical operator, slicing, indexing

   ```python
   # keyTermSearch.py
   # Author: Gloria Steinem
   # Purpose: Perform a key term count.
   # Usage: Place this script in directory with txt files (no arguments needed)
   import re, os, sys
   
   mypath = os.path.dirname(sys.argv[0]) + "/"
   allFiles = os.listdir(mypath)
   textFiles = [ ]
       for f in allFiles:
           if f.endswith(".txt"):
               textFiles.append(f)
   textFiles.pop()
   outputDir = mypath + "out/"
   
   #If an output directory doesn't exist yet, make one.
   if not os.path.exists(outputDir):
       os.mkdir(outputDir)
   outF = open(outputDir + "results.txt", 'w')
   
   for myfile in textFiles:
       inf = open(mypath + myfile, 'r')
   
       contents = inf.read()  # Returns a string
       inf.close()
   
       #Change as needed
       termsOFinterest = ["potato", "rot", "rotted", "weather", "disease", "rain",
                  "rains", "decay", "sudden decay", "fungus", "black spot", "mould"]
       #Terms to remove
       termsToAvoid = ["dry rot", "sweet potato", "sweet potatoes"]
       
       numChars = 50
       message = "******************FILE NAME: "+ myfile+ " ******************\n"
       outF.write(message)
       print message
       for term in termsOFinterest:
           theCount = contents.count(term)
           message =  "Mention of " + term + "\n-----------------------------------"
           outF.write(message)
           print message
           trueCount = theCount
           if theCount > 0:
               for m in re.finditer(term, contents):
                   reallyMyWord = True
                   # Remove plurals of another term in list
                   # (e.g., don't add potatoes to the potato list)
                   for i in termsOFinterest:
                       # Compare the terms interest with the 
                       #   start of the string.Formatter
                       # If it starts with one of the terms and is not a substring of 
                       #  the term, then it's a plural.
                       # Remove it from the count and don't write it to the file.
                       if contents[m.start() : ].startswith(i) and i not in term:
                           #print "This is another search term:", i
                           reallyMyWord = False
                           trueCount = trueCount - 1
                   # If it hasn't yet been elimiated, check if it's one of our terms 
                   #  to avoid.
                   # (E.g., we want potato, but not sweet potato)
                   if reallyMyWord:
                       for bTerm in termsToAvoid:
                           if term in bTerm:
                               start = m.end()-len(bTerm)
                               if contents[start:m.end()] == bTerm:
                                   reallyMyWord = False
                                   trueCount = trueCount - 1                                
                   if reallyMyWord == True:  #How can this line of code be improved? 
                       message =  "\n\t"+ 
                       contents[m.start() - numChars : m.start() + numChars +len(term)]
                       outF.write(message)
                       print message
               message = "\nThe count for {0} is: {1}\n".format(term, trueCount)
               outF.write(message)
               print message  
   outF.close()
   ```

2. Specify whether each of the following lines of code would evaluate as **True** or **False** if used as a Boolean expression in a conditional statement. For example, (None) evaluates to True because it is a non-empty tuple and so bool((None)) returns True. Some expressions will generate an error when you try to use them in this way. For these, respond **ERROR**. 

   Assume that `fields` is `'fields1.shp'`, `centroids` is `'fieldCenters.shp'`, and `myNum` is `1`.

   ```python
   centroids.startswith('cen')
   0 <= myNum <= 2 <= (myNum + 5 - 2*myNum)
   "False"
   myNum**5
   mynum = fields[6]
   mynum == fields[6]
   fields.sort()
   fields == "foo" or centroids
   fields == "foo" and centroids
   myNum == 2 and centroids
   2/3 + 1/3 == 1
   0.25 - myNum/float(4)
   len(fields) != len(centroids)
   not None
   ```

   Check your answers for each expression by trying them in the Python console (Interactive Window) using *bool(theExpression)*

3. Use the given script arguments and the code fragments to **determine the printed output**. If the code would cause an error, write ERROR and give a brief explanation. Assume os and sys have already been imported. **Be sure to use case (upper and lower) and punctuation such as quotation marks and braces appropriately.**  

**Arguments:**    8 3 9 

   ```python
   print sys.argv[1] - 2
   ```

   **Arguments:**    42 3.4 99.9

   ```python
   print len(sys.argv)  - 2
   ```

   **Arguments:**    42 3.4 99.9 

   ```python
   i = int(sys.argv[2])
   print i
   ```

   **Arguments:**    42 3.4 99.9 

   ```python
   i = sys.argv[3]
   if i > 100:
       print "yay"
   else:
       print "boo"
   ```

   **Arguments:**    C:/gispy/data/ch10/xy.shp 

   ```python
   inputData = sys.argv[1]
   name = os.path.dirname(inputData)
   theExtension = os.path.splitext(inputData)[1]
   print name + "out" + theExtension
   ```

   **Arguments:**   elephant

   ```python
   theWord = sys.argv[1]
   theWord.rstrip('ant')
   myList = ['a','b','c'] 
   myList.extend('d')
   print myList.join(theWord)
   ```

   **Arguments:**    avavavoom 

   ```python
   exclamation = sys.argv[1]
   theBits = exclamation.split('v')
   print theBits
   ```

   **Arguments:**    oak

   ```python
   tree = sys.argv[1]
   if tree == 'pine' or "willow":
       print "yay"
   else:
       print "boo"
   ```

   

4. Describe exactly what will be returned by this expression:  arcpy.ListRasters("forest*","TIF")

5. Write a FOR-loop and the equivalent WHILE loop that print:
   -5
   2
   9
   16
   23
   30
   37
   44

6. Write a pseudocode that sets the restaurant rating based on the score given by the user.  If the score is more than 95, the restaurant is excellent.   If the score is less than 30, the restaurant is poor. Otherwise, if the score is 95 or less and 30 or higher, the restaurant is acceptable.  If the user does not provide an argument, tell them they need to provide this information.

7. Given the Summary Statistics tool signature, **Statistics_analysis (in_table, out_table, {statistics_fields}, {case_field})**, tell which toolbox the tool is in, list the required parameters, and list the optional parameters.  
   

8. Write a script that takes one argument, the full path file name of a GIS dataset. Then, if the data type of the input is ShapeFile or FeatureClass, it should print *point*, *line*, or *polygon* depending on the shapeType of the input. If the input data is a not a ShapeFile or FeatureClass, the code should print *I'm don't have a feature type*.

   

9. Write a script that takes one argument, the full path file name of a GIS dataset that will be summarized by calling the Summary Statistics tool.   Place the output in a subdirectory of the directory where the input dataset resides.  Name the output directory  *myOutput*.   For example, if the user passes in C:/foo/mydata.txt, the output will be placed inside of C:/foo/output.   Use the **os.path.dirname** method to get the inputs location.  Use the **os.path.exists** method to check if the output directory already exists.  If not, use the **os.mkdir** method to create it.

   

10. Use the FeatureToPoint tool to convert all the Polygon files in a workspace whose names contain 'oak' to point.  The script takes 2 arguments, an input directory and an output directory.  The tool signature is **FeatureToPoint_management(in_features, out_feature_class, {point_location})**

    

11. List all the point feature classes in C:/gispy/data/ch10/tester.gdb whose names start with 's'.

    Call arcpy.CreateFileGDB_management('C:/gipsy/scratch/', 'out.gdb') to create a new gdb.

    Write copies the point feature classes whose names start with 's' from C:/gispy/data/ch10/tester.gdb and copies them to C:/gispy/scratch/out.gdb. The destination needs to have a slash between the. destination = destWorkspace + '/' + fc

    

12. Create a list of all of the files in a directory whose names end in prj or shx and are smaller than 2000 bytes.  Use **os.listdir** to get a list of all the files.  Given the *full path* of a file, **os.path.getsize** returns the size in bytes. 
