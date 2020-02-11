import pygame as pg
import os
clear = lambda: os.system('cls')

import Object, ClickEvent

print('Mouse library imported')

class Mouse:

    FREE = 'FREE'
    NOT_BUZY = 'NOT_BUZY'
    LEFT_CLICK_UP = 'LEFT_CLICK_UP'
    LEFT_CLICK_DOWN = 'LEFT_CLICK_DOWN'
    END_OF_LIFE_CYCLE = 'END_OF_LIFE_CYCLE'
    INVALID_STATE = 'INVALID_STATE'

    def __init__(self,application):
        '''
        Mouse.position is pondered by dev screen size'''
        self.application = application
        self.position = [0,0]
        self.devPosition = [0,0]
        self.updatePosition()
        self.scripArea = ''

        self.state = Mouse.FREE
        self.lastBusyState = Mouse.NOT_BUZY
        self.inLifeCicle = False

        self.objectHitDown = None
        self.objectHitUp = None
        self.objectHit = None
        self.objectsHitChecket = []

        self.objectClicked = None


    def update(self):
        self.updatePosition()

    def updatePosition(self):
        ###- It needs some work
        self.position = list(pg.mouse.get_pos())
        self.devPosition[0] = int(self.position[0]*self.application.devResize[0])
        self.devPosition[1] = int(self.position[1]*self.application.devResize[1])

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
                if self.lastBusyState == Mouse.NOT_BUZY :
                    self.nextState(Mouse.LEFT_CLICK_DOWN)
                    # print(f'Mouse.state = {self.state}')
                    self.inLifeCicle = True

        if pg.mouse.get_pressed() == (0,0,0) :
            if pgEvent.type == pg.MOUSEBUTTONUP :
                if self.lastBusyState == Mouse.LEFT_CLICK_DOWN :
                    self.nextState(Mouse.LEFT_CLICK_UP)
                    # print(f'Mouse.state = {self.state}')
                    self.inLifeCicle = False
            elif self.state != Mouse.FREE :
                debugText = f'Mouse.updateState():\n'
                debugText += f'Mouse.lastBusyState = {self.lastBusyState}\n'
                debugText += f'Mouse.state = {self.state}\n'
                debugText += f'{Mouse.INVALID_STATE}\n'
                self.application.holdForDebug(debugText)


        if not self.inLifeCicle :
            if self.lastBusyState != Mouse.NOT_BUZY and self.state != Mouse.FREE :
                debugText = f'Mouse.updateState():\n'
                debugText += f'Mouse.lastBusyState = {self.lastBusyState}\n'
                debugText += f'Mouse.state = {self.state}\n'
                debugText += f'{Mouse.INVALID_STATE}\n'
                self.application.holdForDebug(debugText)

    def nextState(self,state):
        # try :
        #     print(f'mouse.scripArea = {self.scripArea} ------------ Aplication.focus.name = {self.application.focus.name}')
        # except :
        #     print(f'mouse.scripArea = {self.scripArea} ------------ Aplication.focus = {self.application.focus}')
        if state==Mouse.LEFT_CLICK_DOWN and self.lastBusyState==Mouse.NOT_BUZY and self.state==Mouse.FREE :
            self.lastBusyState = Mouse.NOT_BUZY
            self.state = state
            # print('************************** Mouse.LEFT_CLICK_DOWN')

        elif state==Mouse.LEFT_CLICK_UP and self.lastBusyState==Mouse.LEFT_CLICK_DOWN and self.state==Mouse.FREE :
            self.lastBusyState = Mouse.NOT_BUZY
            self.state = state
            # print('************************** Mouse.LEFT_CLICK_UP')

        elif state==Mouse.END_OF_LIFE_CYCLE :
            self.objectHit = None
            self.objectsHitChecket = []

            if self.lastBusyState==Mouse.NOT_BUZY and self.state==Mouse.LEFT_CLICK_DOWN :
                self.lastBusyState = self.state
                self.state = Mouse.FREE
                # print('************************** Mouse.LEFT_CLICK_DOWN resolved')

            elif self.lastBusyState==Mouse.NOT_BUZY and self.state==Mouse.LEFT_CLICK_UP :
                self.state = Mouse.FREE
                self.objectHitDown = None
                self.objectHitUp = None
                # print('************************** Mouse.LEFT_CLICK_UP resolved')

    def handleEvent(self,pgEvent):
        self.updateState(pgEvent)
        if self.state == Mouse.LEFT_CLICK_DOWN :
            self.clickDown()
            self.scripArea = f'{self.devPosition[0]}x{self.devPosition[1]}'

        if self.state == Mouse.LEFT_CLICK_UP :
            self.clickUp()
            self.scripArea += f'x{self.devPosition[0]}x{self.devPosition[1]}'
        self.resolveClick()

    def clickDown(self):
        self.getRecursiveColision(self.application)
        # print(f'mouse.objectHitDown = {self.objectHit}')
        # if self.objectHit :
        #     print(f'    mouse.objectHitDown.name = {self.objectHit.name}, type = {self.objectHit.type}')
        self.objectHitDown = self.objectHit

    def clickUp(self):
        self.getRecursiveColision(self.application)
        # print(f'mouse.objectHitUp = {self.objectHit}')
        # if self.objectHit :
        #     print(f'    mouse.objectHitUp.name = {self.objectHit.name}, type = {self.objectHit.type}')
        self.objectHitUp = self.objectHit

    def getRecursiveColision(self,object):
        if object.handler.objects.values() :
            objectHitList = []
            # print(f'{object.name} sons:')
            # for objectSon in object.handler.objects.values() :
            #     print(f'    {objectSon.name}')
            for objectSon in object.handler.objects.values() :
                self.updateColision(objectSon,objectHitList)
            # print(f'\n\n//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-{object.name}: getRecursiveColision()')
            # for obj in objectHitList :
            #     print(f'obj.name = {obj.name}')
            # print(f'//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-{object.name}: end of getRecursiveColision()\n\n')
            if objectHitList :
                for objectHit in objectHitList :
                    self.getRecursiveColision(objectHit)
        self.updateColision(object,[])

    def updateColision(self,object,hitList):
        if object not in self.objectsHitChecket :
            # print(f'''        {object.name} object in colision test
            # object.rect = {object.rect}, mouse.position = {self.position}''')
            if self.didColided(object) :
                hitList.append(object)
                # print(f'\n\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\{object.name}: getRecursiveColision()')
                # for obj in hitList :
                #     print(f'obj.name = {obj.name}')
                # print(f'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\{object.name}: end of getRecursiveColision()\n\n')
                object.updateHitStatus(self.didHit(object))
                # print(f'{object.name}.hit = {object.hit}')
                if object.hit :
                    if not self.objectHit :
                        self.objectHit = object
                    if object.blitOrder > self.objectHit.blitOrder :
                        self.objectHit.updateHitStatus(False)
                        self.objectHit = object
            self.objectsHitChecket.append(object)

    def didColided(self,object):
        return (object.type==Object.ObjectType.APPLICATION and object.rect.collidepoint([
                self.position[0]+object.rect[0],
                self.position[1]+object.rect[1]
            ])) or object.rect.collidepoint(self.position)

    def didHit(self,object):
        # print(f'            Mouse.didHit(): object.name = {object.name}, Mouse.position = {self.position}, object.rect = {object.rect}, object.screen.surface = {object.screen.surface}')
        if object.type==Object.ObjectType.APPLICATION :
            pixelColor = object.screen.surface.get_at([
                self.position[0],
                self.position[1]
            ])
        else :
            pixelColor = object.screen.surface.get_at([
                self.position[0]-object.position[0],
                self.position[1]-object.position[1]
            ])
        notHit = True
        notHit = (pixelColor[0] == Object.Object.NOT_HITTABLE_COLOR[0]) and notHit
        notHit = (pixelColor[1] == Object.Object.NOT_HITTABLE_COLOR[1]) and notHit
        notHit = (pixelColor[2] == Object.Object.NOT_HITTABLE_COLOR[2]) and notHit
        notHit = (pixelColor[3] == Object.Object.NOT_HITTABLE_COLOR[3]) and notHit
        # print(f'            object hit name = {object.name}, pixelColor = {pixelColor}')
        # if notHit :
            # print(f"                {object.name} wasn' hit by mouse")
        # else :
            # print(f'                {object.name} was hit by mouse')
        return not notHit

    def resolveClick(self):
        # if self.state != Mouse.FREE :
            # print(f'Mouse.state = {self.state}')
            # try :
            #     print(f'Mouse.objectHitDown.name = {self.objectHitDown.name}')
            # except : pass
            # try :
            #     print(f'Mouse.objectHitUp.name = {self.objectHitUp.name}')
            # except : pass
        if self.state==Mouse.LEFT_CLICK_UP or self.state==Mouse.LEFT_CLICK_DOWN :
            # print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
            ClickEvent.ClickEvent(self)

        self.nextState(Mouse.END_OF_LIFE_CYCLE)

    def removeFocus(self) :
        if self.application.focus :
            print(f'Mouse.removeFocus(): application.focus.name = {self.application.focus.name}')
            print(f'Mouse.removeFocus(): application.focus.father.name = {self.application.focus.father.name}')
            print(f'Mouse.removeFocus(): application.focus.tutor.name = {self.application.focus.tutor.name}')
            # print(f'Aplication.focus.name = {self.application.focus.name}')
            if not self.hittingApplicationFocusChild(self.objectHit) :
                self.application.removeFocus()

    def hittingApplicationFocusChild(self,object):
        if object.father == self.application.focus :
            return True
        elif (
                object.father.type == Object.ObjectType.APPLICATION and
                object.father.tutor.type == Object.ObjectType.APPLICATION
            ) :
            return False
        elif (
                object.father.type == Object.ObjectType.APPLICATION and
                object.father.tutor.type != Object.ObjectType.APPLICATION
            ) :
            return self.hittingApplicationFocusChild(object.father)
        else :
            return self.hittingApplicationFocusChild(object.tutor)



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
