import eventFunction

from event.resolveLessonClick import *

def resolveModuleClick(event) :
    import ItemSet
    from model.course import Module

    lessonsPath = f'{event.object.application.pathMannanger.getApiModulePath("course")}{Module.Module.MODULE_PATH}{event.object.name}\\{event.object.name}.ht'
    lessons = []
    with open(lessonsPath,"r",encoding="utf-8") as lessonsFile :
        for lesson in lessonsFile :
            lessons.append(lesson.strip())

    name = 'lessonsItemSet'
    position = event.object.getAbsolutePosition()
    itemsExternalEvent = resolveLessonClick
    father = event.object
    print(f'resolveModuleClick(): father.name = {father.name}')

    ItemSet.ItemSet(name,position,father,
        itemsName = lessons,
        itemsText = lessons,
        itemSize = [100,20],
        itemDirection = ItemSet.ItemSet.RIGHT,
        itemsExternalEvent = itemsExternalEvent,
        noImage = True,
        imagePath = None,
        soundPath = None
    )

    event.status = eventFunction.Status.NOT_RESOLVED

    print(f'    EventFunction called: {event.object.name}.resolveModuleClick({event.object.application.name})')
