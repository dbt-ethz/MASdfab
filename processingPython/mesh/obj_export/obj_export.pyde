add_library('OBJExport')

def setup():
    size(800,450,P3D)
    noLoop()
    beginRecord('nervoussystem.obj.OBJExport', 'mymesh.obj')
    
def draw():
    background(0)
    box(100)
    
    endRecord()