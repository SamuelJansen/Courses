from model import Aplication
from model.course import Module
from model.object.user_interface import UserInterfaceSurface

import pygame as pg

def openModule(event) :
    modulesPath = f'{event.object.aplication.pathMannanger.getApiModulePath("course")}{Module.Module.MODULES_FILE}'
    modules = []
    with open(modulesPath,"r",encoding="utf-8") as modulesFile :
        for line in modulesFile :
            modules.append(line.strip())
    print(modules)

    # name = 'moduleCollumn'
    # object = event.object
    # position = [object.position[0],object.position[1]]
    # print(position)
    # size = [140,20*len(modules)+object.size[1]]
    # father = object.aplication.objectHandler.objects[Aplication.Aplication.FLOOR]#.objectHandler.objects['headerSurface'].objectHandler.objects['openModule']

    name = 'moduleCollumn'
    object = event.object

    print(f'object.name = {object.name}, object.father.name = {object.father.name}')

    position = [0,object.father.size[1]]
    print(position)
    size = [140,20*len(modules)]
    father = event.object.aplication.objectHandler.objects[Aplication.Aplication.FLOOR]#.objectHandler.objects['headerSurface'].objectHandler.objects['openModule']

    userInterface = UserInterfaceSurface.UserInterfaceSurface(name,position,size,father,
        padding = [2,2],
        imagePath = None,
        soundPath = None
    )

    pg.font.init()
    myfont = pg.font.SysFont('Comic Sans MS', 18)
    courseNameSurface = myfont.render('modules[0]',False,(0, 0, 0))

    print(f'userInterface.father.name = {userInterface.father.name}')
    for object in userInterface.father.objectHandler.objects.values() :
        print(f'   father child = {object.name}')

    event.object.aplication.objectHandler.objects[Aplication.Aplication.FLOOR].objectHandler.objects['moduleCollumn'].image.blit(courseNameSurface,(2,2))
    event.object.aplication.objectHandler.objects[Aplication.Aplication.FLOOR].objectHandler.objects['moduleCollumn'].screen.newSurface()
    event.object.aplication.objectHandler.objects[Aplication.Aplication.FLOOR].objectHandler.objects['moduleCollumn'].screen.mustUpdateNextFrame()

    print(f'    EventFunction called: openModule({event.object.aplication.name})')
    pass
