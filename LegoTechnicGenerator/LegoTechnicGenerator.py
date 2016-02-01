import maya.cmds as cmds
import math as math

window_name = "LegoMaker"

if cmds.window( window_name, exists = True ):
    cmds.deleteUI( window_name, window = True )

window = cmds.window(window_name, title="Lego Maker", menuBar=True, widthHeight=(483, 603))

cmds.menu(label="Basic Options")
cmds.menuItem(label="New Scene", 
command=('cmds.file(new=True,force=True)'))
cmds.menuItem(label="Delete Selected", command=('cmds.delete()'))

tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

#####brick options
#brick colour
child1 = cmds.columnLayout()

cmds.frameLayout( collapsable = False, label = "Brick Colour", width = 483)
cmds.colorSliderGrp('brickColour', label="Colour", hsv=(120, 1, 1))
cmds.checkBox( 'makeTransparent', label='Transparent', changeCommand ='brickHeightToggle()' )
cmds.setParent( '..' )

#brick options
cmds.frameLayout( collapsable = True, label = "Bricks", width = 483)
cmds.intSliderGrp('brickLength',label="Length", field=True, min=1, max=20, value=1)
cmds.intSliderGrp('brickWidth', label="Width", field=True, min=1, max=20, value=6)
cmds.intSliderGrp('brickHeight', label="Height", field=True, min=1, max=20, value=1)
cmds.radioButtonGrp('brickStudOptions', label='Studs:', labelArray3=['hollow', 'filled', 'none'], numberOfRadioButtons=3, select = 1 )
cmds.radioButtonGrp('brickHoleOptions', label='Holes:', labelArray3=['offset', 'even', 'none'], numberOfRadioButtons=3, select = 1 )
cmds.checkBox( 'flatBrickCheck', label='Flat Brick', changeCommand ='brickHeightToggle()' )
cmds.button(label="Create Brick", command=('brick()'))
cmds.setParent( '..' )

#brick options
cmds.frameLayout( collapsable = True, label = "Round Plate", width = 483)
cmds.button(label="Create Round Plate", command=('roundPlate()'))
cmds.setParent( '..' )

