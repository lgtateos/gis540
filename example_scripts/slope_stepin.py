#Purpose: find slope of line from (x,y) to (a,b)
def findSlope(x1, y1, x2, y2):
    rise = Y2 - Y1
    run = x2 - x1
    slope = rise/run  
    return slope

#Set points (x,y) and (a,b)
x = 0
y = 3
a = 2
b = 2

#Find the slope
mySlope = findSlope(x, y, a, b)
print mySlope