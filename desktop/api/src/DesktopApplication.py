from function import importMannanger
pathMannanger = importMannanger.updateImportMannger()
from function import importMannanger

from model.course import Course
from model.user import ApplicationUser
from model import Plataform
from function.performance_measurement import makePagesFunction, makeScriptFunction

import os
import pygame as pg
import time as now
import numpy as np
import ArrowKey, Object
import imageFunction

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
aplicationUser = AplicationUser.AplicationUser(aplicationUserRegistration,aplicationUserPassword,plataform,coursesName=coursesName)

arrow = ArrowKey.ArrowKey()
mouse = Mouse.Mouse(plataform)
move = [np.random.randint(3)-1,np.random.randint(3)-1]

plataform.run(arrow)
