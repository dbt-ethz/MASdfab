class DXFRecorder:
    def __init__(self,applet):
        self.isRecording=False
        self.hasFile=False
        self.applet=applet
        self.dxf=None
        self.fileName=None
    def setFile(self,fileName):
        self.hasFile=True
        self.fileName=fileName
    def startRecording(self):
        self.dxf=self.applet.beginRaw(DXF, self.fileName)
        self.applet.camera()
        self.isRecording=True
    def layer(self,i):
        if self.isRecording:
            self.applet.flush()
            self.dxf.setLayer(i)
    def stopRecording(self):
         self.isRecording=False
         self.applet.endRaw()
         self.hasFile=False
    def timeStamp(self):
        return str(year()) + str(nf(month(),2)) + str(nf(day(),2)) + "-" + str(nf(hour(),2)) + str(nf(minute(),2)) + str(nf(second(),2))
    