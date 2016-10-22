def setup():
    size(1600,900)
    noFill()
    stroke(255,100)
    
    global strProduction, fltLength, fltTheta
    strProduction="F+F"
    fltLength = 200.0
    fltTheta = radians(100)
    print strProduction
    
def draw():
    background(0)
    
    translate(50,50)
    for step in strProduction:
        if step=="F":
            rect(0,0,fltLength,fltLength)
            translate(fltLength,0)
        elif step=="+":
            rotate(fltTheta)
        elif step=="-":
            rotate(-fltTheta)
        elif step=="[":
            pushMatrix()
        elif step=="]":
            popMatrix()
    
def myReplacement():
    global strProduction, fltLength
    strProduction = strProduction.replace("F","F+[F-[F]]-F")
    fltLength = fltLength * 0.6
    print strProduction
    
def keyPressed():
    myReplacement()
    
def mousePressed():
    save("image.png")