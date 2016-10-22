from mesh import Face
def importOBJ(filename):
    """Loads a Wavefront OBJ file. """
    vertices = []
    faces = []
    for line in open(filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'v':
            v = map(float, values[1:4])
            vertices.append(PVector(v[0],v[1],v[2]))
        elif values[0] == 'f':
            face = Face([])
            for v in values[1:]:
                w = v.split('/')
                node=vertices[int(w[0])-1]
                face.nodes.append(node)
                faces.append(face)
    return faces

class OBJExporter:
    # https://en.wikipedia.org/wiki/Wavefront_.obj_file
    def __init__(self,filePath,fileName):
        self.file = open(filePath+fileName, "w")
        self.file.write("mtllib ./"+fileName+".mtl"+"\n");
        self.fileMTL = open(filePath+fileName+".mtl", "w")
        self.vertexCount=0
        self.materials=set()
        self.vertices={}
        
    def writeFace(self,face):
        # write Face
        faceString="f"
        for p in face.nodes:
            if p in self.vertices:
                faceString+=" "+str(self.vertices[p])
            else:
                self.vertexCount+=1
                faceString+=" "+str(self.vertexCount)
                self.vertices[p]=self.vertexCount
                self.file.write("v "+str(p.x)+" "+str(p.y)+" "+str(p.z)+"\n")        
        faceString+="\n"
        self.file.write(faceString)
    
    def stop(self):
        # end export and save file
        self.file.close()
        for mat in self.materials:
            self.fileMTL.write("newmtl material"+str(mat)+"\n");
            self.fileMTL.write("Kd "+str(red(mat)/255.0)+" "+" "+str(green(mat)/255.0)+" "+str(blue(mat)/255.0)+"\n");
        self.fileMTL.close()
        println("OBJ exported")
        
    def writeMaterial(self,r,g,b):
        # write material as RGB
        rgb=color(r,g,b)
        self.materials.add(rgb)
        self.file.write("usemtl material"+str(rgb)+"\n")
        
    def writeMaterialHD(self,name,dif,amb,spec,transparency):
        # write Material https://en.wikipedia.org/wiki/Wavefront_.obj_file#Basic_materials
        self.file.write("usemtl "+name+"\n")
        self.fileMTL.write("newmtl "+name+"\n");
        self.fileMTL.write("Kd "+str(dif[0])+" "+" "+str(dif[1])+" "+str(dif[2])+"\n");
        self.fileMTL.write("Ka "+str(amb[0])+" "+" "+str(amb[1])+" "+str(amb[2])+"\n");
        self.fileMTL.write("Ks "+str(spec[0])+" "+" "+str(spec[1])+" "+str(spec[2])+"\n");
        self.fileMTL.write("Tr "+str(transparency)+"\n");
    
    def exportFacesWithColors(self,faces):
        for face in faces:
            self.writeMaterial(red(face.color),green(face.color),blue(face.color))
            self.writeFace(face)
        self.stop()
        
def timeStamp():
    # returns a unique filename 
    return str(year()) + str(nf(month(),2)) + str(nf(day(),2)) + "-" + str(nf(hour(),2)) + str(nf(minute(),2)) + str(nf(second(),2))