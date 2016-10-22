add_library('controlP5')
add_library('peasycam')
add_library('hdgeom')

def setup():
    size(1200,850,P3D)
    cam=PeasyCam(this,200)
    
def construct():
    global voxelSpace,voxelShape,iso,nX,nY,nZ
    nX=100
    nY=70
    nZ=20
    iso=0.5
    voxelSpace=VoxelSpace(nX,nY,nZ)
    fX=SineFunction(50,1,5)
    fY=SineFunction(40,1,2)
    fZ=SineFunction(5,1,frameCount*1.0/10)
    for i in range(len(voxelSpace.values)):
        x=voxelSpace.getX(i)*1.0/nX
        y=voxelSpace.getY(i)*1.0/nY
        z=voxelSpace.getZ(i)*1.0/nZ
        v=fX.getValue(x)+fY.getValue(y*y)+fZ.getValue(z)+x
        voxelSpace.set(i,v)
    voxelSpace.setValueToBorders(0)
    noStroke()
    fill(255)
    voxelShape=voxelSpace.getPShape(this,iso)

def draw():
    construct()
    background(0)
    translate(-nX/2,-nY/2,-nZ/2)
    lights()
    shape(voxelShape)
    
def keyPressed():
    if (key=='e'):
        voxelShape.saveMCube(iso, "/Users/dillenburger_b/Desktop/t200.obj")
        voxelShape.saveObjQUADS(iso, "/Users/dillenburger_b/Desktop/t100.obj")
        
class SineFunction():
    def __init__(self,frequency,amplitude,phase):
        self.amplitude=amplitude
        self.frequency=frequency
        self.phase=phase
    def getValue(self,input):
        return sin(input*self.frequency+self.phase)*self.amplitude
    