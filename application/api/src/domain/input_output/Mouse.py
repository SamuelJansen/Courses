import pygame as pg

import ClickEvent, FalseClickEvent, ErrorEvent, HoverEvent
import objectFunction, mouseFunction, applicationFunction, fatherFunction

print('Mouse library imported')

class Mouse:

    ERROR_IN_HOVER_EVENT_DETECTION = 'Eror in hover event detection'

    def update(self):
        self.updatePosition()

    def __init__(self,application):
        '''
        Mouse.position is pondered by dev screen size'''
        self.application = application
        self.position = [0,0]
        self.devPosition = [0,0]
        self.scripArea = ''

        self.state = mouseFunction.State.FREE
        self.lastBusyState = mouseFunction.State.NOT_BUZY
        self.inLifeCicle = False

        self.objectHitDown = None
        self.objectHitUp = None
        self.objectHit = None
        self.objectsHitChecket = []

        self.objectClicked = None

        self.objectsHoverChecket = []
        self.hovering = None
        self.objectHover = None
        self.lastObjectHover = None

        self.updatePosition()

    def updatePosition(self):
        ###- It needs some work
        position = list(pg.mouse.get_pos())
        self.position = [int(position[0]),int(position[1])]
        self.devPosition[0] = int(self.position[0]*self.application.devResize[0])
        self.devPosition[1] = int(self.position[1]*self.application.devResize[1])
        if self.application.frame.apfNew :
            self.updateObjectHover()

    def handleEvent(self,pgEvent):
        self.updateState(pgEvent)
        if self.state == mouseFunction.State.LEFT_CLICK_DOWN :
            self.clickDown()
            self.scripArea = f'{self.devPosition[0]}x{self.devPosition[1]}'

        if self.state == mouseFunction.State.LEFT_CLICK_UP :
            self.clickUp()
            self.scripArea += f'x{self.devPosition[0]}x{self.devPosition[1]}'
        self.resolveClick()

    def clickDown(self):
        self.getRecursiveColision(self.application)
        self.objectHitDown = self.objectHit

    def clickUp(self):
        self.getRecursiveColision(self.application)
        self.objectHitUp = self.objectHit

    def getRecursiveColision(self,object):
        if object.handler.objects :
            objectHitList = []
            childrenNames = list(object.handler.objects.keys())
            for childName in childrenNames:
                if childName in object.handler.objects :
                    self.updateColision(object.handler.objects[childName],objectHitList)
            if objectHitList :
                for objectHit in objectHitList :
                    self.getRecursiveColision(objectHit)
        self.updateColision(object,[])

    ###- TODO samuel.jansen 2020-02-16 - remove objectsHitChecked list
    def updateColision(self,object,hitList):
        if object not in self.objectsHitChecket :
            if self.didColided(object) :
                # print(f'Mouse.updateColision(): Mouse.didColided() -> object.name = {object.name}')
                if self.didHit(object) :
                    # print(f'Mouse.updateColision(): Mouse.didHit() -> object.name = {object.name}')
                    if not self.objectHit :
                        self.objectHit = object
                    if object.blitOrder > self.objectHit.blitOrder :
                        self.objectHit = object
                    hitList.append(object)
            self.objectsHitChecket.append(object)

    def didColided(self,object):
        if object.type == objectFunction.Type.APPLICATION or object.father.type == objectFunction.Type.APPLICATION :
            if object.father.type == objectFunction.Type.APPLICATION :
                objectFatherPosition = [0,0]
            else :
                objectFatherPosition = object.father.getAbsolutePosition()
            objectFatherPosition = [0,0]
            collidePoint = [
                self.position[0] - objectFatherPosition[0],
                self.position[1] - objectFatherPosition[1]
            ]
            # print(f'Mouse.didColided(): {object.rect.collidepoint(collidePoint)}, object.name = {object.name}, object.position = {object.position}, object.size = {object.size}, mouse.position = {self.position}, collidePoint = {collidePoint}')
        else :
            objectFatherPosition = object.father.getAbsolutePosition()
            collidePoint = [
                self.position[0] - objectFatherPosition[0],
                self.position[1] - objectFatherPosition[1]
            ]
            # print(f'Mouse.didColided(): {object.rect.collidepoint(collidePoint)}, object.name = {object.name}, object.position = {object.position}, object.size = {object.size}, mouse.position = {self.position}, collidePoint = {collidePoint}, objectFatherPosition = {objectFatherPosition}')

        return object.rect.collidepoint(collidePoint)

    def didHit(self,object):
        if object.type == objectFunction.Type.APPLICATION :
            pixelPoint = self.position
            xDiff = self.position[0] - object.position[0]
            yDiff = self.position[1] - object.position[1]
            # print(f'Mouse.didHit(): pixelPoint = {pixelPoint}')
            # print(f'    object.name = {object.name}, object.position = {object.position}, object.size = {object.size}')
            # print(f'    mouse.position = {self.position}', end = '')
            # print(f'    0 < {self.position[0] - object.position[0]} < {object.size[0]} and 0 < {self.position[1] - object.position[1]} < {object.size[1]}')
        else :
            objectPosition = object.getAbsolutePosition()
            pixelPoint = [
                self.position[0] - objectPosition[0],
                self.position[1] - objectPosition[1]
            ]
            xDiff = self.position[0] - objectPosition[0]
            yDiff = self.position[1] - objectPosition[1]
            # print(f'Mouse.didHit(): pixelPoint = {pixelPoint}')
            # print(f'    object.name = {object.name}, objectPosition = {objectPosition}, object.size = {object.size}')
            # print(f'    mouse.position = {self.position}', end = '')
            # print(f'    0 < {self.position[0] - objectPosition[0]} < {object.size[0]} and 0 < {self.position[1] - objectPosition[1]} < {object.size[1]}')
        notHit = True
        if (0 < xDiff and xDiff < object.size[0]) and (0 < yDiff and yDiff < object.size[1]) :
            pixelColor = object.screen.surface.get_at(pixelPoint)
            # print(f', pixelColor = {pixelColor}')
            notHit = (pixelColor[0] == objectFunction.Attribute.NOT_HITTABLE_COLOR[0]) and notHit
            notHit = (pixelColor[1] == objectFunction.Attribute.NOT_HITTABLE_COLOR[1]) and notHit
            notHit = (pixelColor[2] == objectFunction.Attribute.NOT_HITTABLE_COLOR[2]) and notHit
            notHit = (pixelColor[3] == objectFunction.Attribute.NOT_HITTABLE_COLOR[3]) and notHit
        return not notHit

    def resolveClick(self):
        if self.state==mouseFunction.State.LEFT_CLICK_DOWN or self.state==mouseFunction.State.LEFT_CLICK_UP :
            # print(f'Mouse.resolveClick(): Mouse.state = {self.state}, Mouse.scripArea = {self.scripArea}')
            if self.objectHit :
                # print(f'Mouse.resolveClick():   Mouse.objectHit = {self.objectHit.name}')
                # try :
                #     print(f'                        Mouse.objectHitDown = {self.objectHitDown.name}')
                # except : pass
                # try :
                #     print(f'                        Mouse.objectHitUp = {self.objectHitUp.name}')
                # except : pass
                print()
                print('============================================================================================================================================================')
                ClickEvent.ClickEvent(self)
                # printMemoryOptimizationTree(self)
                print('============================================================================================================================================================')
                print()
                # printAllObjectEvents(self.application)
                # printAllObjectNames(self.application)
                # if self.application.session :
                #     print(f'Session.itemNames = {self.application.session.itemNames}')
                # try :
                #     print(f'Application focus name = {self.application.focus.name}')
                # except : pass
                # updateAllObjectsNextFrame(self.application)
            else :
                FalseClickEvent.FalseClickEvent(self.application)

        self.nextState(mouseFunction.State.END_OF_LIFE_CYCLE)

    def updateObjectHover(self):
        self.detectObjectHover()
        if not self.hovering :
            if self.objectHover and self.objectHover == self.lastObjectHover and self.objectHover.type != objectFunction.Type.APPLICATION :
                if self.application.timeNow - self.firstTimeHoveringThisObject > mouseFunction.Attribute.MINIMUM_HOVERING_TIME :
                    self.hovering = self.objectHover
                    HoverEvent.HoverEvent(self.hovering)
            else :
                self.lastObjectHover = self.objectHover
                self.firstTimeHoveringThisObject = self.application.timeNow
        else :
            if self.objectHover and self.objectHover != self.hovering and self.objectHover.type != objectFunction.Type.APPLICATION :
                HoverEvent.HoverEvent(self.hovering)
                self.hovering = None
            # elif self.objectHover and self.objectHover == self.lastObjectHover :
            #     pass
            # # else :
            # #     print(Mouse.ERROR_IN_HOVER_EVENT_DETECTION)
        self.objectHover = None

    def detectObjectHover(self):
        self.getRecursiveHover(self.application)
        self.objectsHoverChecket = []

    def getRecursiveHover(self,object):
        if object.handler.objects :
            objectHoverList = []
            childrenNames = list(object.handler.objects.keys())
            for childName in childrenNames:
                if childName in object.handler.objects :
                    self.updateHoverCheck(object.handler.objects[childName],objectHoverList)
            if objectHoverList :
                for objectHover in objectHoverList :
                    self.getRecursiveHover(objectHover)
        self.updateHoverCheck(object,[])

    def updateHoverCheck(self,object,hoverList):
        if object not in self.objectsHitChecket :
            if self.didColided(object) :
                if self.didHit(object) :
                    if not self.objectHover :
                        self.objectHover = object
                    if object.blitOrder > self.objectHover.blitOrder :
                        self.objectHover = object
                    hoverList.append(object)
            self.objectsHoverChecket.append(object)


    def updateState(self,pgEvent):
        # self.inLifeCicle = True
        # print(f'    pg.mouse.get_pressed() = {pg.mouse.get_pressed()}')
        # print(f'    pg.event.get() = {pg.event.get()}')
        # if pgEvent.type == pg.MOUSEBUTTONDOWN :
        #     print(f'    pgEvent.button = {pgEvent.button}')
        #     if pgEvent.button == 4 :
        #         print(f'    whell up')
        #     elif pgEvent.button == 5 :
        #         print(f'    whell down')
        #################################
        # pg.event.get() - related to exit or enter in application area, ammong possible others
        # pg.mouse.get_pressed()
        # 1- Left click
        # 2- Center click
        # 3- Right click
        # 4- Whell up
        # 5- Whell down
        if pg.mouse.get_pressed() != (0,0,0) :
            # clear()
            pass

        if pg.mouse.get_pressed() == (1,0,0) :
            if pgEvent.type == pg.MOUSEBUTTONDOWN :
                if self.lastBusyState == mouseFunction.State.NOT_BUZY :
                    self.nextState(mouseFunction.State.LEFT_CLICK_DOWN)
                    self.inLifeCicle = True

        if pg.mouse.get_pressed() == (0,0,0) :
            if pgEvent.type == pg.MOUSEBUTTONUP :
                if self.lastBusyState == mouseFunction.State.LEFT_CLICK_DOWN :
                    self.nextState(mouseFunction.State.LEFT_CLICK_UP)
                    self.inLifeCicle = False
            elif self.state != mouseFunction.State.FREE :
                debugText = f'Mouse.updateState():\n'
                debugText += f'Mouse.lastBusyState = {self.lastBusyState}\n'
                debugText += f'Mouse.state = {self.state}\n'
                debugText += f'{mouseFunction.State.INVALID_STATE}\n'
                ErrorEvent.ErrorEvent(None,
                    message = debugText
                )


        if not self.inLifeCicle :
            if self.lastBusyState != mouseFunction.State.NOT_BUZY and self.state != mouseFunction.State.FREE :
                debugText = f'Mouse.updateState():\n'
                debugText += f'Mouse.lastBusyState = {self.lastBusyState}\n'
                debugText += f'Mouse.state = {self.state}\n'
                debugText += f'{mouseFunction.State.INVALID_STATE}\n'
                ErrorEvent.ErrorEvent(None,
                    message = debugText
                )

    def nextState(self,state):

        if state==mouseFunction.State.LEFT_CLICK_DOWN and self.lastBusyState==mouseFunction.State.NOT_BUZY and self.state==mouseFunction.State.FREE :
            self.lastBusyState = mouseFunction.State.NOT_BUZY
            self.state = state
            # print('************************** mouseFunction.State.LEFT_CLICK_DOWN')

        elif state==mouseFunction.State.LEFT_CLICK_UP and self.lastBusyState==mouseFunction.State.LEFT_CLICK_DOWN and self.state==mouseFunction.State.FREE :
            self.lastBusyState = mouseFunction.State.NOT_BUZY
            self.state = state
            # print('************************** mouseFunction.State.LEFT_CLICK_UP')

        elif state==mouseFunction.State.END_OF_LIFE_CYCLE :
            self.objectHit = None
            self.objectsHitChecket = []
            if self.lastBusyState==mouseFunction.State.NOT_BUZY and self.state==mouseFunction.State.LEFT_CLICK_DOWN :
                self.lastBusyState = self.state
                self.state = mouseFunction.State.FREE
                # print('************************** mouseFunction.State.LEFT_CLICK_DOWN resolved')

            elif self.lastBusyState==mouseFunction.State.NOT_BUZY and self.state==mouseFunction.State.LEFT_CLICK_UP :
                self.state = mouseFunction.State.FREE
                self.objectHitDown = None
                self.objectHitUp = None
                # print('************************** mouseFunction.State.LEFT_CLICK_UP resolved')

