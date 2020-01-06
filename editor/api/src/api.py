from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model.course import Course
from model.user import AplicationUser
from model import Editor
import os
import pygame as pg
import time as now
import numpy as np
from model import ArrowKey,Mouse,Object

editorName = 'editor_mode'
colors =    {
            'black' : (0,0,0),
            'white' : (255,255,255),
            'backgroundColor' : (237,201,202),
            'red' : (255,0,0)
            }
fps = 30
aps = 30
editorPosition = (600,0)
editor = Editor.Editor(editorName,fps,aps,colors,
    position = editorPosition
)

arrow = ArrowKey.ArrowKey()
mouse = Mouse.Mouse(editor)
move = [np.random.randint(3)-1,np.random.randint(3)-1]

editor.createFrame(now.time())
while editor.playing :

    if editor.frame.apfNew :
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                editor.playing = False
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

        editor.updateSpaceCostRectList()

    editor.update(now.time())

pg.quit()
#sys.exit()
