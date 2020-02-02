import pygame as pg

import ItemsSet

from model.course import Module

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

    print(f'object.father.size = {object.father.size}')

    itemsFunctionKey = 'resolveSelection'
    father = object
    userInterface = ItemsSet.ItemsSet(name,position,itemsFunctionKey,father,
        itemsName = modules,
        itemsText = modules,
        itemSize = [240,20],
        noImage = True,
        imagePath = None,
        soundPath = None
    )

    object.aplication.focus = userInterface
    print(f'    new Application.focus = {object.aplication.focus.name}')

        # courseNameSurface = myfont.render(modules[indexModuleName],False,(0, 0, 0))
        # userInterface.addText(modules[moduleIndex],[2,+father.size[1]-4+moduleIndex*20])
        # userInterface.screen.surface.blit(courseNameSurface,)
    # userInterface.screen.mustUpdateNextFrame()

    print(f'        EventFunction called: openModule({event.object.aplication.name})')
