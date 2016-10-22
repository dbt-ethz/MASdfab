# parameters to play with:
# the initial lines can be changed
#the color,position, length, amount, angle and radius of the branches can be variated
 

def setup():
    global maxGenerations,doExport
    doExport=False
    maxGenerations=8
    size(800,450)
    background(0)

def draw():
    global doExport
    # adjusting the graphics
    noStroke()
    fill(0,10)
    rect(0,0,width,height)
    stroke(255) 
    # the initial lines for starting the recursion
    translate(width*0.5,0)
    drawLine(height,1)
    if doExport:
        saveFrame(timeStamp()+".png")
        println("frame saved")
        doExport=False
  
# recursion
def drawLine(extrude,generation):
    # draws the line as an extruded polygon
    stroke(255,255-generation*20)
    println(str(maxGenerations-generation)) 
    strokeWeight((maxGenerations-generation)*1)
    line(0,0,0,extrude)
    # increased the counter of the generation
    generation+=1
    # angles of the branches are depending on the mouseposition
    angle=mouseX*PI/width
    newExtrude=extrude*mouseY/height
    # only if we didn't reach the maximum allowed recursion yet, we create a branch
    if (generation<maxGenerations):
        # first branch starts at 0.6 from the previous line
        with pushMatrix():
            translate(0,extrude*0.6)
            rotate(angle)
            drawLine(newExtrude,generation)
        # second branch starts at 0.3 from the previous line
        with pushMatrix():
            translate(0,extrude*0.3)
            rotate(-angle)
            drawLine(newExtrude,generation)

def keyPressed():
    if (key=='e'):doExport=true

def timeStamp():
    return str(year()) + str(nf(month(),2)) + str(nf(day(),2)) + "-" + str(nf(hour(),2)) + str(nf(minute(),2)) + str(nf(second(),2))