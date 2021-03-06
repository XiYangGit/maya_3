# randomNode.py
#   Produces random locations to be used with the Maya instancer node.

import sys
import random

import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as cmds
import maya.mel as mel

# Useful functions for declaring attributes as inputs or outputs.
def MAKE_INPUT(attr):
    attr.setKeyable(True)
    attr.setStorable(True)
    attr.setReadable(True)
    attr.setWritable(True)
def MAKE_OUTPUT(attr):
    attr.setKeyable(False)
    attr.setStorable(False)
    attr.setReadable(True)
    attr.setWritable(False)

# Define the name of the node
rkPluginNodeTypeName = "randomNode"

# Give the node a unique ID. Make sure this ID is different from all of your
# other nodes!
randomNodeId = OpenMaya.MTypeId(0x8705)

# Node definition
class randomNode(OpenMayaMPx.MPxNode):
    # Declare class variables:
    # TODO:: declare the input and output class variables
    #         i.e. inNumPoints = OpenMaya.MObject()
    inNumPoints=OpenMaya.MObject()
    minBound=OpenMaya.MVector()
    maxBound=OpenMaya.MVector()
    pointList=OpenMaya.MObject()
    #idList=OpenMaya.MObject()
    #pointList=pointsAAD.vectorArray()
    # constructor
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

    # compute
    def compute(self,plug,data):
        # TODO:: create the main functionality of the node. Your node should 
        #         take in three floats for max position (X,Y,Z), three floats 
        #         for min position (X,Y,Z), and the number of random points to
        #         be generated. Your node should output an MFnArrayAttrsData 
        #         object containing the random points. Consult the homework
        #         sheet for how to deal with creating the MFnArrayAttrsData. 
        numberData=data.inputValue(randomNode.inNumPoints)
        numberpt=numberData.asInt()
        minData=data.inputValue(randomNode.minBound)
        minb=minData.asFloat3()
        maxData=data.inputValue(randomNode.maxBound)
        maxb=maxData.asFloat3()
        pointsData=data.outputValue(randomNode.pointList)
        pointsAAD=OpenMaya.MFnArrayAttrsData()
        pointsObject=pointsAAD.create()
        pointsArray=pointsAAD.vectorArray("position")
        idArray=pointsAAD.doubleArray("id")
        for i in range(0,numberpt):
            posx=random.uniform(minb[0],maxb[0])
            posy=random.uniform(minb[1],maxb[1])
            posz=random.uniform(minb[2],maxb[2])
            pos=OpenMaya.MVector(posx,posy,posz)
            pointsArray.append(pos)
            idArray.append(i)
        pointsData.setMObject(pointsObject)
        data.setClean(plug)
    
# initializer
def rnodeInitializer():
    tAttr = OpenMaya.MFnTypedAttribute()
    nAttr = OpenMaya.MFnNumericAttribute()

    # TODO:: initialize the input and output attributes. Be sure to use the 
    #         MAKE_INPUT and MAKE_OUTPUT functions.
    randomNode.inNumPoints=nAttr.create("Number","num",OpenMaya.MFnNumericData.kLong,10)
    #nAttr.default=10;
    MAKE_INPUT(nAttr)
    randomNode.minBound=nAttr.create("minbound","min",OpenMaya.MFnNumericData.k3Float)
    #nAttr.default=(0,0,0);
    MAKE_INPUT(nAttr)
    randomNode.maxBound=nAttr.create("maxbound","max",OpenMaya.MFnNumericData.k3Float)
    #nAttr.default=(20,20,20);
    MAKE_INPUT(nAttr)
    randomNode.pointList=tAttr.create("randomPoint","pt",OpenMaya.MFnArrayAttrsData.kDynArrayAttrs)
    MAKE_OUTPUT(tAttr)
    #randomNode.idList=tAttr.create("idList","id",OpenMaya.MFnArrayAttrsData.kDynArrayAttrs)
    #MAKE_OUTPUT(tAttr)

    try:
        # TODO:: add the attributes to the node and set up the
        #         attributeAffects (addAttribute, and attributeAffects)
        randomNode.addAttribute(randomNode.inNumPoints)
        randomNode.addAttribute(randomNode.minBound)
        randomNode.addAttribute(randomNode.maxBound)
        randomNode.addAttribute(randomNode.pointList)
        #randomNode.addAttribute(randomNode.idList)
        randomNode.attributeAffects(randomNode.inNumPoints,randomNode.pointList)
        randomNode.attributeAffects(randomNode.minBound,randomNode.pointList)
        randomNode.attributeAffects(randomNode.maxBound,randomNode.pointList)
        print "Initialization!\n"

    except:
        sys.stderr.write( ("Failed to create attributes of %s node\n", kPluginNodeTypeName) )

