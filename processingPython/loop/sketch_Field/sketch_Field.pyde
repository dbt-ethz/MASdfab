add_library('pdf')
def setup():
    global exportPDF,doAnimation
    size(800,450)
    smooth()
    rectMode(CENTER)
    exportPDF=False
    doAnimation=False

def draw():
    global exportPDF,doAnimation
    if exportPDF==True:
        beginRecord(PDF,"myPDF.pdf")
    background(0)
    drawGrid()
    if exportPDF==True:
        endRecord()
        exportPDF=False
        println("exported")
    if doAnimation:
        saveFrame("test-######.png")

def keyPressed():
    global exportPDF
    println(key)
    if key=='e':
        exportPDF=True
    if key=='a':
        doAnimation=!doAnimation
        println("is recording: " + doAnimation)
    
def drawGrid():
    nX=30;
    nY=10;
    dimX=width/nX;
    dimY=height/nY;
    noFill();
    stroke(255);
    for y in xrange(nY):
        for x in xrange(nX):
            pushMatrix()
            posX=x*dimX+dimX*0.5;
            posY=y*dimY+dimY*0.5;
            distToMouse=dist(posX,posY,mouseX,mouseY);
            translate(posX,posY);
            rotate(distToMouse/200.0);
            ellipse(0,0,distToMouse,dimY-4);
            popMatrix();