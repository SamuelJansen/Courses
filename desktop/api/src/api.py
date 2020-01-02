def makeAplicationLibrariesAvaliable() :
    baseApiPath = 'api/src/'
    from pathlib import Path
    userPath = str(Path.home())
    import sys
    sys.path.append(userPath+'/Morgs/')
    sys.path.append(userPath+'/Courses/course/'+baseApiPath)

makeAplicationLibrariesAvaliable()
from model import Game
from model.course import Course
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
game = Game.Game(plataformName,fps,aps,colors)

objectName = '1'
objectFolder = ''
objectPosition = [0,0]
objectSize = game.size
objectScale = 1000
objectVelocity = .0001
Object.Object(
    objectName,
    objectFolder,
    objectPosition,
    objectSize,
    objectScale,
    objectVelocity,
    game
)

arrow = ArrowKey.ArrowKey()
mouse = Mouse.Mouse(game)
move = [np.random.randint(3)-1,np.random.randint(3)-1]

game.createFrame(now.time())
while game.playing :

    if game.frame.apfNew :
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

        game.updateSpaceCostRectList()

    game.update(now.time())

pg.quit()
#sys.exit()
