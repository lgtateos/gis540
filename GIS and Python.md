# GIS and Python

ArcMap is a GIS for visualizing and analyzing data.

Open ArcMap ![ArcMap][https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwirks-cppjhAhXLmOAKHUTuBcwQjRx6BAgBEAU&url=https%3A%2F%2Flibrary.columbia.edu%2Fservices%2Fresearch-data-services%2Fsoftware.html&psig=AOvVaw2RG4tLXEaxLPhBdHs9dm78&ust=1553431704290516]

## 1. Play with Python in a GIS
Open the Python Window in ArcMap

![Python Window][https://lgtateos.github.io/gis540/images/pythonWindow.png]

  Type each of the following lines of code at the Python prompt and observe the result:

```Python

print('Hello')

5 + 6

x = 5

print(x)

x  
```
## 2. Add a basemap

1. Click the "Add Data" button.
![Add data][http://sandbox.idre.ucla.edu/sandbox/wp-content/uploads/2015/05/addData.png]

2. Select "Add Basemap"

3. Select "National Geographic"

## 3. Add points to the map.
Now we're going to map geotagged photos.  

2. 1. First, we need to tell Python where the images are.  Copy the following into the Python Window and hit Enter:

```Python
myPicFolder = "C:/gispy/scratch/EnchantedForest/"
```
2. Then we can call an ArcGIS tool "GeoTagged Photos to Points".   Copy the following into the Python Window and hit Enter:
```Python
arcpy.GeoTaggedPhotosToPoints_management(myPicFolder)
```
3. Do you see any new points?  Look for the new layer in the table of contents.  Right click on the layer and select "Zoom to layer"
4. Cick the identify button
  ![Identify button][https://lh3.googleusercontent.com/-ztcqPC8oNow/TgOD7SiaZ9I/AAAAAAAABT0/BLUKIKVP8aI/s800/identify-attachments.jpg]
5. Click on the name of the image in the identify box.  The image will open.


## 4. Add points to the map.

1. Now add a lot more photos from different folders all at once. Copy the following into the Python Window and hit Enter:
```Python
import os

myFolder = "C:/gispy/scratch/chile/"

myDirs = os.listdir(myFolder)

for d in myDirs:
    arcpy.GeoTaggedPhotosToPoints_management(myFolder + d)
```