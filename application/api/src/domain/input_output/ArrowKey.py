import pygame as pg

print('ArrowKey library imported')

class ArrowKey:
    def __init__(self):
        self.status = [0,0]

    def newEvent(self,pgEvent):
        if pgEvent.type==pg.KEYDOWN :
            if pgEvent.key==pg.K_LEFT :
                self.status[0] = -1
            elif pgEvent.key==pg.K_RIGHT :
                self.status[0] = 1
        if pgEvent.type==pg.KEYDOWN :
            if pgEvent.key==pg.K_UP :
                self.status[1] = -1
            elif pgEvent.key==pg.K_DOWN :
                self.status[1] = 1
        if pgEvent.type==pg.KEYUP  :
            if pg.key.get_pressed()[pg.K_LEFT] and not pg.key.get_pressed()[pg.K_RIGHT] :
                self.status[0] = -1
            elif pg.key.get_pressed()[pg.K_RIGHT] and not pg.key.get_pressed()[pg.K_LEFT] :
                self.status[0] = 1
            elif not pg.key.get_pressed()[pg.K_LEFT] and not pg.key.get_pressed()[pg.K_RIGHT] :
                self.status[0] = 0
        if pgEvent.type==pg.KEYUP  :
            if pg.key.get_pressed()[pg.K_UP] and not pg.key.get_pressed()[pg.K_DOWN] :
                self.status[1] = -1
            elif pg.key.get_pressed()[pg.K_DOWN] and not pg.key.get_pressed()[pg.K_UP] :
                self.status[1] = 1
            elif not pg.key.get_pressed()[pg.K_UP] and not pg.key.get_pressed()[pg.K_DOWN] :
                self.status[1] = 0
