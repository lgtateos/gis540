#import modules
import os, random
#import rpy2 module
import rpy2.robjects as robjects
#set r as working variable to call robjects
r = robjects.r

#set output file name as full path
outputPlot="C:/Temp/normalPlot.png"

#open graphic device
rPNGplot=robjects.r.png
rPNGplot(outputPlot,width=1600,height=1200)

#create normal distribution
## x and y can also be given as Python lists of numbers.
## To create the blue dots, use the Python range function
## to set x and y.
x = r.seq(-4,4,length=200) 
y = r.dnorm(x,mean=0,sd=1)

#create plot
## connects the points with a red line (type='l') 4 pixels wide
## type = 'p' plots points, not a line.
r.plot(x,y,type="l",ann="FALSE",col="red",lwd=4)

#close graphic device
closeFile=robjects.r["dev.off"]
closeFile()
