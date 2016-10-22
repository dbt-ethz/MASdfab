
def guiInit(cp5):
    global sliderFaceMove,sliderNodeMove,sliderEdgeMove
    global sliderFrequenceVer,sliderFrequenceHor,sliderAmplitudeVer,sliderAmplitudeHor
    global sliderOffset
    global display
    
    println("init GUI...") 
 
    cp5.addButton("export").setPosition(width - 100, 20)
    cp5.addButton("reset").setPosition(width - 100, 40) 
    cp5.addButton("undo").setPosition(width - 100, 60) 
    groupLaplace = cp5.addGroup("laplaceGroup").setBackgroundColor(20) 
    cp5.addButton("ruleLaplace").setPosition(10, 10).moveTo(groupLaplace).setCaptionLabel("APPLY") 
    groupSplit = cp5.addGroup("splitGroup").setBackgroundColor(20) 
    cp5.addButton("ruleSplit").setPosition(10, 10).moveTo(groupSplit).setCaptionLabel("APPLY") 
    groupTapered = cp5.addGroup("tapered").setBackgroundColor(20).setBackgroundHeight(560) 
    
    # create a toggle
    cp5.addToggle("taperedClose").setPosition(10,10).setSize(10,10).moveTo(groupTapered) 
    cp5.addToggle("taperedPyramide").setPosition(100,10).setSize(10,10).moveTo(groupTapered)  
    
    offsetFunction=guiConstructParameterGroup(cp5,"taperedOffset") 
    offsetFunction.disableCollapse() 
    offsetFunction.setPosition(0, 50) 
    offsetFunction.moveTo(groupTapered) 
    
    taperedFunction=guiConstructParameterGroup(cp5,"taperedExtrude") 
    taperedFunction.disableCollapse() 
    taperedFunction.setPosition(0, 210) 
    taperedFunction.moveTo(groupTapered) 
    
    maskFunction=guiConstructParameterGroup(cp5,"taperedMask") 
    maskFunction.disableCollapse() 
    maskFunction.setPosition(0, 370) 
    maskFunction.moveTo(groupTapered) 
    
    cp5.addButton("ruleTapered").setPosition(10, 530).setGroup(groupTapered).setCaptionLabel("APPLY") 
  
    groupOffset = cp5.addGroup("offsetGroup").setBackgroundColor(20) 
    sliderOffset= cp5.addSlider("offsetValue").setPosition(10, 10).setRange(-1,1).moveTo(groupOffset) 
    cp5.addButton("ruleOffset").setPosition(10, 30).moveTo(groupOffset).setCaptionLabel("APPLY") 
  
    groupCatmull = cp5.addGroup("catmullRule").setBackgroundColor(20).setBackgroundHeight(120) 
    
    sliderFaceMove= cp5.addSlider("faceMove").setPosition(10, 10).setRange(-1, 1).moveTo(groupCatmull) 
    sliderEdgeMove= cp5.addSlider("edgeMove").setPosition(10, 20).setRange(-1, 1).moveTo(groupCatmull) 
    sliderNodeMove=cp5.addSlider("nodeMove").setPosition(10, 30).setRange(-1, 1).moveTo(groupCatmull) 
    
    cp5.addButton("catmullReset").setPosition(10, 50).moveTo(groupCatmull).setCaptionLabel("Reset") 
    cp5.addButton("ruleCatmull").setPosition(10, 80).moveTo(groupCatmull).setCaptionLabel("APPLY") 
    
    groupWavesV = cp5.addGroup("ruleWavesVerticalRule").setBackgroundColor(20) 
    sliderFrequenceVer=cp5.addSlider("frequenceVer").setPosition(10, 10).setRange(2, 128).moveTo(groupWavesV) 
    sliderAmplitudeVer=cp5.addSlider("amplitudeVer").setPosition(10, 20).setRange(-1, 1).moveTo(groupWavesV) 
    cp5.addButton("ruleWavesVertical").setPosition(10, 40).moveTo(groupWavesV).setCaptionLabel("APPLY") 
  
    groupWavesH = cp5.addGroup("ruleWavesHoriztontalRule").setBackgroundColor(20) 
    sliderFrequenceHor= cp5.addSlider("frequenceHor").setPosition(10, 10).setRange(2, 128).moveTo(groupWavesH) 
    sliderAmplitudeHor=cp5.addSlider("amplitudeHor").setPosition(10, 20).setRange(-1, 1).moveTo(groupWavesH) 
    cp5.addButton("ruleWavesHorizontal").setPosition(10, 40).moveTo(groupWavesH).setCaptionLabel("APPLY") 
    
    groupTranslate = cp5.addGroup("translateGroup").setBackgroundColor(20).setBackgroundHeight(200) 
    translateGroup = guiConstructParameterGroup(cp5,"translate") 
    translateGroup.disableCollapse().moveTo(groupTranslate).setPosition(10,20) 
    cp5.addButton("ruleTranslate").setPosition(10, 170).setGroup(groupTranslate).setCaptionLabel("APPLY") 
    
    acc=cp5.addAccordion("acc").setPosition(20, 40).setWidth(220)
    acc.addItem(groupLaplace).addItem(groupSplit)
    acc.addItem(groupTapered)
    acc.addItem(groupOffset)
    acc.addItem(groupCatmull)
    acc.addItem(groupWavesV)
    acc.addItem(groupWavesH)
    acc.addItem(groupTranslate) 
    display = cp5.addDropdownList("Display")
    display.setPosition(20, 30)
    display.setWidth(220)
    display.addItems( [ "none", "Area", "Perimeter","Curvature", "Planarity", "Horizontality","Verticality","ZPos", "Hidden Line" ]) 
    display.setBackgroundColor(255) 
    display.bringToFront() 
    display.setOpen(False)
    cp5.setAutoDraw(False) 
  
