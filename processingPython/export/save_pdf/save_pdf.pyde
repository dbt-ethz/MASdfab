add_library('pdf')

def setup():
    size(800,450)
    beginRecord(PDF, "filename.pdf")
    background(255,255,0)
    
def draw():
    line(width-mouseY,height-mouseX,mouseX,mouseY)

def keyPressed():
    endRecord()