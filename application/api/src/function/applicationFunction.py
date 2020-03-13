class Attribute:

    NAME = 'Application'
    FLOOR = 'floor'
    ICON = 'icon'
    IMAGE_EXTENSION = 'png'


class Priority:

    NO_PRIORITY = 0
    LOW = 1
    MEDIUM = 3
    HIGHT = 5


class Key:

    ON_LEFT_CLICK = 'onLeftClick'
    ON_MENU_RESOLVE = 'onMenuResolve'
    ON_HOVERING = 'onHovering'
    TEXT = 'text'
    TEXT_POSITION = 'textPosition'
    FONT_SIZE = 'fontSize'
    IMAGE_PATH = 'imagePath'
    AUDIO_PATH = 'audioPath'
    PRIORITY = 'priority'

def priorityOrder(memoryPackage):
    # return memoryPackage.newObjectsDto
    return 0

def getFloorName(application):
    return f'{application.name}.{Attribute.FLOOR}'
