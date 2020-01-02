def makeAplicationLibrariesAvaliable() :
    from pathlib import Path
    userPath = str(Path.home())
    import sys
    sys.path.append(userPath+'/Morgs/')
    sys.path.append(userPath+'/Morgs/')

makeAplicationLibrariesAvaliable()
from model import Game
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