# creator
def rnodeCreator():
    return OpenMayaMPx.asMPxPtr( randomNode() )


# LSystemNode.py
import LSystem
import math
# Define the name of the node
kPluginNodeTypeName = "LSystemNode"

# Give the node a unique ID. Make sure this ID is different from all of your
# other nodes!
LSystemNodeId = OpenMaya.MTypeId(0x8704)

# Node definition
class LSystemNode(OpenMayaMPx.MPxNode):
    # Declare class variables:
    # TODO:: declare the input and output class variables
    #         i.e. inNumPoints = OpenMaya.MObject()
    defaultAngle=OpenMaya.MObject()
    defaultStepsize=OpenMaya.MObject()
    grammar=OpenMaya.MObject()
    iteration=OpenMaya.MObject()
    branch=OpenMaya.MObject()
    flower=OpenMaya.MObject()
    
    # constructor
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

    # compute
    def compute(self,plug,data):
        # TODO:: create the main functionality of the node. Your node should 
        #         take in three floats for max position (X,Y,Z), three floats 
        #         for min position (X,Y,Z), and the number of random points to
        #         be generated. Your node should output an MFnArrayAttrsData 
        #         object containing the random points. Consult the homework
        #         sheet for how to deal with creating the MFnArrayAttrsData. 
        iterationData=data.inputValue(LSystemNode.iteration)
        iterNum=iterationData.asInt()
        angleData=data.inputValue(LSystemNode.defaultAngle)
        ang=angleData.asFloat()
        stepData=data.inputValue(LSystemNode.defaultStepsize)
        stepsize=stepData.asFloat()
        grammarData=data.inputValue(LSystemNode.grammar)
        gra=grammarData.asString()
        pointsData=data.outputValue(LSystemNode.branch)
        fpointsData=data.outputValue(LSystemNode.flower)
        pointsAAD=OpenMaya.MFnArrayAttrsData()
        fpointsAAD=OpenMaya.MFnArrayAttrsData()
        pointsObject=pointsAAD.create()
        fpointsObject=fpointsAAD.create()
        pointsArray=pointsAAD.vectorArray("position")
        fpointsArray=fpointsAAD.vectorArray("position")
        idArray=pointsAAD.doubleArray("id")
        fidArray=fpointsAAD.doubleArray("id")
        lengthArray=pointsAAD.vectorArray("scale")
        directionArray=pointsAAD.vectorArray("aimDirection")
        axisArray=pointsAAD.vectorArray("aimAxis")
        lsys=LSystem.LSystem()
        lsys.setDefaultAngle(ang)
        lsys.setDefaultStep(stepsize)
        lsys.loadProgramFromString(str(gra))
        braVector=LSystem.VectorPyBranch()
        floVector=LSystem.VectorPyBranch()
        lsys.processPy(iterNum,braVector,floVector)
        for i in range(0,braVector.size()):
            posx=(braVector[i][4]+braVector[i][1])*0.5
            posy=(braVector[i][5]+braVector[i][2])*0.5
            posz=(braVector[i][3]+braVector[i][0])*0.5
            pos=OpenMaya.MVector(posx,posy,posz)
            pointsArray.append(pos)
            idArray.append(i)
            scalei=OpenMaya.MVector(1,stepsize,1)
            lengthArray.append(scalei)
            axisArray.append(OpenMaya.MVector(0,1,0))
            directionx=(braVector[i][4]-braVector[i][1])
            directiony=braVector[i][5]-braVector[i][2]
            directionz=braVector[i][3]-braVector[i][0]
            diri=OpenMaya.MVector(directionx,directiony,directionz)
            diri.normalize()
            directionArray.append(diri)
        pointsData.setMObject(pointsObject)
        for i in range(0,floVector.size()):
            fposx=floVector[i][1]
            fposy=floVector[i][2]
            fposz=floVector[i][0]
            fpos=OpenMaya.MVector(fposx,fposy,fposz)
            fpointsArray.append(fpos)
            fidArray.append(i)
        fpointsData.setMObject(fpointsObject)
            
        data.setClean(plug)
    
