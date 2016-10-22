intNumBalls = 100

def setup():
    size(1600,900)
    noStroke()
    
    global lstPos, lstSpd, lstRad, lstCol
    lstPos = []
    lstSpd = []
    lstRad = []
    lstCol = []
    print len(lstPos)
    for i in range(intNumBalls):
        # generate random position, speed, radius and color
        vecPos = PVector(random(30,width-30), random(30,height-30))
        vecSpd = PVector(random(-4,4), random(-4,4))
        fltRad = random(10,70)
        col = color(random(255), random(255), random(255))
        # append these to the corresponding list
        lstPos.append(vecPos)
        lstSpd.append(vecSpd)
        lstRad.append(fltRad)
        lstCol.append(col)
    print len(lstPos)

def draw():
    # display
    background(200)
    global lstPos, lstSpd, lstRad, lstCol
    for i in range(len(lstPos)):
        vecPos = lstPos[i]
        fltRad = lstRad[i]
        col = lstCol[i]
        fill(col,200)
        ellipse(vecPos.x, vecPos.y, 2*fltRad, 2*fltRad)
    
    # calculation
    # update positions
    for i in range(len(lstPos)):
        vecPos = lstPos[i]
        vecSpd = lstSpd[i]
        lstPos[i] = vecPos+vecSpd
    
    # check for boundary collision
    for i in range(len(lstPos)):
        vecPos = lstPos[i]
        vecSpd = lstSpd[i]
        fltRad = lstRad[i]
        if vecPos.x<fltRad or vecPos.x>width-fltRad:
            vecSpd.x = vecSpd.x * -1
        if vecPos.y<fltRad or vecPos.y>height-fltRad:
            vecSpd.y = vecSpd.y * -1
        lstSpd[i] = vecSpd
        
    #saveFrame("movie-#####.png")
        
def mousePressed():
    for i in range(len(lstPos)):
        vecMouse = PVector(mouseX, mouseY)
        vecPos = lstPos[i]
        vecBetween = vecPos - vecMouse
        fltRad = lstRad[i]
        fltDist = vecBetween.mag()
        if fltDist <= fltRad:
            print "YOU HIT NUMBER ", i
            del lstPos[i]
            del lstSpd[i]
            del lstRad[i]
            del lstCol[i]
            break
        
def keyPressed():
    if key=='s':
        save("pic.png")
    if key=='m':
        saveFrame("pic-####.png")