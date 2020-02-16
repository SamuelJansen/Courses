import eventFunction, objectFunction

import ItemSet
from model.course import Module

def openModule(event) :

    modulesPath = f'{event.object.application.pathMannanger.getApiModulePath("course")}{Module.Module.MODULE_PATH}{Module.Module.MODULES_FILE}'
    modules = []
    with open(modulesPath,"r",encoding="utf-8") as modulesFile :
        for module in modulesFile :
            modules.append(module.strip())

    name = 'modulesItemSet'
    # position = event.object.position.copy()
    position = event.object.getAbsolutePosition()
    itemsFunctionKey = 'resolveModuleClick'
    father = event.object
    event.object.application.setFocus(
        ItemSet.ItemSet(name,position,father,
            itemsName = modules,
            itemsText = modules,
            itemSize = [240,20],
            itemDirection = ItemSet.ItemSet.DOWN,
            itemsFunctionKey = itemsFunctionKey,
            noImage = True,
            imagePath = None,
            soundPath = None
        )
    )

    event.status = eventFunction.Status.NOT_RESOLVED

    # print(f'    new Application.focus = {event.object.application.focus.name}')
    print(f'    Event called: {event.object.name}.openModule({event.object.application.name})')
