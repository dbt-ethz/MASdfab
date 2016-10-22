add_library('hdgeom')
add_library('controlP5')
add_library('peasycam')
import display as dsp
import gui

def setup():
    global cam,path,fileName,cp5,listener
    size(1200, 760, P3D)
    cam = PeasyCam(this, 400)
    cp5 = ControlP5(this)
    cp5.addListener(Listener() )
    cp5.addCallback(ButtonListener())
    gui.guiInit(cp5)
    path="/Users/dillenburger_b/Documents/Code/SketchesProcessing/sketch_Subdivision1511/data/"
    fileName="panel.obj"
    path=sketchPath("")+"/data/"
    initImages()
    reset()
    
def fixBounds():
    box=mesh.getBounds()
    box.offset(-0.01)
    box.z1-=0.02
    box.z2+=0.02
    for face in mesh.faces:
        center=face.getCenter()
        if box.contains(center)==False:
            face.fix=True
    for v in mesh.nodes:
         if box.contains(center)==False:
            v.fix=True
   
        
def getBrightnessValues(img):
    bixels=[]
    for p in img.pixels:
        bixels.append(brightness(p))
    return bixels

def initImages():
    println("init images...")
    global images,imgValues
    images=[loadImage(path + "masks/mask1.jpg"),loadImage(path + "masks/mask2.jpg"),loadImage(path + "masks/mask3.jpg"),loadImage(path + "masks/mask4.jpg")]
    imgValues = []
    for img in images:
        imgValues.append(getBrightnessValues(img))
   

def updateShape():
    global transformation,mh,shapeToDraw
    println("numVertices: " + str(mesh.getNumVertices()))
    println("updating histograms...")
    mh = MeshHistograms(mesh)
    println("histograms updated...")
    println("updating shape...")
    if (gui.display.getValue() == 8):
        shapeToDraw= dsp.shapeHiddenLine(mesh)
    elif (gui.display.getValue()>0 and gui.display.getValue()<=7):
        h=getHistogram(gui.display.getValue()-1)
        shapeToDraw= dsp.shapeHistogram(h,mesh)
    else:
        shapeToDraw= dsp.shapeWhite(mesh)
        println("shape updated...")
    bds = mesh.getBounds()
    transformation = PMatrix3D()
    scale = 300.0/ bds.getMaxDimension()
    transformation.scale(scale)
    transformation.translate(-bds.getCenterX(), -bds.getCenterY(),-bds.getCenterZ())

def timestamp():
    return str(year()) + str(nf( month(), 2)) +  str(nf( day(), 2)) + "-"  +  str(nf( hour(), 2)) +  str(nf( minute(), 2)) +   str(nf( second(), 2))

def getMeshFunction(cp5,name):
    functionRadio=cp5.getGroup(name+"FunctionRadio")
    if (functionRadio.getValue()==0):
        funct=MeshFunctionConstant()
        funct.constant=cp5.getController(name+"Constant").getValue()
        return funct
    elif (functionRadio.getValue()==1):
       range=cp5.getController(name+"ImageRange")  
       funct=MeshFunctionMap() 
      
       imageRadio=cp5.getGroup(name+"ImageRadio")  
       index=int(imageRadio.getValue())
       funct.setMask(imgValues[index],images[index].width,images[index].height);  
       funct.bounds=mesh.getBounds()
       funct.bounds.offset(funct.bounds.getMaxDimension()*0.01)
       funct.target1=range.getLowValue()
       funct.target2=range.getHighValue()
       return funct  
    elif (functionRadio.getValue()==2):
       range=cp5.getController(name+"HistoRange")  
       li=cp5.getController(name+"Histo")  
       funct=MeshFunctionRange()  
       funct.targetMin=range.getLowValue()  
       funct.targetMax=range.getHighValue()  
       println("list value: "+str(li.getValue()))  
       funct.histogram=getHistogram(li.getValue())
       return funct  
    else:
        sinus=SinusFunction()  
        sinus.offset=cp5.getValue(name+"ruleOffset")  
        sinus.amplitude=cp5.getValue(name+ "Amplitude")  
        sinus.frequency=cp5.getValue(name+"Frequency")  
        sinus.phase=cp5.getValue(name+"Phase")  
        funct=MeshFunctionSine()  
        funct.function=sinus  
        li=cp5.getController(name+"Sinus")  
        println(name+"Sinus")
        println("list value: "+str(li.getValue()))  
        funct.histogram=getHistogram(li.getValue())
        return funct
    
