import arcpy, BeautifulSoup

arcpy.overwriteOutput = True

filename =  "C:/gispy/data/Ch20/Sample_7_Day_GPS_Data.kml"

#Read the kml file and put contents in BeautifulSoup object
data = open(filename,'r')
soup = BeautifulSoup.BeautifulSoup(data)
data.close()

#GET kml with name and description tags.
names = soup.findAll("name")
descriptions = soup.findAll("description")

class kmlPoint():
	def __init__(self):
		self.name = ""
		self.date = ""
		self.time = ""
		self.x = 0
		self.y = 0
		self.z = 0
	def parseDescription(self, descriptionList):
		'''Parse a point description '''
		#Description looks like: [u'Date: 01/18/2012', <br />, u'Time: 02:28:23 PM']
		try:
			#Get the date
			date = descriptionList[0].split(":")
			self.date = date[1].strip()
			#Get the time
			time = descriptionList[2]
			time = time.lower()
			time = time.replace("time:","")
			self.time = time.strip()
		except:
			print
			print "Data in {0} has an incomplete description: {1}".format(self.name,description.contents)

	def parsePoint(self, coord):
		'''Parse the coordinate values from  -78.67717,35.781952,0'''
		# coord is a comma delimited string. Split the coord on comma!
		# Set each (self.x, self.y, self.z) with the split results.
		###Set the point's x, y, and z coordinate values
		print self.y,self.x,self.z

#Parse Placemarks
### Find all the placemarks in the soup and put the results in a variable named placesmarks.

pointList = []
for placemark in placemarks:
	#Check if the placemark contains a point or a linestring.
	pointSoup = placemark.find("point")
	if pointSoup:
		print "point"
		mypoint = kmlPoint()
		#point placemarks look like this:
		#<placemark> <name>Stop #30</name><styleurl>#normalPlacemark</styleurl> <description>Date: 01/18/2012<br />
		#Time: 02:28:23 PM</description> <point> <coordinates> -78.67717,35.781952,0</coordinates> </point> </placemark>
		mypoint.name = placemark.find("name").contents[0]
		mypoint.parseDescription(placemark.find("description").contents)

		#pointSoup looks like this: [<point> <coordinates> -78.67717,35.781952,0</coordinates> </point>]
		coords = placemark.find("coordinates").contents[0]
		mypoint.parsePoint(coords)
		pointList.append(mypoint)


# Create output shapefiles
fc = "stops.shp"
mydir = "C:/gispy/scratch/"
arcpy.env.workspace = mydir
arcpy.overwriteOutput = True
if arcpy.Exists(fc):
	arcpy.Delete_management(fc)
	
sr = arcpy.SpatialReference('WGS 1984')
### Create a POINT feature class in mydir named fc with spatial reference sr.

#Add fields
textFieldNames = [ 'SHAPE@XY', 'Name', 'Date', 'Time']
###Loop through the fields in the fieldnames list
	###Add text fields for each field name in the list (use the AddFields tool)

fieldnames = [ 'SHAPE@XY'] + textFieldNames
# Insert kml points into point shapefile #
try:
	#Prepare for writing to file. Create insert cursor object.
	###Create an insert cursor named ic. Use the field name list that includes the shape token!!

	#Loop through the point list and create a new record for each.
	print "---Adding entries to the {0}{1}---".format(mydir, fc)
	for currPoint in pointList:
		print '---Adding row {0} to the feature class.---'.format(currPoint.name)
		#Set the point coordinate
		pnt = arcpy.Point( mypoint.x, mypoint.y, mypoint.z )
		###Set the row lists's Shape, Name, Date, and Time field values. (starts out like row = [pnt, currPoint.name, ,...)
		###Insert the row into the table using the insert cursor 'insertRow' method.
	del ic
except:
	del ic