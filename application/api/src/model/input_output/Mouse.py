import pygame as pg

import Object, Button, Event

print('Mouse library imported')

class Mouse:

    FREE = 'FREE'
    LEFT_CLICK_UP = 'CLICK_UP'
    LEFT_CLICK_DOWN = 'CLICK_DOWN'

    def __init__(self,aplication):
        '''
        Mouse.position is pondered by dev screen size'''
        self.aplication = aplication
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
        self.devPosition[0] = int(self.position[0]*self.aplication.devResize[0])
        self.devPosition[1] = int(self.position[1]*self.aplication.devResize[1])
        # self.setPosition(self.position)

    def update(self):
        self.updatePosition()

    def newEvent(self,pgEvent):
        self.hit = None
        print(f'    pg.mouse.get_pressed() = {pg.mouse.get_pressed()}')
        print(f'    pg.event.get() = {pg.event.get()}')
        if pgEvent.type == pg.MOUSEBUTTONDOWN :
            print(f'    pgEvent.button = {pgEvent.button}')
            if pgEvent.button == 4 :
                print(f'    whell up')
            elif pgEvent.button == 5 :
                print(f'    whell down')
        if pgEvent.type == pg.MOUSEBUTTONDOWN :
            self.clickDown()
            self.scripArea = f'{self.devPosition[0]}x{self.devPosition[1]}'

        if pgEvent.type == pg.MOUSEBUTTONUP :
            self.clickUp()
            self.scripArea += f'x{self.devPosition[0]}x{self.devPosition[1]}'
            try :
                print(f'mouse.scripArea = {self.scripArea} ------------ Aplication.focus.name = {self.aplication.focus.name}')
            except :
                print(f'mouse.scripArea = {self.scripArea} ------------ Aplication.focus = {self.aplication.focus}')
            self.resolveClick()

    def clickDown(self):
        self.state = Mouse.LEFT_CLICK_DOWN
        self.getRecursiveColision(self.aplication)
        # print(f'mouse.objectHitClickDown = {self.hit}')
        if self.hit :
            print(f'    mouse.objectHitClickDown.name = {self.hit.name}, type = {self.hit.type}')
        self.objectHitClickDown = self.hit

    def clickUp(self):
        self.state = Mouse.LEFT_CLICK_UP
        self.getRecursiveColision(self.aplication)
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
            print(f'mouse colided with {object.name}')
            if object.handler.isSelected(self.position) :
                return object

    def resolveClick(self):
        self.objectSelected = self.objectHitClickUp
        if self.objectSelected and self.objectHitClickDown == self.objectHitClickUp :
            print(f'  objectClicked.name = {self.objectSelected.name}')

            if self.aplication.focus and self.aplication.focus!=self.objectSelected :
                self.removeFocus()
            else :
                self.action(self.objectSelected)
        else :
            self.removeFocus()

    def removeFocus(self) :
        if self.aplication.focus :
            print(f'Aplication.focus.name = {self.aplication.focus.name}')
            self.aplication.focus.father.handler.deleteObject(self.aplication.focus.name)
        self.aplication.focus = None
        self.objectSelected = None

    def action(self,object):
        event = Event.Event(object)
        if event.className == Event.Event.BUTTON :
            object.run(event)




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