# initializer
def nodeInitializer():
    tAttr = OpenMaya.MFnTypedAttribute()
    nAttr = OpenMaya.MFnNumericAttribute()

    # TODO:: initialize the input and output attributes. Be sure to use the 
    #         MAKE_INPUT and MAKE_OUTPUT functions.
    LSystemNode.defaultAngle=nAttr.create("defaultAngle","a",OpenMaya.MFnNumericData.kFloat,30.0)
    MAKE_INPUT(nAttr)
    LSystemNode.defaultStepsize=nAttr.create("defaultStepsize","s",OpenMaya.MFnNumericData.kFloat,10.0)
    MAKE_INPUT(nAttr)
    LSystemNode.iteration=nAttr.create("iteration","i",OpenMaya.MFnNumericData.kLong,2)
    MAKE_INPUT(nAttr)
    LSystemNode.grammar=tAttr.create("grammar","g",OpenMaya.MFnData.kString)
    defaultgrammar=OpenMaya.MFnStringData().create("F\nF->F[+F]F[-F]F*")
    tAttr.setDefault(defaultgrammar)
    MAKE_INPUT(tAttr)
    LSystemNode.branch=tAttr.create("LSystemPoints","pt",OpenMaya.MFnArrayAttrsData.kDynArrayAttrs)
    MAKE_OUTPUT(tAttr)
    LSystemNode.flower=tAttr.create("flowerPoints","f",OpenMaya.MFnArrayAttrsData.kDynArrayAttrs)
    MAKE_OUTPUT(tAttr)

    try:
        # TODO:: add the attributes to the node and set up the
        #         attributeAffects (addAttribute, and attributeAffects)
        LSystemNode.addAttribute(LSystemNode.defaultAngle)
        LSystemNode.addAttribute(LSystemNode.defaultStepsize)
        LSystemNode.addAttribute(LSystemNode.iteration)
        LSystemNode.addAttribute(LSystemNode.grammar)
        LSystemNode.addAttribute(LSystemNode.branch)
        LSystemNode.addAttribute(LSystemNode.flower)
        #LSystemNode.addAttribute(LSystemNode.idList)
        LSystemNode.attributeAffects(LSystemNode.defaultAngle,LSystemNode.branch)
        LSystemNode.attributeAffects(LSystemNode.defaultStepsize,LSystemNode.branch)
        LSystemNode.attributeAffects(LSystemNode.grammar,LSystemNode.branch)
        LSystemNode.attributeAffects(LSystemNode.iteration,LSystemNode.branch)
        LSystemNode.attributeAffects(LSystemNode.defaultAngle,LSystemNode.flower)
        LSystemNode.attributeAffects(LSystemNode.defaultStepsize,LSystemNode.flower)
        LSystemNode.attributeAffects(LSystemNode.grammar,LSystemNode.flower)
        LSystemNode.attributeAffects(LSystemNode.iteration,LSystemNode.flower)
		
        print "Initialization!\n"

    except:
        sys.stderr.write( ("Failed to create attributes of %s node\n", kPluginNodeTypeName) )

# creator
def nodeCreator():
    return OpenMayaMPx.asMPxPtr( LSystemNode() )

# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    fileHandle = open('E:\EDocuments\cis660\hw3\HW3_basecode\menuinitialization.mel', 'r' )
    str1 = fileHandle.read()
    fileHandle.close()
    mymel=mel.eval(str1)
    
    try:
        mplugin.registerNode( kPluginNodeTypeName, LSystemNodeId, nodeCreator, nodeInitializer )
    except:
        sys.stderr.write( "Failed to register node: %s\n" % kPluginNodeTypeName )
    try:
        mplugin.registerNode( rkPluginNodeTypeName, randomNodeId, rnodeCreator, rnodeInitializer )
    except:
        sys.stderr.write( "Failed to register node: %s\n" % rkPluginNodeTypeName )

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( LSystemNodeId )
    except:
        sys.stderr.write( "Failed to unregister node: %s\n" % kPluginNodeTypeName )
    try:
        mplugin.deregisterNode( randomNodeId )
    except:
        sys.stderr.write( "Failed to unregister node: %s\n" % kPluginNodeTypeName )

