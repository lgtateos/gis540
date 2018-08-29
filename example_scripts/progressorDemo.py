# Demonstration script showing examples of using the progressor
#  Parameters:
#   n - number to count to (a good first choice is 10)
#   p - interval to count by (a good first choice is 1)
# The various time.sleep() calls are just to slow the dialog down
#  so you can view messages and progressor labels.
#
import arcpy
import time

n = int(arcpy.GetParameterAsText(0))
p = int(arcpy.GetParameterAsText(1))

readTime = 2.5 # Pause to read what's written on dialog
loopTime = 0.3 # Loop iteration delay

arcpy.AddMessage("Running demo with: " + str(n) + " by " + str(p))

# Start by showing the default progress dialog, where the
#  progress bar goes back and forth. Note how the progress label
#  mimics working through some "phases", or chunks of work that
#  a script may perform.
#
arcpy.SetProgressor("default", "This is the default progressor")
time.sleep(readTime)



for i in range(3):
  arcpy.SetProgressorLabel("Working on \"phase\" " + str(i + 1))
  arcpy.AddMessage("Messages for phase " + str(i+1))
  time.sleep(readTime)
arcpy.AddMessage("-------------------------")

# Setup the progressor with its initial label, min, max, and interval
#
arcpy.SetProgressor("step", "Step progressor: Counting from 0 to " + str(n), 0, n, p)
time.sleep(readTime)

# Loop issuing a new label when the increment is divisible by the
#  value of countBy (p). The "%" is python's modulus operator - we
#  only update the position every p'th iteration
#
for i in range(n):
  if (i % p) == 0:
    arcpy.SetProgressorLabel("Iteration: " + str(i))
    arcpy.SetProgressorPosition(i)
    time.sleep(loopTime)

# Update the remainder that may be left over due to modulus operation
#  
arcpy.SetProgressorLabel("Iteration: " + str(i+1))
arcpy.SetProgressorPosition(i+1)

arcpy.AddMessage("Done counting up")
arcpy.AddMessage("-------------------------")
time.sleep(readTime)

# Just for fun, make the progressor go backwards.
#
arcpy.SetProgressor("default", "Default progressor: Now we'll do a countdown")
time.sleep(readTime)
arcpy.AddMessage("Here comes the countdown...")
arcpy.SetProgressor("step", "Step progressor: Counting backwards from " + str(n), 0, n, p)
time.sleep(readTime)
arcpy.AddMessage("Counting down now...")

for i in range(n, 0, -1):
  if (i % p) == 0:
    arcpy.SetProgressorLabel("Iteration: " + str(i))
    arcpy.SetProgressorPosition(i)
    time.sleep(loopTime)

# Update for remainder
#
arcpy.SetProgressorLabel("Iteration: " + str(i-1))
arcpy.SetProgressorPosition(i-1)
time.sleep(readTime)    
arcpy.AddMessage("-------------------------")
arcpy.AddMessage("All done")
arcpy.ResetProgressor()