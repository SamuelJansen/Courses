from function import importMannanger
userPath = importMannanger.makeAplicationLibrariesAvaliable()
from model import Game
from model.course import Course
from model import Plataform
import os
import pygame as pg
import time as now
import numpy as np
from model import Game, Object, Cenario, ArrowKey, Screen, Mouse, Frame

plataformName = 'courses_plataform'
colors =    {
            'black' : (0,0,0),
            'white' : (255,255,255),
            'backgroundColor' : (237,201,202),
            'red' : (255,0,0)
            }
fps = 30
aps = 30
plataform = Plataform.Plataform(plataformName,fps,aps,colors)

objectName = '1'
objectFolder = ''
objectPosition = [0,0]
objectSize = plataform.app.size
objectScale = 1000
objectVelocity = .0001
Object.Object(
    objectName,
    objectFolder,
    objectPosition,
    objectSize,
    objectScale,
    objectVelocity,
    plataform.app
)

arrow = ArrowKey.ArrowKey()
mouse = Mouse.Mouse(plataform.app)
move = [np.random.randint(3)-1,np.random.randint(3)-1]

plataform.app.createFrame(now.time())
while plataform.app.playing :

    if plataform.app.frame.apfNew :
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                game.playing = False
            arrow.events(event)
            mouse.events(event)
            """
            if a.arrows[1]==-1 :
                gl.playSound(upSound)
            if a.arrows[1]==1 :
                gl.playSound(downSound)
            if a.arrows[0]==1 :
                gl.playMusic('Sounds/TakeaWalk.mp3')
            if a.arrows[0]==-1 :
                gl.playSound(leftSound)
            #"""

        plataform.app.updateSpaceCostRectList()

    plataform.app.update(now.time())

pg.quit()
#sys.exit()
