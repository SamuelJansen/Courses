from domain.control import PathMannanger
pathMannanger = PathMannanger.PathMannanger()

from model.course import Course
from model.user import ApplicationUser

from domain import Plataform
from function.performance_measurement import makePagesFunction, makeScriptFunction

import os
import numpy as np
import ArrowKey, Object
import imageFunction

plataformName = 'desktop'
colors =    {
            'black' : (0,0,0),
            'white' : (255,255,255),
            'backgroundColor' : (237,201,202),
            'red' : (255,0,0)
            }
fps = 30
aps = 30
plataform = Plataform.Plataform(plataformName,fps,aps,colors,pathMannanger,
    floor = False
)

objectName = '1'
objectPosition = [0,0]
objectSize = plataform.size
objectScale = 1000
objectVelocity = .0001
father = plataform
Object.Object(
    objectName,
    objectPosition,
    objectSize,
    objectScale,
    objectVelocity,
    father
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
aplicationUser = ApplicationUser.ApplicationUser(aplicationUserRegistration,aplicationUserPassword,plataform,coursesName=coursesName)

arrow = ArrowKey.ArrowKey()
move = [np.random.randint(3)-1,np.random.randint(3)-1]

plataform.run(arrow)
