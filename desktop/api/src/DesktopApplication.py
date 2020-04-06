from domain.control import PathMannanger

if __name__ == '__main__' :
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

registration = '000001'
password = 'abcd1234'
courseNames = ['macro_2020_03 1']

# aplicationUser = ApplicationUser.ApplicationUser(registration,password,plataform,
#     courseNames = courseNames
# )
plataform.setApplicationUser(registration,password)
plataform.buildPage()



arrow = ArrowKey.ArrowKey()
move = [np.random.randint(3)-1,np.random.randint(3)-1]

plataform.run(arrow)
