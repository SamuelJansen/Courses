from domain.control import PathMannanger
pathMannanger = PathMannanger.PathMannanger()

import os
import numpy as np

import Course, ApplicationUser

import Plataform

import ArrowKey

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

aplicationUser = ApplicationUser.ApplicationUser(aplicationUserRegistration,aplicationUserPassword,plataform,coursesName=coursesName)

arrow = ArrowKey.ArrowKey()
move = [np.random.randint(3)-1,np.random.randint(3)-1]

plataform.run(arrow)
