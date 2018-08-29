#Purpose: practice calling class object from another class

### 1. add code here so that you can use module excel_lib


#Example of creating an ExcelDocument object called exO1. This one sets visibility to False
exO1 = excel_lib.ExcelDocument(False) 
exO1.quit() #Quit this excel session.

### 2. add code to create an ExcelDocument object called exObj, set visibility to True


#Creating a new file
exObj.new()  # open a new blank excel document

exObj.set_value("A1:A10", "GIS") #set values in A1:A10 to GIS
exObj.set_cell_value(3,10, "cool") #set value in third column 10th row to cool
### 3. add code to set the 2nd value in the third row to Bonus!


row = ['a','b','c']
exObj.set_value("A1:C1", row)

exObj.save()  #Save the file with the default name
print "File saved to", exObj.getName() 
filename = exObj.getName() 

exObj.close() # Close the document

exObj.open(filename)
print exObj.get_value("A10:D10") #Get first column
L = exObj.get_value("A1:C1") #Get first row
for i, v  in enumerate(L): #modify first row  
    L[i] = v.upper()  
print L
exObj.set_value("A1:C1",L) #write first row
### 4. add to use L to set the values of the first three rows of the 5th column to A, B, and C


filename = filename[:-5] + "out.xlsx"
exObj.save_as(filename, True)
exObj.close()
exObj.quit() #quits the excel session.  do this last.
