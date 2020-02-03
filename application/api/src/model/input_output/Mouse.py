import pygame as pg

import Object, SelectionEvent

print('Mouse library imported')

class Mouse:

    FREE = 'FREE'
    LEFT_CLICK_UP = 'LEFT_CLICK_UP'
    LEFT_CLICK_DOWN = 'LEFT_CLICK_DOWN'

    def __init__(self,application):
        '''
        Mouse.position is pondered by dev screen size'''
        self.application = application
        self.position = [0,0]
        self.devPosition = [0,0]
        self.updatePosition()
        self.scripArea = ''

        self.state = None

        self.objectHitClickDown = None
        self.objectHitClickUp = None
        self.hit = None
        self.objectSelected = None

    def updatePosition(self):
        ###- It needs some work
        self.position = list(pg.mouse.get_pos())
        self.devPosition[0] = int(self.position[0]*self.application.devResize[0])
        self.devPosition[1] = int(self.position[1]*self.application.devResize[1])

    def update(self):
        self.updatePosition()

    def handleEvent(self,pgEvent):
        # print(f'    pg.mouse.get_pressed() = {pg.mouse.get_pressed()}')
        # print(f'    pg.event.get() = {pg.event.get()}')
        # if pgEvent.type == pg.MOUSEBUTTONDOWN :
        #     print(f'    pgEvent.button = {pgEvent.button}')
        #     if pgEvent.button == 4 :
        #         print(f'    whell up')
        #     elif pgEvent.button == 5 :
        #         print(f'    whell down')
        if pgEvent.type == pg.MOUSEBUTTONDOWN :
            self.clickDown()
            self.scripArea = f'{self.devPosition[0]}x{self.devPosition[1]}'

        if pgEvent.type == pg.MOUSEBUTTONUP :
            self.clickUp()
            self.scripArea += f'x{self.devPosition[0]}x{self.devPosition[1]}'
            try :
                print(f'mouse.scripArea = {self.scripArea} ------------ Aplication.focus.name = {self.application.focus.name}')
            except :
                print(f'mouse.scripArea = {self.scripArea} ------------ Aplication.focus = {self.application.focus}')
        self.resolveClick()

    def clickDown(self):
        self.state = Mouse.LEFT_CLICK_DOWN
        self.getRecursiveColision(self.application)
        # print(f'mouse.objectHitClickDown = {self.hit}')
        if self.hit :
            print(f'    mouse.objectHitClickDown.name = {self.hit.name}, type = {self.hit.type}')
        self.objectHitClickDown = self.hit

    def clickUp(self):
        self.state = Mouse.LEFT_CLICK_UP
        self.getRecursiveColision(self.application)
        # print(f'mouse.objectHitClickUp = {self.hit}')
        if self.hit :
            print(f'    mouse.objectHitClickUp.name = {self.hit.name}, type = {self.hit.type}')
        self.objectHitClickUp = self.hit

    def getRecursiveColision(self,object):
        if object.handler.objects.values() :
            objectHitList = []
            for objectSon in object.handler.objects.values() :
                objectHit = self.getColision(objectSon)
                if objectHit :
                    objectHitList.append(objectHit)
            if objectHitList :
                for objectHit in objectHitList :
                    self.getRecursiveColision(objectHit)
            objectHit = self.getColision(object)
            if objectHit :
                if not self.hit :
                    self.hit = objectHit
                elif objectHit.blitOrder > self.hit.blitOrder :
                    self.hit = objectHit
        else :
            objectHit = self.getColision(object)
            if objectHit :
                if (not self.hit) or (objectHit.blitOrder > self.hit.blitOrder) :
                    self.hit = objectHit

    def getColision(self,object):
        print(f'{object.name} object in colision test, object.rect = {object.rect}, mouse.position = {self.position}')
        if object.rect.collidepoint(self.position) :
            print(f'mouse collided with {object.name}')
            object.updateSelectionStatus( self.didSelected(object) )
            if object.isSelected :
                return object

    def didSelected(self,object):
        if object.selectable :
            try :
                notSelected = True
                pixelColor = object.screen.surface.get_at(self.position)
                notSelected = (pixelColor[0] == Object.Object.NOT_SELECTABLE_COLOR[0]) and notSelected
                notSelected = (pixelColor[1] == Object.Object.NOT_SELECTABLE_COLOR[1]) and notSelected
                notSelected = (pixelColor[2] == Object.Object.NOT_SELECTABLE_COLOR[2]) and notSelected
                notSelected = (pixelColor[3] == Object.Object.NOT_SELECTABLE_COLOR[3]) and notSelected
                print(f'object hit name = {object.name}, pixelColor = {pixelColor}')
                print(f'    notSelected = {notSelected}')
                return not notSelected
            except :
                print(f'    it was selected')
                return True

    def resolveClick(self):
        if self.objectHitClickDown == self.objectHitClickUp :
            self.objectSelected = self.objectHitClickUp

        SelectionEvent.SelectionEvent(self)

        self.objectSelected = None
        self.state = Mouse.FREE
        self.hit = None

    def removeFocus(self) :
        if self.application.focus :
            print(f'Aplication.focus.name = {self.application.focus.name}')
            self.application.focus.father.handler.deleteObject(self.application.focus.name)
        self.application.focus = None
        self.objectSelected = None


#################################
# pg.mouse.get_pressed()
# 1- Left click
# 2- Center click
# 3- Right click
# 4- Whell up
# 5- Whell down

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
