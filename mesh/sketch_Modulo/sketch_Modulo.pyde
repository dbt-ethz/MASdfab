def setup():
    size(800,450)
    
def draw():
    nColumns=20
    nRows=10
    rectWidth=width/nColumns
    rectHeight=height/nRows
    for i in xrange(nColumns):
        for j in xrange(nRows):
            red=255
            green=255
            blue=255
            if i%4==0:
                red=0
            if j%3==0:
                green=0
            if j%5==0:
                blue=0
            fill(red,green,0)
            rect(i*rectWidth,j*rectHeight,rectWidth,rectHeight)