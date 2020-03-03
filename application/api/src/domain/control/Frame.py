import pygame as pg

import TimeErrorControl

class Frame:

    def update(self):
        #- dealling with frame control
        self.new = False
        self.newSecond = False
        if self.aplication.timeNow > self.timeNext :
            self.new = True
            self.timeError += self.correctionFactor * (self.aplication.timeNow - self.timeNext - self.timeError)
            if self.timeError<0 :
                self.timeError = 0
            elif self.timeError > 1 :
                self.timeError = .95
            if self.counter<self.aplication.fps-1 :
                self.counter += 1
            else :
                self.newSecond = True
                self.counter = 0
            error = self.timeOveralError * self.width + self.timeError
            self.timeNext = self.aplication.timeNow + self.width - error
            self.fpsCounter += 1
        #- Dealling with apf's time erros
        if self.aplication.timeNow > self.apfTimeNext :
            self.apfNew = True
            self.apsCounter += 1
            self.apfTimeError += self.correctionFactor * (self.aplication.timeNow - self.apfTimeNext - self.apfTimeError)
            if self.apfTimeError<0 :
                self.apfTimeError = 0
            elif self.apfTimeError > 1 :
                self.apfTimeError = .95
            if self.apfCounter < self.apf-1 :
                self.apfCounter += 1
            else :
                self.apfCounter = 0
            self.apfTimeNext = self.aplication.timeNow + self.apfWidth - self.apfTimeError
        else :
            self.apfNew = False
        #- Dealling with time erros
        self.timeErrorControl.checkTimeError()
        if self.newSecond :
            self.fpsCounter = 0
            self.apsCounter = 0

    def __init__(self,aplication):
        self.aplication = aplication
        self.newSecond = True
        #- Frame stuffs
        self.counter = 0
        self.new = True
        self.width = 1 / self.aplication.fps
        self.timeNext = self.aplication.timeNow + self.width
        #- Frame stuffs
        self.fpsCounter = 0
        self.apsCounter = 0
        #- Actions per frame. It was much simpler to implement
        self.apf = self.aplication.aps/self.aplication.fps
        self.apfWidth = self.width / self.apf
        self.apfCounter = 0
        self.apfNew = True
        self.apfTimeNext = self.aplication.timeNow + self.apfWidth
        #- Time issues
        self.timeError = 0
        self.apfTimeError = 0
        self.timeOveralError = 0
        self.correctionFactor = .6
        #- External time corrector
        self.timeErrorControl = TimeErrorControl.TimeErrorControl(self,self.aplication)
