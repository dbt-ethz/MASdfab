def shapeHiddenLine(mesh):
    shape = createShape(PApplet.GROUP)
    tris = createShape()
    tris.beginShape(PApplet.TRIANGLES)
    tris.fill(0)
    tris.stroke(255)
    colorMode(PApplet.RGB, 255)
    quads = createShape()
    quads.beginShape(PApplet.QUADS)
    quads.fill(0)
    quads.stroke(255)
    for face in mesh.faces:
        s = tris
        if (face.getNumVertices() == 4):
            s = quads
        for v in face.nodes:
            s.vertex(v.x, v.y, v.z)
    tris.endShape()
    shape.addChild(tris)
    quads.endShape()
    shape.addChild(quads)
    return shape
  
def shapeWhite(mesh):
    colorMode(PApplet.RGB, 255)
    shape = createShape(PApplet.GROUP)
    tris = createShape()
    tris.beginShape(PApplet.TRIANGLES)
    tris.noStroke()
    tris.fill(255)
    quads = createShape()
    quads.beginShape(PApplet.QUADS)
    quads.noStroke()
    quads.fill(255)
    for face in mesh.faces:
        s = tris
        if (face.getNumVertices() == 4):
            s = quads
        for v in face.nodes:
            s.vertex(v.x, v.y, v.z)
    tris.endShape()
    shape.addChild(tris)
    quads.endShape()
    shape.addChild(quads)
    return shape
  
def shapeHistogram(h,mesh):
    shape = createShape(PApplet.GROUP)
    tris = createShape()
    # tris.colorMode(PApplet.HSB, 255)
    tris.beginShape(PApplet.TRIANGLES)
    quads = createShape()
    quads.beginShape(PApplet.QUADS)
    quads.colorMode(PApplet.HSB, 255)
    colorMode(PApplet.HSB, 255)
    for face in mesh.faces:
        s = tris
        if (face.getNumVertices() == 4):
            s = quads
        face.col=color(h.map(h.values[face.id], 0, 255), 255, 255)
        s.fill(h.map(h.values[face.id], 0, 255), 255, 255)
        for v in face.nodes:
            s.vertex(v.x, v.y, v.z)
    tris.endShape()
    shape.addChild(tris)
    quads.endShape()
    shape.addChild(quads)  
    return shape