import Object
import eventFunction

def openModule(event) :

    if requestingAttributes(event) :
        return getAttributes(event)

    import ItemSet
    from model.course import Module

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

    event.status = eventFunction.EventStatus.NOT_RESOLVED

    # print(f'    new Application.focus = {event.object.application.focus.name}')
    print(f'    EventFunction called: {event.object.name}.openModule({event.object.application.name})')


def requestingAttributes(event):
    return type(event) == type('')

def getAttributes(type) :
    if type == Object.Object.SINGLE_CLICKABLE : return True
    if type == Object.Object.DOUBLE_CLICKABLE : return False
    return None
