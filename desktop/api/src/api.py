from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model.course import Course
from model.user import AplicationUser
from model import Plataform
import os
import pygame as pg
import time as now
import numpy as np
from model import ArrowKey,Mouse,Object
from function import imageFunction
from function.performance_measurement import makePagesFunction,makeScriptFunction

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
objectPosition = [0,0]
objectSize = plataform.size
objectScale = 1000
objectVelocity = .0001
father=None
Object.Object(
    objectName,
    objectPosition,
    objectSize,
    objectScale,
    objectVelocity,
    plataform,
    plataform
)

courseName = 'macro_2020_03'
moduleName = 'assistente_administrativo'
lessonName = 'aula_01'
amountOfPagesToMake = 1
makePagesFunction.makeSoManyPages(courseName,moduleName,lessonName,amountOfPagesToMake,plataform)
makeScriptFunction.makeAScript(courseName,moduleName,lessonName,amountOfPagesToMake,plataform)

coursesName = [courseName]
aplicationUserRegistration = '000000'
aplicationUserPassword = '123'
aplicationUser = AplicationUser.AplicationUser(aplicationUserRegistration,aplicationUserPassword,coursesName=coursesName)

arrow = ArrowKey.ArrowKey()
mouse = Mouse.Mouse(plataform)
move = [np.random.randint(3)-1,np.random.randint(3)-1]

plataform.initialize(now.time())
while plataform.running :

    if plataform.frame.apfNew :
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                plataform.running = False
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

        plataform.objectHandler.update()

    plataform.update(now.time())

pg.quit()
#sys.exit()
