add_library('dxf')
add_library('peasycam')
from DXFRecorder import DXFRecorder

def setup():
    size(800,450,P3D)
    cam=PeasyCam(this,600)
    global dxfRecorder
    dxfRecorder=DXFRecorder(this)
    
def draw():
    background(0)
    if dxfRecorder.hasFile:
        dxfRecorder.startRecording()
    dxfRecorder.layer(2)
    fill(255,0,0)
    box(500,100,100)
    dxfRecorder.layer(3)
    fill(0,255,0)
    box(100,100,500)
    if dxfRecorder.isRecording:
        dxfRecorder.stopRecording()

def keyPressed():
    dxfRecorder.setFile(dxfRecorder.timeStamp()+".dxf")