def getHistogram(value):
    global mh
    if (value == 0):return mh.area
    if (value == 1):return mh.perimeter
    if (value == 2):return mh.curvature
    if (value == 3):return mh.planarity
    if (value== 4):return mh.horizontality
    if (value== 5):return mh.verticality
    if (value== 6):return mh.zPos
    return None

def reset():
    global mesh,history
    history=[]
    println("start load")
    mesh = Mesh(path + fileName)
    mesh.constructTopology()
    fixBounds()
    updateShape()

def export():
    stamp = timestamp()
    mesh.saveOBJ(path + "output/export" + stamp + ".obj")
    saveFrame(path+"output/screenshot" + stamp + ".png")

def undo():
    global mesh
    if (len(history)<1):
        return
    mesh=history[len(history)-1]
    history.pop()
    updateShape()

def backupMesh():
    history.append(mesh.getCopy())

def draw():
    if (mouseX < 300 and mouseY < 500):
        cam.setActive(False)
    else:
        cam.setActive(True)
    hint(ENABLE_DEPTH_TEST)
    background(0)
    if (gui.display.getValue()==0):
        ambient(100)
        pointLight(200,205,205,-350,-350,-350)
        pointLight(202,203,205,350,350,350)
    applyMatrix(transformation)
    shape(shapeToDraw)
    hint(DISABLE_DEPTH_TEST)
    cam.beginHUD()
    noLights()
    noStroke()
    fill(0, 100)
    rect(0, 0, 320, 260)
    cp5.draw()
    cam.endHUD()


def keyPressed():
    println("key"+key)
    if (key == 'u'):
        undo()
    if (key == 'r'):
        reset()
    if (key == 'e'):
        export()

class ButtonListener(CallbackListener):
    def controlEvent(self, theEvent):
        global mesh,cp5
        controller=theEvent.getController()
        name=str(controller.getName());
        if theEvent.getAction()==ControlP5.ACTION_RELEASE:
            if (name=="reset"):
                reset()
            if (name=="export"):
                export()
            if (name=="undo"):
                undo()
            if (name=="catmullReset"):
                cp5.getController("nodeMove").setValue(0)
                cp5.getController("edgeMove").setValue(0)
                cp5.getController("faceMove").setValue(0)
            if (name.startswith("rule")):
                backupMesh()
                if (name=="ruleLaplace"):
                    FilterLaplacianSmooth.laplacianSmooth(mesh, 1)
                elif (name=="ruleCatmull"):
                    smooth = RuleCatmull()
                    mesh = smooth.replace(mesh, gui.sliderNodeMove.getValue(), gui.sliderEdgeMove.getValue(), gui.sliderFaceMove.getValue())
                elif (name=="ruleSplit"):
                    split = RuleSplit()
                    mesh = split.replace(mesh)
                elif (name=="ruleWavesVertical"):
                    rule = RuleMoveVertex()
                    rule.waveVerticesVertical(mesh, gui.sliderAmplitudeVer.getValue(), int(gui.sliderFrequenceVer.getValue()))
                elif (name=="ruleWavesHorizontal"):
                    rule = RuleMoveVertex()
                    rule.waveVerticesHorizontal(mesh, gui.sliderAmplitudeHor.getValue(), int(gui.sliderFrequenceHor.getValue()))
                elif (name=="ruleTapered"):
                    t = cp5.getController("taperedClose")
                    t2 = cp5.getController("taperedPyramide")
                    rule = RuleTapered(getMeshFunction(cp5,"taperedOffset"), getMeshFunction(cp5,"taperedExtrude"), getMeshFunction(cp5,"taperedMask"))
                    rule.closed = t.getState()
                    rule.pyramide = t2.getState()
                    mesh = rule.replace(mesh)
                elif (name=="ruleTranslate"):
                    rule = RuleTranslate()
                    rule.function = getMeshFunction(cp5,"translate")
                    rule.translate(mesh)
                elif (name=="ruleOffset"):
                    rule = RuleOffset()
                    rule.offset(mesh, gui.sliderOffset.getValue(), True)
                updateShape()

class Listener(ControlListener):
    def controlEvent(self, theEvent):
        global mesh,cp5
        if (theEvent.isGroup()):
            if (theEvent.getGroup().getName()=="Display"):
                updateShape()
        else:
            name = str(theEvent.getName())
            if (name=="Display"):
                updateShape()