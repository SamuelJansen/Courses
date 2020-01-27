from model import Aplication
from model.course import Module
from model.object.user_interface import ItemsSetCollumn

import pygame as pg

def openModule(event) :
    modulesPath = f'{event.object.aplication.pathMannanger.getApiModulePath("course")}{Module.Module.MODULES_FILE}'
    modules = []
    with open(modulesPath,"r",encoding="utf-8") as modulesFile :
        for line in modulesFile :
            modules.append(line.strip())
    print(modules)

    name = 'moduleCollumn'
    object = event.object

    print(f'object.name = {object.name}, object.father.name = {object.father.name}')

    position = object.position
    size = [240,20*len(modules)+object.size[1]]

    print(f'object.father.size = {object.father.size}')


    father = object
    userInterface = ItemsSetCollumn.ItemsSetCollumn(name,position,size,father,
        padding = [2,2],
        noImage = True,
        imagePath = None,
        soundPath = None
    )

    pg.font.init()
    myfont = pg.font.SysFont('Comic Sans MS', 18)

    for indexModuleName in range(len(modules)) :
        courseNameSurface = myfont.render(modules[indexModuleName],False,(0, 0, 0))
        userInterface.screen.surface.blit(courseNameSurface,(2,+father.size[1]-4+indexModuleName*20))
    userInterface.screen.mustUpdateNextFrame()



    print(f'    EventFunction called: openModule({event.object.aplication.name})')
