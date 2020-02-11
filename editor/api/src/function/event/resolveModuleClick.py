import Object
import eventFunction

def resolveModuleClick(event) :

    if requestingAttributes(event) :
        return getAttributes(event)

    import ItemSet
    from model.course import Module

    lessonsPath = f'{event.object.application.pathMannanger.getApiModulePath("course")}{Module.Module.MODULE_PATH}{event.object.name}\\{event.object.name}.ht'
    lessons = []
    with open(lessonsPath,"r",encoding="utf-8") as lessonsFile :
        for lesson in lessonsFile :
            lessons.append(lesson.strip())

    name = 'lessonsItemSet'
    position = event.object.getAbsolutePosition()
    itemsFunctionKey = 'resolveLessonClick'
    father = event.object
    print(f'resolveModuleClick(): father.name = {father.name}')


    # event.object.application.focus = ItemSet.ItemSet(name,position,father,
    ItemSet.ItemSet(name,position,father,
        itemsName = lessons,
        itemsText = lessons,
        itemSize = [100,20],
        itemDirection = ItemSet.ItemSet.RIGHT,
        itemsFunctionKey = itemsFunctionKey,
        noImage = True,
        imagePath = None,
        soundPath = None
    )

    event.status = eventFunction.EventStatus.NOT_RESOLVED

    print(f'    EventFunction called: {event.object.name}.resolveModuleClick({event.object.application.name})')

def requestingAttributes(event):
    return type(event) == type('')

def getAttributes(type) :
    if type == Object.Object.SINGLE_CLICKABLE : return True
    if type == Object.Object.DOUBLE_CLICKABLE : return False
    return None