def guiHistogramList(cp5,name):
    histoList=cp5.addDropdownList(name).addItems([ "Area", "Perimeter", "Curvature","Planarity", "Horizontality", "Verticality","ZPos" ])
    histoList.setCaptionLabel("Histogram").setBackgroundColor(255).setOpen(False)
    return histoList

def guiConstructParameterGroup(cp5,name):
    parameterGroup = cp5.addGroup(name) 
    parameterGroup.setBackgroundColor(20) 
    parameterGroup.setBackgroundHeight(185) 
    r = cp5.addRadioButton(name+"FunctionRadio").setPosition(10, 0)
    r.setSize(10, 10).setColorForeground(color(120))
    r.setColorActive(color(255)).setItemsPerRow(1)
    r.setSpacingColumn(10).setSpacingRow(5).addItem(name+"50", 0)
    r.addItem(name+"100", 1).addItem(name+"150", 2).addItem(name+"250", 3) 
    r.getItem(0).setPosition(0,10) 
    r.getItem(1).setPosition(0,30) 
    r.getItem(2).setPosition(0,60) 
    r.getItem(3).setPosition(0,90) 
    r.hideLabels() 
    r.moveTo(parameterGroup) 
    
    cp5.addSlider(name+"Constant").setPosition(25, 10).setGroup(parameterGroup).setRange(-1, 1).setCaptionLabel("Constant") 
    
    ir=cp5.addRadioButton(name+"ImageRadio").setPosition(25, 30).setSize(10, 10).setColorForeground(color(120)).setColorActive(color(255))
    ir.setItemsPerRow(6).setSpacingColumn(15).addItem(name+"1", 0)
    ir.addItem(name+"2", 1).addItem(name+"3", 2).addItem(name+"4", 3).setGroup(parameterGroup) 
    cp5.addRange(name+"ImageRange").setPosition(25, 40).setGroup(parameterGroup).setRange(-1, 1).setCaptionLabel("Range") 
    ir.hideLabels() 
    # HistoRange
    list1=guiHistogramList(cp5,name+"Histo").setPosition(25, 60).setGroup(parameterGroup)
    cp5.addRange(name+"HistoRange").setPosition(25, 70).setGroup(parameterGroup).setRange(-1, 1).setCaptionLabel("Range") 
    # HistoSinus
    list2=guiHistogramList(cp5,name+"Sinus").setPosition(25, 90).setGroup(parameterGroup) 
    cp5.addSlider(name + "Amplitude").setPosition(25, 100).setGroup(parameterGroup).setCaptionLabel("Amplitude").setRange(0, 0.3) 
    cp5.addSlider(name + "Frequency").setPosition(25, 110).setGroup(parameterGroup).setCaptionLabel("Frequency").setRange(0, 50) 
    cp5.addSlider(name + "Phase").setPosition(25, 120).setGroup(parameterGroup).setCaptionLabel("Phase").setRange(0, 4) 
    cp5.addSlider(name + "ruleOffset").setPosition(25, 130).setGroup(parameterGroup).setCaptionLabel("ruleOffset").setRange(-1, 1) 
    list2.bringToFront() 
    list1.bringToFront() 
    return parameterGroup 