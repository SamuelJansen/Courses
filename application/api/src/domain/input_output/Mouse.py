import pygame as pg

import ClickEvent, FalseClickEvent
import objectFunction, mouseFunction, applicationFunction

print('Mouse library imported')

class Mouse:

    def update(self):
        self.updatePosition()

    def __init__(self,application):
        '''
        Mouse.position is pondered by dev screen size'''
        self.application = application
        self.position = [0,0]
        self.devPosition = [0,0]
        self.updatePosition()
        self.scripArea = ''

        self.state = mouseFunction.State.FREE
        self.lastBusyState = mouseFunction.State.NOT_BUZY
        self.inLifeCicle = False

        self.objectHitDown = None
        self.objectHitUp = None
        self.objectHit = None
        self.objectsHitChecket = []

        self.objectClicked = None

    def updatePosition(self):
        ###- It needs some work
        self.position = list(pg.mouse.get_pos())
        self.devPosition[0] = int(self.position[0]*self.application.devResize[0])
        self.devPosition[1] = int(self.position[1]*self.application.devResize[1])

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
            # print(f'Mouse.didHit(): pixelPoint = {pixelPoint}, object.name = {object.name}, object.position = {object.position}, object.size = {object.size}, mouse.position = {self.position}', end = '')
        else :
            objectPosition = object.getAbsolutePosition()
            pixelPoint = [
                self.position[0] - objectPosition[0],
                self.position[1] - objectPosition[1]
            ]
            # print(f'Mouse.didHit(): pixelPoint = {pixelPoint}, object.name = {object.name}, objectPosition = {objectPosition}, object.size = {object.size}, mouse.position = {self.position}', end = '')
        pixelColor = object.screen.surface.get_at(pixelPoint)
        # print(f', pixelColor = {pixelColor}')
        notHit = True
        notHit = (pixelColor[0] == objectFunction.Attribute.NOT_HITTABLE_COLOR[0]) and notHit
        notHit = (pixelColor[1] == objectFunction.Attribute.NOT_HITTABLE_COLOR[1]) and notHit
        notHit = (pixelColor[2] == objectFunction.Attribute.NOT_HITTABLE_COLOR[2]) and notHit
        notHit = (pixelColor[3] == objectFunction.Attribute.NOT_HITTABLE_COLOR[3]) and notHit
        return not notHit

    def resolveClick(self):
        if self.state==mouseFunction.State.LEFT_CLICK_DOWN or self.state==mouseFunction.State.LEFT_CLICK_UP :
            print(f'Mouse.resolveClick(): Mouse.state = {self.state}, Mouse.scripArea = {self.scripArea}')
            if self.objectHit :
                # print(f'Mouse.resolveClick():   Mouse.objectHit = {self.objectHit.name}')
                # try :
                #     print(f'                        Mouse.objectHitDown = {self.objectHitDown.name}')
                # except : pass
                # try :
                #     print(f'                        Mouse.objectHitUp = {self.objectHitUp.name}')
                # except : pass
                # print()
                # print('============================================================================================================================================================')
                ClickEvent.ClickEvent(self)
                # print('============================================================================================================================================================')
                # print()
                # printAllObjectEvents(self.application)

            else :
                FalseClickEvent.FalseClickEvent(self.application)

        self.nextState(mouseFunction.State.END_OF_LIFE_CYCLE)


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
                applicationFunction.holdForDebug(debugText)


        if not self.inLifeCicle :
            if self.lastBusyState != mouseFunction.State.NOT_BUZY and self.state != mouseFunction.State.FREE :
                debugText = f'Mouse.updateState():\n'
                debugText += f'Mouse.lastBusyState = {self.lastBusyState}\n'
                debugText += f'Mouse.state = {self.state}\n'
                debugText += f'{mouseFunction.State.INVALID_STATE}\n'
                applicationFunction.holdForDebug(debugText)

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
    for event in object.handler.events.values() :
        print(f'{object.type}.name = {object.name}, {event.type}.name = {event.name}')

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
