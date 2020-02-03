import Object

def openModule(event) :

    if requestingAttributes(event) :
        return getAttributes(event)
    import ItemSet, Event
    from model.course import Module

    modulesPath = f'{event.object.application.pathMannanger.getApiModulePath("course")}{Module.Module.MODULES_FILE}'
    modules = []
    with open(modulesPath,"r",encoding="utf-8") as modulesFile :
        for line in modulesFile :
            modules.append(line.strip())

    name = 'modulesItemSet'
    position = event.object.position.copy()
    itemsFunctionKey = 'resolveSelection'
    father = event.object
    event.object.application.focus = ItemSet.ItemSet(name,position,father,
        itemsName = modules,
        itemsText = modules,
        itemSize = [240,20],
        itemsFunctionKey = itemsFunctionKey,
        noImage = True,
        imagePath = None,
        soundPath = None
    )

    print(f'    new Application.focus = {event.object.application.focus.name}')
    print(f'        EventFunction called: openModule({event.object.application.name})')

    return Event.Event.NOT_RESOLVED

def requestingAttributes(event):
    return type(event) == type('')

def getAttributes(type) :
    if type == Object.Object.SINGLE_CLICK_SELECTABLE : return True
    if type == Object.Object.DOUBLE_CLICK_SELECTABLE : return False
    return None