def printAllObjectEvents(object) :
    print()
    print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
    printObjectEvents(object)
    print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
    print()

def printObjectEvents(object) :
    for objectSon in object.handler.objects.values() :
        printObjectEvents(objectSon)
    events = object.handler.events.values()
    if events :
        print(f'object.name = {object.name}')
        for event in events :
            print(f'    {object.type}.name = {object.name}, {event.type}.name = {event.name}')

def updateAllObjectsNextFrame(object) :
    print()
    print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
    updateObjectsNextFrame(object)
    print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
    print()

def updateObjectsNextFrame(object) :
    object.mustUpdate = True
    print(f'object.name = {object.name}, father.name = {object.father.name}, position = {object.position}, size = {object.size}, blitOrder = {object.blitOrder}')
    for objectSon in object.handler.objects.values() :
        updateObjectsNextFrame(objectSon)

def printMemoryOptimizationTree(mouse) :
    for memoryPackageKey in mouse.application.memoryOptimizer.memoryPackageTree.keys() :
        print(f'memoryPackageKey = {memoryPackageKey}')
        for pageKey in mouse.application.memoryOptimizer.memoryPackageTree[memoryPackageKey].keys() :
             print(f'   pageKey = {pageKey}')
             for memoryPackage in mouse.application.memoryOptimizer.memoryPackageTree[memoryPackageKey][pageKey] :
                 for objectDto in memoryPackage.objectsDto :
                     print(f'       objectDto.name = {objectDto[0][0]}')

def printAllObjectNames(application) :
    print()
    print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
    printObjectNames(application)
    print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
    print()

def printObjectNames(object) :
    for objectSon in object.handler.objects.values() :
        printObjectNames(objectSon)
    print(f'object.name = {object.name}')


# A little black cross. Mouse cursor is 8*8 Pixel, hotspot is at (4, 4).
# the cross is (Read Binary):
# 00011000 => 24
# 00011000
# 00011000
# 11100111 => 231
# 11100111
# 00011000
# 00011000
# and has no AND-Mask.
#
# pygame.mouse.set_cursor((8, 8), (4, 4), (24, 24, 24, 231, 231, 24, 24, 24), (0, 0, 0, 0, 0, 0, 0, 0))
