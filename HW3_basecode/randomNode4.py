# randomNode.py
#   Produces random locations to be used with the Maya instancer node.

import sys
import random

import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as cmds

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
kPluginNodeTypeName = "randomNode"

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
def nodeInitializer():
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
def nodeCreator():
    return OpenMayaMPx.asMPxPtr( randomNode() )

# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode( kPluginNodeTypeName, randomNodeId, nodeCreator, nodeInitializer )
    except:
        sys.stderr.write( "Failed to register node: %s\n" % kPluginNodeTypeName )

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( randomNodeId )
    except:
        sys.stderr.write( "Failed to unregister node: %s\n" % kPluginNodeTypeName )