#brick options
cmds.frameLayout( collapsable = True, label = "Sloped Block", width = 483)
cmds.button(label="Create Sloped Block", command=('slopedBlock()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

#####beam options
child2 = cmds.columnLayout()

#general
cmds.frameLayout( collapsable = False, label = "General", width = 483)
cmds.colorSliderGrp('beamColour', label="Colour", hsv=(120, 1, 1))
cmds.checkBox( 'leftCrossCheck', label = 'Left Hole Cross')
cmds.checkBox( 'rightCrossCheck', label = 'Right Hole Cross')
cmds.setParent( '..' )

#straight beam
cmds.frameLayout( collapsable = True, label = "Straight Beam", width = 483)
cmds.intSliderGrp('beamLength', label="Length", field=True, min=2, max=15, value=8)
cmds.button(label="Create Straight Beam", command=('straightBeam()'))
cmds.setParent( '..' )

#angular beam
cmds.frameLayout( collapsable = True, label = "Angular Beam", width = 483)
cmds.intSliderGrp('horizontalLength', label="Horizontal Length", field=True, min=2, max=15, value=4)
cmds.intSliderGrp('angledLength', label="Angled Length", field=True, min=2, max=15, value=3)
cmds.radioButtonGrp('angleDegree', label='Angle (Degrees):', labelArray2=['53', '90'], numberOfRadioButtons=2, select = 2 )
angleArray = [0, 53, 90]
cmds.button(label="Create Angular Beam", command=('angularBeam()'))
cmds.setParent( '..' )

#double angular beam
cmds.frameLayout( collapsable = True, label = "Double Angular Beam", width = 483)
cmds.intSliderGrp('dHorizontalLength', label="Horizontal Length", field=True, min=2, max=15, value=7)
cmds.intSliderGrp('dVerticalLength', label="Vertical Length", field=True, min=2, max=15, value=3)
cmds.button(label="Create Double Angular Beam", command=('doubleAngularBeam()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

#####wheel options
#tyre/hub colour
child3 = cmds.columnLayout()

cmds.frameLayout( collapsable = False, label = "Wheel Colour", width = 483)
cmds.colorSliderGrp('wheelColour', label="Colour", hsv=(120, 1, 1))
cmds.setParent( '..' )

#rim options
cmds.frameLayout( collapsable = True, label = "Rims", width = 483)
cmds.radioButtonGrp('rimStyle', label='Rim Style:', labelArray2=['Wide', 'Narrow'], numberOfRadioButtons=2, select = 1 )
cmds.button(label="Create Rim", command=('rim()'))
cmds.setParent( '..' )

#tyre options
cmds.frameLayout( collapsable = True, label = "Tyres", width = 483)
cmds.button(label="Create Tyre", command=('tyre()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

#####Misc
#colour
child4 = cmds.columnLayout()

cmds.frameLayout( collapsable = False, label = "Colour", width = 483)
cmds.colorSliderGrp('miscColour', label="Colour", hsv=(120, 1, 1))
cmds.setParent( '..' )

#axles
cmds.frameLayout( collapsable = True, label = "Axles", width = 483)
cmds.intSliderGrp('axleLength', label="Axle Length", field=True, min=1, max=20, value=7)
cmds.button(label="Create Axle", command=('axle()'))
cmds.setParent( '..' )

#connectors
cmds.frameLayout( collapsable = True, label = "Connectors", width = 483)
cmds.button(label="Create Connector", command=('connector()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

#tab layout lables
cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'Bricks'), (child2, 'Beams'), (child3, 'Wheels'), (child4, 'Misc')) )

cmds.setParent( '..' )

cmds.showWindow( window )

#turn off height and hole options if flat brick is selected 
def brickHeightToggle():
    flatBrick = cmds.checkBox('flatBrickCheck', query = True, value = True)
    
    if( flatBrick == True ):
        cmds.intSliderGrp( 'brickHeight', edit = True, value = 1, enable = False)
        cmds.radioButtonGrp( 'brickHoleOptions', edit = True, select = 3, enable = False)
    elif( flatBrick == False ):
        cmds.intSliderGrp( 'brickHeight', edit = True, enable = True )
        cmds.radioButtonGrp( 'brickHoleOptions', edit = True, enable = True)

#create connectors
def connector():
    rgb = cmds.colorSliderGrp('miscColour', query=True, rgbValue=True)
    
    cX = 1.6
    cY = 0.6
    cZ = 0.6
    
    cMiddle = cmds.polyCylinder( h = 1.6/2, r = 0.5/2, sz = 1 )
    cmds.rotate( 90, rotateZ = True )
    cmds.move( (1.6/2)/2, moveX = True )
    
    cInsideRidge = cmds.polyCylinder( h = 0.1, r = cY/2, sz = 1 )
    cmds.rotate( 90, rotateZ = True )
    cmds.move( 0.1/2, moveX = True )
    
    cOutsideRidge = cmds.polyTorus( sr = 0.05, r = (cY/2.6))
    cmds.rotate( 90, rotateZ = True )
    cmds.move( (cX/2) - (0.08/2), moveX = True )
    
    connector = cmds.polyCBoolOp( cMiddle, cInsideRidge, op = 1 )
    connector = cmds.polyCBoolOp( connector, cOutsideRidge, op = 1 )
    
    cCut = createRoundedBlock( cY * 0.6, cY * 0.2, 5, 2 )
    cmds.move( cY + 0.1, moveX = True )
    
    connector = cmds.polyCBoolOp( connector, cCut, op = 2 )
    
    cMCut = cmds.polyCylinder( h = 1.6, r = 0.45/2, sz = 1 )
    cmds.rotate( 90, rotateZ = True )
    cmds.move( (1.6/2)/2, moveX = True )
    
    connector = cmds.polyCBoolOp( connector, cMCut, op = 2 )
    
    connectorL = cmds.duplicate( connector )
    cmds.scale( -1, scaleX = True )
    cmds.move( -(1.6/2), moveX = True )
    
    connector = cmds.polyUnite( connector, connectorL)
    
    myShader = cmds.shadingNode( 'phong', asShader=True )
    cmds.setAttr( myShader+".color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.setAttr( myShader+".reflectivity", 0 )
    
    cmds.select( connector )
    cmds.hyperShade( assign = myShader )
    
    cmds.delete( ch = True )

#create axles
def axle():
    axleLength = cmds.intSliderGrp( 'axleLength', query = True, value = True)
    rgb = cmds.colorSliderGrp('miscColour', query=True, rgbValue=True)
    
    axleX = axleLength * 0.8
    axleY = 0.4
    axleZ = 0.4
    
    hAxle = cmds.polyCube( w = axleX, h = axleY/2, d = axleZ )
    vAxle = cmds.polyCube( w = axleX, h = axleY, d = axleZ/2 )
    
    axle = cmds.polyCBoolOp( hAxle, vAxle, op = 1 )[0]
    
    myShader = cmds.shadingNode( 'phong', asShader=True )
    cmds.setAttr( myShader+".color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.setAttr( myShader+".reflectivity", 0 )
    
    cmds.select( axle )
    cmds.hyperShade( assign = myShader )
    
    cmds.delete( ch = True )

#create rims
def rim():
    
    #get values from UI
    rimStyle = cmds.radioButtonGrp( 'rimStyle', query = True, select = True)
    rgb = cmds.colorSliderGrp('wheelColour', query=True, rgbValue=True)
    
    #set up variables
    radius = 1.6
    widthHalf = 2.1 / 2
    
    if( rimStyle == 1 ):
        mediumCircle = cmds.polyCylinder( h = widthHalf * 0.4, r = radius * 0.67 )
        cmds.rotate( 90, rotateZ = True )
        
        crossV = cmds.polyCube( w = widthHalf, h = 0.4, d = 0.2 )
        crossH = cmds.polyCube( w = widthHalf, h = 0.2, d = 0.4 )
        cross = cmds.polyCBoolOp( crossV, crossH, op = 1 )
        cmds.move( widthHalf / 2, moveX = True ) 
        mediumCircle = cmds.polyCBoolOp( mediumCircle, cross, op = 2 )
        
        innerCircle = cmds.polyPipe( h = widthHalf * 0.3, r = radius * 0.33, t = 0.14 )    
        cmds.rotate( 90, rotateZ = True )
        cmds.move( ((widthHalf * 0.4) / 2) + ((widthHalf * 0.3) / 2), moveX = True )
        
        outerCircle = cmds.polyPipe( h = widthHalf, r = radius, t = 0.2 )
        cmds.rotate( 90, rotateZ = True )
        cmds.move( (((widthHalf * 0.4) / 2) + ((widthHalf * 0.5) / 2)) + 0.1, moveX = True )
        
        outerCircleCut = cmds.polyPipe( h = widthHalf * 0.33, r = radius, t = 0.1 )
        cmds.rotate( 90, rotateZ = True )
        cmds.move( (((widthHalf * 0.4) / 2) + ((widthHalf * 0.5) / 2)) + 0.1, moveX = True )
        
        outerCircle = cmds.polyCBoolOp( outerCircle, outerCircleCut, op = 2 )
        
        slope = cmds.polyCone()
        cmds.rotate( 90, rotateZ = True )
        cmds.move( 0.810, moveX = True )
        cmds.scale( 5.455, 1, 5.455 )
        
        slopeCutL = cmds.polyCylinder( h = widthHalf, r = radius )
        cmds.rotate( 90, rotateZ = True )
        cmds.move( -( widthHalf / 2), moveX = True )
        
        slopeCutR = cmds.polyCylinder( h = 4, r = radius * 10 )
        cmds.rotate( 90, rotateZ = True )
        cmds.move( 2.326, moveX = True )
        
        slope = cmds.polyCBoolOp( slope, slopeCutL, op = 2 )[0]
        slope = cmds.polyCBoolOp( slope, slopeCutR, op = 2 )[0]
        
        cmds.delete( slope+".f[21]")
        
        rimL = cmds.polyUnite( mediumCircle, innerCircle, outerCircle, slope )
        cmds.move( (widthHalf*0.4)/2, moveX = True )
        
        rimR = cmds.duplicate( rimL )
        cmds.scale( -1, scaleX = True )
        cmds.move( -((widthHalf*0.4)/2), moveX = True )
        
        rim = cmds.polyUnite( rimR, rimL )
    
    elif( rimStyle == 2 ):
        
        radius  = 1.5
        circleList = []
        
        mainCircle = cmds.polyCylinder( h = 0.4, r = radius - 0.2 )
        innerCircle = cmds.polyCylinder( h = 0.5, r = radius * 0.2 )
        hCross = cmds.polyCube( w = radius * 0.24, h = 3, d = radius * 0.1 )
        vCross = cmds.polyCube( w = radius * 0.1, h = 3, d = radius * 0.24 )
        cross = cmds.polyCBoolOp( hCross, vCross, op = 1 )[0]
        
        rim = cmds.polyCBoolOp( mainCircle, innerCircle, op = 1 )
        rim = cmds.polyCBoolOp( rim, cross, op = 2 )
        
        lRidge = cmds.polyTorus( sr = 0.1, r = (radius * 0.9))
        cmds.move( 0.4/2, moveY = True )
        rRidge = cmds.polyTorus( sr = 0.1, r = (radius * 0.9))
        cmds.move( -(0.4/2), moveY = True )
        
        rim = cmds.polyCBoolOp( rim, lRidge, op = 1 )[0]
        rim = cmds.polyCBoolOp( rim, rRidge, op = 1 )[0]
        
        cutCircle = cmds.polyCylinder( h = 3, r = radius * 0.17 )[0]
        
        cmds.move( 0, 0, 0.8)
    
        cmds.move( 0, 0, 0, cutCircle+".scalePivot", cutCircle+".rotatePivot", absolute=True)
        
        circleList.append( cutCircle )
        
        for i in range( 0, 5):
            cutCircle = cmds.duplicate( cutCircle )
            cmds.rotate( 0, 60, 0, cutCircle, r = True )
            circleList.append( cutCircle )
    
        
        cutCircles = cmds.polyUnite( *circleList)
        
        rim = cmds.polyCBoolOp( rim, cutCircles, op = 2 )
        
        cmds.rotate( 90, rotateX = True )
        
            
    myShader = cmds.shadingNode( 'phong', asShader=True )
    cmds.setAttr( myShader+".color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.setAttr( myShader+".reflectivity", 0 )
    
    cmds.select( rim )
    cmds.hyperShade( assign = myShader )
    
    cmds.delete( ch = True )
    
def tyre():
    
    #get values from UI
    rgb = cmds.colorSliderGrp('wheelColour', query=True, rgbValue=True)
    
    #set up variables
    radius = 2.85
    widthHalf = 2.7
    
    ridgeShapeList = []
    
    innerCircle = cmds.polyPipe( h = widthHalf * 0.7, r = 2.65, t = 1.05 )
    outerCircle = cmds.polyPipe( h = widthHalf, r = 2.65, t = 0.85 )
    ridge1 = cmds.polyPipe( h = (widthHalf * 0.33)/2, r = 2.85, t = 0.80 )
    cmds.move( -0.567, moveY = True)
    ridge2 = cmds.polyPipe( h = widthHalf * 0.33, r = 2.85, t = 0.80 )
    cmds.move( -0.120, moveY = True)
    
    tire = cmds.polyCBoolOp( innerCircle, outerCircle, op = 1 )[0]
    tire = cmds.polyCBoolOp( tire, ridge1, op = 1 )[0]
    tire = cmds.polyCBoolOp( tire, ridge2, op = 1 )[0]
    
    ridgeShape = cmds.polyCube( w = 0.63, h = 0.2, d = 0.2)
    cmds.move( -0.05, moveY = True)
    ridgeShapeL = cmds.polyCube( w = 0.2, h = 0.33, d = 0.2, sy = 2)[0]
    cmds.select( ridgeShapeL+'.vtx[4]', ridgeShapeL+'.vtx[5]')
    cmds.move( -0.09, moveZ = True )
    ridgeShapeR = cmds.duplicate( ridgeShapeL )
    cmds.move( -((0.63/2) - 0.1), 0.33/2, 0, ridgeShapeL )
    cmds.move( (0.63/2) - 0.1, 0.33/2, 0, ridgeShapeR )
    
    ridgeShape = cmds.polyCBoolOp( ridgeShape, ridgeShapeL, op = 1 )[0]
    ridgeShape = cmds.polyCBoolOp( ridgeShape, ridgeShapeR, op = 1 )[0]
    
    cmds.move( 0, 0.343, radius - 0.14)
    
    cmds.move( 0, 0, 0, ridgeShape+".scalePivot", ridgeShape+".rotatePivot", absolute=True)
    
    ridgeShapeList.append( ridgeShape )
    
    for i in range( 0, 19):
        ridgeShape = cmds.duplicate( ridgeShape )[0]
        cmds.rotate( 0, 18, 0, ridgeShape, r = True )
        ridgeShapeList.append( ridgeShape )
    
    ridges = cmds.polyUnite( *ridgeShapeList ) 
    cmds.rotate( 9, rotateY = True ) 
    tireL = cmds.polyUnite( tire, ridges )[0]
    
    cmds.rotate( 90, tireL, rotateZ = True )
    cmds.move( ((widthHalf / 2)/2), tireL, moveX = True )  
    
    tireR = cmds.duplicate( tireL )[0]
    cmds.scale( -1, scaleY = True )
    cmds.move( -((widthHalf / 2)/2), tireL, moveX = True ) 
    
    tire = cmds.polyUnite( tireR, tireL )
    
    myShader = cmds.shadingNode( 'phong', asShader=True )
    cmds.setAttr( myShader+".color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.setAttr( myShader+".reflectivity", 0 )
    
    cmds.select( tire )
    cmds.hyperShade( assign = myShader )
    
    cmds.delete( ch = True )
    
#create bricks
def brick():
    
    #get values from UI
    brickLength = cmds.intSliderGrp( 'brickLength', query = True, value = True)
    brickWidth = cmds.intSliderGrp( 'brickWidth', query = True, value = True)
    brickHeight = cmds.intSliderGrp('brickHeight', query = True, value = True)
    flatBrick = cmds.checkBox('flatBrickCheck', query = True, value = True)
    brickStuds = cmds.radioButtonGrp( 'brickStudOptions', query = True, select = True)
    brickHoles = cmds.radioButtonGrp( 'brickHoleOptions', query = True, select = True)
    rgb = cmds.colorSliderGrp('brickColour', query=True, rgbValue=True)
    transparent = cmds.checkBox('makeTransparent', query = True, value = True)
    
    #set up variables
    brickList = []
    studList = []
    
    if brickHoles == 1:
        holeOffset = 0.8
        holeNum = brickWidth - 1
    else:
        holeOffset = 0.4
        holeNum = brickWidth
    
    brickSizeX = brickWidth * 0.8
    brickSizeZ = brickLength * 0.8
    if( flatBrick == True ):
        brickSizeY =  0.32
    elif( flatBrick == False ):    
        brickSizeY = 0.96
    
    #create brick 
    for h in range ( brickHeight ):
        brick = cmds.polyCube( h = brickSizeY, w = brickSizeX, d = brickSizeZ )
        cmds.move( ( brickSizeY / 2 ), brick, moveY = True )
        
        if( brickHoles == 1 or brickHoles == 2 ):
            brick = createBlockHoles( brickSizeX, brickSizeY, brick, holeNum, holeOffset )
                
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        cmds.move( ( brickSizeY * h ), brick, moveY = True, a = True )
        brickList.append( brick )
        
    if( len( brickList ) > 1 ):
        brick = cmds.polyUnite( *brickList )
    else:
        brick = brickList[0]
    
    if( brickStuds == 1 or brickStuds == 2 ):
        for l in range ( brickLength ):
            for w in range( brickWidth ):
                stud = cmds.polyCylinder( h = 0.18, r = 0.24 )
                
                if( brickStuds == 1 ):
                   studCut = cmds.polyCylinder( h = 0.18, r = 0.15 ) 
                   stud = cmds.polyCBoolOp( stud, studCut, op = 2 )
                
                cmds.move(((w * 0.8) - (brickSizeX/2.0) + 0.4 ), moveX = True, a = True)
                cmds.move((brickSizeY * brickHeight) + (0.18/2), moveY = True, a = True)
                cmds.move(((l * 0.8) - (brickSizeZ/2.0) + 0.4), moveZ = True, a = True)
                studList.append( stud )
    
        studs =  cmds.polyUnite( *studList )
        brick = cmds.polyUnite( studs, brick )
        
    myShader = cmds.shadingNode( 'phong', asShader=True )
    cmds.setAttr( myShader+".color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.setAttr( myShader+".reflectivity", 0 )
    
    if( transparent == True ):
       cmds.setAttr( myShader+".transparency", 0.5, 0.5, 0.5, type = 'double3' ) 
    
    cmds.select( brick )
    cmds.hyperShade( assign = myShader )
    
    cmds.delete( ch = True )
    
#create round plate
def roundPlate():
    
    #get values from UI
    rgb = cmds.colorSliderGrp('brickColour', query=True, rgbValue=True)
    transparent = cmds.checkBox('makeTransparent', query = True, value = True)
    
    base = cmds.polyCylinder( h = 0.18, r = 0.3 )
    cmds.rotate( 90, rotateY = True )
    cmds.move( 0.18/2, moveY = True)
    
    wide = cmds.polyCylinder( h = 0.14, r = 0.4 )
    cmds.rotate( 90, rotateY = True )
    cmds.move( 0.18 + (0.14/2), moveY = True)
    
    stud = cmds.polyCylinder( h = 0.18, r = 0.24 )
    cmds.rotate( 90, rotateY = True )
    cmds.move( 0.18 + 0.14 + (0.18/2), moveY = True)
    
    rp = cmds.polyUnite( base, wide, stud )
    
    myShader = cmds.shadingNode( 'phong', asShader=True )
    cmds.setAttr( myShader+".color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.setAttr( myShader+".reflectivity", 0 )
    
    if( transparent == True ):
       cmds.setAttr( myShader+".transparency", 0.5, 0.5, 0.5, type = 'double3' ) 
    
    cmds.select( rp )
    cmds.hyperShade( assign = myShader )
    
    cmds.delete( ch = True )
    
#create sloped block
def slopedBlock():
    
    #get values from UI
    rgb = cmds.colorSliderGrp('brickColour', query=True, rgbValue=True)
    transparent = cmds.checkBox('makeTransparent', query = True, value = True)
    
    block = cmds.polyCube( w = 0.8, h = 0.6, d = 0.8)[0]
    cmds.move( 0.6/2, moveY = True)
    
    cmds.select( block+'.vtx[2]', block+'.vtx[3]')
    cmds.move( 0.1, moveY = True )
    
    myShader = cmds.shadingNode( 'phong', asShader=True )
    cmds.setAttr( myShader+".color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.setAttr( myShader+".reflectivity", 0 )
    
    if( transparent == True ):
       cmds.setAttr( myShader+".transparency", 0.5, 0.5, 0.5, type = 'double3' ) 
    
    cmds.select( block )
    cmds.hyperShade( assign = myShader )  
    
    cmds.delete( ch = True )  
    
#create straight beam
def straightBeam():
    
    #get values from UI
    beamLength = cmds.intSliderGrp('beamLength', query=True, value=True)
    leftCross = cmds.checkBox('leftCrossCheck', query = True, value = True)
    rightCross = cmds.checkBox('rightCrossCheck', query = True, value = True)
    rgb = cmds.colorSliderGrp('beamColour', query=True, rgbValue=True)
    
    #set up variables
    holeOffset = 0.0;
    
    beamSizeX = ( beamLength - 1 ) * 0.8
    beamSizeZ = 0.8
    beamSizeY = 0.8
    
    #hAxle = cmds.polyCube( w = axleX, h = axleY/2, d = axleZ )
    #vAxle = cmds.polyCube( w = axleX, h = axleY, d = axleZ/2 )
    
    #axle = cmds.polyCBoolOp( hAxle, vAxle, op = 1 )[0]
    
    beam = createRoundedBlock( beamSizeX, beamSizeY, beamSizeZ, beamLength )
    cmds.move(( beamSizeY / 2.0 ), moveY = True ) 
    
    if( leftCross == True and rightCross == False):
        holeOffset = 0.8
        beam = createBlockHoles( beamSizeX, beamSizeY, beam, beamLength - 1, holeOffset )
        hCross = cmds.polyCube( w = 0.62, h = 0.31, d = 3 )
        vCross = cmds.polyCube( w = 0.31, h = 0.62, d = 3 )
        cross = cmds.polyCBoolOp( hCross, vCross, op = 1 )[0]
        cmds.move( -(beamSizeX/2), beamSizeY/2, 0 )
        beam = cmds.polyCBoolOp( beam, cross, op = 2 )[0]
        
    elif( leftCross == False and rightCross == True):
        beam = createBlockHoles( beamSizeX, beamSizeY, beam, beamLength - 1, holeOffset )
        hCross = cmds.polyCube( w = 0.62, h = 0.31, d = 3 )
        vCross = cmds.polyCube( w = 0.31, h = 0.62, d = 3 )
        cross = cmds.polyCBoolOp( hCross, vCross, op = 1 )[0]
        cmds.move( (beamSizeX/2), beamSizeY/2, 0 )
        beam = cmds.polyCBoolOp( beam, cross, op = 2 )[0]
        
    elif( leftCross == True and rightCross == True):
        holeOffset = 0.8
        beam = createBlockHoles( beamSizeX, beamSizeY, beam, beamLength - 2, holeOffset )
        hLCross = cmds.polyCube( w = 0.62, h = 0.31, d = 3 )
        vLCross = cmds.polyCube( w = 0.31, h = 0.62, d = 3 )
        lCross = cmds.polyCBoolOp( hLCross, vLCross, op = 1 )[0]
        cmds.move( -(beamSizeX/2), beamSizeY/2, 0 )
        beam = cmds.polyCBoolOp( beam, lCross, op = 2 )[0]
        hRCross = cmds.polyCube( w = 0.62, h = 0.31, d = 3 )
        vRCross = cmds.polyCube( w = 0.31, h = 0.62, d = 3 )
        rCross = cmds.polyCBoolOp( hRCross, vRCross, op = 1 )[0]
        cmds.move( beamSizeX/2, beamSizeY/2, 0 )
        beam = cmds.polyCBoolOp( beam, rCross, op = 2 )[0]
        
    else:
        beam = createBlockHoles( beamSizeX, beamSizeY, beam, beamLength, holeOffset )
           
    myShader = cmds.shadingNode( 'phong', asShader=True )
    cmds.setAttr( myShader+".color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.setAttr( myShader+".reflectivity", 0 )
    
    cmds.select( beam )
    cmds.hyperShade( assign = myShader )
    
    cmds.delete( ch = True )

#create angular beam    
def angularBeam():
    
    horizontalLength = cmds.intSliderGrp('horizontalLength', query=True, value=True)
    angledLength = cmds.intSliderGrp('angledLength', query=True, value=True)
    angleSelected = cmds.radioButtonGrp('angleDegree', query=True, select=True)
    angleDegree = angleArray[angleSelected]
    leftCross = cmds.checkBox('leftCrossCheck', query = True, value = True)
    rightCross = cmds.checkBox('rightCrossCheck', query = True, value = True)
    rgb = cmds.colorSliderGrp('beamColour', query=True, rgbValue=True)
    
    holeOffset = 0.0;
    
    cubeSizeH = (horizontalLength - 1) * 0.8
    cubeSizeA = (angledLength - 1) * 0.8
    cubeSizeZ = 0.8 
    cubeSizeY = 0.8
    
    horizontalCube = createRoundedBlock( cubeSizeH, cubeSizeY, cubeSizeZ, horizontalLength )
    cmds.move(( cubeSizeY / 2.0 ), moveY = True )
    
    if( leftCross == True ):
        holeOffset = 0.8
        horizontalCube = createBlockHoles( cubeSizeH, cubeSizeY, horizontalCube, horizontalLength - 1, holeOffset )
        hCross = cmds.polyCube( w = 0.62, h = 0.31, d = 3 )
        vCross = cmds.polyCube( w = 0.31, h = 0.62, d = 3 )
        cross = cmds.polyCBoolOp( hCross, vCross, op = 1 )[0]
        cmds.move( -(cubeSizeH/2), cubeSizeY/2, 0 )
        horizontalCube = cmds.polyCBoolOp( horizontalCube, cross, op = 2 )[0]
               
    else:
        horizontalCube = createBlockHoles( cubeSizeH, cubeSizeY, horizontalCube, horizontalLength, holeOffset )
    
    angledCube = createRoundedBlock( cubeSizeA, cubeSizeY, cubeSizeZ, angledLength )
    cmds.move(( cubeSizeY / 2.0 ), moveY = True )
    
    if( rightCross == True ):
        holeOffset = 0.0
        angledCube = createBlockHoles( cubeSizeA, cubeSizeY,angledCube, angledLength - 1, holeOffset )
        hCross = cmds.polyCube( w = 0.62, h = 0.31, d = 3 )
        vCross = cmds.polyCube( w = 0.31, h = 0.62, d = 3 )
        cross = cmds.polyCBoolOp( hCross, vCross, op = 1 )[0]
        cmds.move( cubeSizeA/2, cubeSizeY/2, 0 )
        angledCube = cmds.polyCBoolOp( angledCube, cross, op = 2 )[0]
               
    else:
        holeOffset = 0.0
        angledCube = createBlockHoles( cubeSizeA, cubeSizeY, angledCube, angledLength, holeOffset )[0]
    
    cmds.move( ( - (cubeSizeA/2.0)), (cubeSizeY/2), 0, angledCube+".scalePivot", angledCube+".rotatePivot", absolute=True)
    
    cmds.rotate( angleDegree, rotateZ = True )
    cmds.move( ((cubeSizeH/2) + (cubeSizeA/2)), moveX = True )
    
    angledBeam = cmds.polyUnite( horizontalCube, angledCube )
    
    myShader = cmds.shadingNode( 'phong', asShader=True )
    cmds.setAttr( myShader+".color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.setAttr( myShader+".reflectivity", 0 )
    
    cmds.select( angledBeam )
    cmds.hyperShade( assign = myShader )
    
    cmds.delete( ch = True )
    
#create double angular beam    
def doubleAngularBeam():
    
    horizontalLength = cmds.intSliderGrp('dHorizontalLength', query=True, value=True)
    verticalLength = cmds.intSliderGrp('dVerticalLength', query=True, value=True)
    angledLength = 3.8
    leftCross = cmds.checkBox('leftCrossCheck', query = True, value = True)
    rightCross = cmds.checkBox('rightCrossCheck', query = True, value = True)
    rgb = cmds.colorSliderGrp('beamColour', query=True, rgbValue=True)
    
    holeOffset = 0.0;
    
    cubeSizeH = (horizontalLength - 1) * 0.8
    cubeSizeA = 3.04
    cubeSizeV = (verticalLength - 1) * 0.8
    cubeSizeZ = 0.8 
    cubeSizeY = 0.8
    
    beamAngle = 45
    angledDistance =  ( math.sin( math.radians(45))) * cubeSizeA
    
    #create horizontal section of angled beam

    horizontalCube = createRoundedBlock( cubeSizeH, cubeSizeY, cubeSizeZ, horizontalLength )
    cmds.move(( cubeSizeY / 2.0 ), moveY = True )
    
    if( leftCross == True ):
        holeOffset = 0.8
        horizontalCube = createBlockHoles( cubeSizeH, cubeSizeY, horizontalCube, horizontalLength - 1, holeOffset )
        hCross = cmds.polyCube( w = 0.62, h = 0.31, d = 3 )
        vCross = cmds.polyCube( w = 0.31, h = 0.62, d = 3 )
        cross = cmds.polyCBoolOp( hCross, vCross, op = 1 )[0]
        cmds.move( -(cubeSizeH/2), cubeSizeY/2, 0 )
        horizontalCube = cmds.polyCBoolOp( horizontalCube, cross, op = 2 )[0]
               
    else:
        horizontalCube = createBlockHoles( cubeSizeH, cubeSizeY, horizontalCube, horizontalLength, holeOffset )
    
    #create angled section of angled beam
    
    angledCube = createRoundedBlock( cubeSizeA, cubeSizeY, cubeSizeZ, angledLength )
    cmds.move(( cubeSizeY / 2.0 ), moveY = True ) 
    
    #create left hole in angled beam section
    
    holeCylinderL = cmds.polyCylinder( r = 0.24, h = 2, sz=1 )
    cmds.rotate( 90, rotateX = True )
    cmds.move((cubeSizeY/2), moveY = True, a = True)
    cmds.move(( - (cubeSizeA/2.0)), moveX = True, a = True)
        
    ridgeCylinderL = cmds.polyCylinder( r=0.31, h=2, sz=1 )
    cmds.rotate( 90, rotateX = True )
    cmds.move((cubeSizeY/2), moveY = True, a = True)
    cmds.move(( - ( cubeSizeA / 2.0 )), moveX = True, a = True)
    
    ridgeCubeL = cmds.polyCube ( h = 0.64, w = cubeSizeY, d = cubeSizeY )
    cmds.rotate( 90, rotateX = True )
    cmds.move(( cubeSizeY / 2 ), moveY=True )
    cmds.move(( - (cubeSizeA/2.0)), moveX=True )
    
    angledCube = cmds.polyCBoolOp( angledCube, holeCylinderL, op=2 )
    ridgeCutterL = cmds.polyCBoolOp( ridgeCylinderL, ridgeCubeL, op=2 )  
    angledCube = cmds.polyCBoolOp( angledCube, ridgeCutterL, op=2 )
    
    #create right hole in angled beam section
    
    holeCylinderR = cmds.polyCylinder( r = 0.24, h = 2, sz=1 )
    cmds.rotate( 90, rotateX = True )
    cmds.move((cubeSizeY/2), moveY = True, a = True)
    cmds.move(((angledLength * 0.8) - (cubeSizeA/2.0)), moveX = True, a = True)
        
    ridgeCylinderR = cmds.polyCylinder( r=0.31, h=2, sz=1 )
    cmds.rotate( 90, rotateX = True )
    cmds.move((cubeSizeY/2), moveY = True, a = True)
    cmds.move(((angledLength * 0.8) - (cubeSizeA/2.0)), moveX = True, a = True)
    
    ridgeCubeR = cmds.polyCube ( h = 0.64, w = cubeSizeY, d = cubeSizeY )
    cmds.rotate( 90, rotateX = True )
    cmds.move((cubeSizeY/2), moveY=True )
    cmds.move(((angledLength * 0.8) - (cubeSizeA/2.0)), moveX=True )
    
    angledCube = cmds.polyCBoolOp( angledCube, holeCylinderR, op=2 )  
    ridgeCutterR = cmds.polyCBoolOp( ridgeCylinderR, ridgeCubeR, op=2 )   
    angledCube = cmds.polyCBoolOp( angledCube, ridgeCutterR, op=2 ) 
    
    #create rounded rectangle cutout in angled beam section
    holeBlock = createRoundedBlock( ( cubeSizeA - ( 0.8 * 2 )), 0.48, 2, angledLength )
    cmds.move(( cubeSizeY / 2.0 ), moveY = True )
    
    ridgeBlock = createRoundedBlock( ( cubeSizeA - ( 0.8 * 2 )), 0.62, 2, angledLength )
    cmds.move(( cubeSizeY / 2.0 ), moveY = True )
    
    ridgeCube = cmds.polyCube ( h = cubeSizeY, w = cubeSizeA, d = 0.64  )
    cmds.move(( cubeSizeY / 2.0 ), moveY = True )
    
    angledCube = cmds.polyCBoolOp( angledCube, holeBlock, op=2 )
    ridgeCutter = cmds.polyCBoolOp( ridgeBlock, ridgeCube, op=2 )   
    angledCube = cmds.polyCBoolOp( angledCube, ridgeCutter, op=2 ) 
    
    #move and rotate angled beam in to position
    cmds.move( ( - (cubeSizeA/2.0)), (cubeSizeY/2), 0, angledCube[0]+".scalePivot",angledCube[0]+".rotatePivot", absolute=True)
    
    cmds.rotate( beamAngle, rotateZ = True )
    cmds.move( ((cubeSizeH/2) + (cubeSizeA/2)), moveX = True )
    
    doubleBeam = cmds.polyUnite( horizontalCube, angledCube )
     
    #create vertical section of angled beam
    verticalCube = createRoundedBlock( cubeSizeV, cubeSizeY, cubeSizeZ, verticalLength )
    cmds.move(( cubeSizeY / 2.0 ), moveY = True )
    
    if( rightCross == True ):
        holeOffset = 0.0
        verticalCube = createBlockHoles( cubeSizeV, cubeSizeY, verticalCube, verticalLength - 1, holeOffset )
        hCross = cmds.polyCube( w = 0.62, h = 0.31, d = 3 )
        vCross = cmds.polyCube( w = 0.31, h = 0.62, d = 3 )
        cross = cmds.polyCBoolOp( hCross, vCross, op = 1 )[0]
        cmds.move( cubeSizeV/2, cubeSizeY/2, 0 )
        verticalCube = cmds.polyCBoolOp( verticalCube, cross, op = 2 )[0]
               
    else:
        holeOffset = 0.0
        verticalCube = createBlockHoles( cubeSizeV, cubeSizeY, verticalCube, verticalLength, holeOffset )
    
    cmds.move( ( - (cubeSizeA/2.0)), (cubeSizeY/2), 0, angledCube[0]+".scalePivot",angledCube[0]+".rotatePivot", absolute=True)
    
    cmds.rotate( 90, rotateZ = True )
    cmds.move( (( cubeSizeH / 2 ) + angledDistance ), moveX = True )
    cmds.move( (( cubeSizeV / 2 ) + angledDistance ), moveY = True )
    
    doubleBeam = cmds.polyUnite( doubleBeam, verticalCube )
    
    #add material
    myShader = cmds.shadingNode( 'phong', asShader=True )
    cmds.setAttr( myShader+".color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.setAttr( myShader+".reflectivity", 0 )
    
    cmds.select( doubleBeam )
    cmds.hyperShade( assign = myShader )
    
    cmds.delete( ch = True )

#create rounded corner rectangles
def createRoundedBlock( blockSizeX, blockSizeY, blockSizeZ, blockLength ):
    
    edgeCylinderL = cmds.polyCylinder ( h = blockSizeZ, r = blockSizeY/2 )
    cmds.rotate( 90, rotateX = True )
    cmds.move( ( -blockSizeX/2 ), moveX = True, a=True)
    
    edgeCylinderR = cmds.polyCylinder ( h = blockSizeZ, r = blockSizeY/2 )
    cmds.rotate( 90, rotateX = True )
    cmds.move( ( blockSizeX/2 ), moveX = True, a=True)
    
    block = cmds.polyCube ( h = blockSizeY, w = blockSizeX, d = blockSizeZ, sx = ( blockLength - 1 ) * 2, sy = 2 )
    
    block =  cmds.polyCBoolOp( block, edgeCylinderL, op = 1 )
    block =  cmds.polyCBoolOp( block, edgeCylinderR, op = 1 )
    
    return block

#create holes in blocks
def createBlockHoles( blockSizeX, blockSizeY, block, blockLength, blockOffset ):
    
    hcList = []
    rcyList = []
    rcuList = []
    
    for j in range( blockLength ):
        #create cylinders to cut holes
        holeCylinder = cmds.polyCylinder( r = 0.24, h = 2, sz=1 )
        cmds.rotate( 90, rotateX = True )
        cmds.move((blockSizeY/2), moveY = True, a = True)
        cmds.move(((j * 0.8) - (blockSizeX/2.0) + blockOffset ), moveX = True, a = True)
        hcList.append( holeCylinder )
        
        #create cylinders to cut sunken area around holes 
        ##create a cylinder
        ridgeCylinder = cmds.polyCylinder( r=0.31, h=2, sz=1 )
        cmds.rotate( 90, rotateX = True )
        cmds.move((blockSizeY/2), moveY = True, a = True)
        cmds.move(((j * 0.8) - (blockSizeX/2.0) + blockOffset ), moveX = True, a = True)
        rcyList.append( ridgeCylinder )
        
        ##create a cube
        ridgeCube = cmds.polyCube ( h = 0.64, w = blockSizeY, d = blockSizeY )
        cmds.rotate( 90, rotateX = True )
        cmds.move((blockSizeY/2), moveY=True )
        cmds.move(((j * 0.8) - (blockSizeX/2.0) + blockOffset ), moveX=True )
        rcuList.append( ridgeCube )
    
    if len( hcList ) > 1 :
        holeCylinders = cmds.polyUnite( *hcList )  
        ridgeCylinders = cmds.polyUnite( *rcyList )
        ridgeCubes = cmds.polyUnite( *rcuList )  
    else:
        holeCylinders = hcList[0]
        ridgeCylinders = rcyList[0]
        ridgeCubes = rcuList[0]
        
    block = cmds.polyCBoolOp( block, holeCylinders, op=2 )
    
    ridgeCutter = cmds.polyCBoolOp( ridgeCylinders, ridgeCubes, op=2 ) 
    
    block = cmds.polyCBoolOp( block, ridgeCutter, op=2 )
    
    return block