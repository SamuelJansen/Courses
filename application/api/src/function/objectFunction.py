class Attribute:

    NAME = 'Object'

    '''
    NOT_HITTABLE_COLOR = [0,0,0,0]
    NO_IMAGE_COLOR = [0,0,0,0]
    '''
    NOT_HITTABLE_COLOR = [0,0,100,40]
    NO_IMAGE_COLOR = [255,0,0,40]
    #'''

    SINGLE_CLICKABLE = 'SINGLE_CLICKABLE'
    DOUBLE_CLICKABLE = 'DOUBLE_CLICKABLE'


class Type:

    APPLICATION = 'APPLICATION'
    APPLICATION_FLOOR = 'APPLICATION_FLOOR'
    CENARIO = 'CENARIO'
    OBJECT = 'OBJECT'
    USER_INTERFACE = 'USER_INTERFACE'

    DRAG_AND_DROP = 'DRAG_AND_DROP'
    MESSAGE = 'MESSAGE'

    types = {
        0 : APPLICATION,
        10 : APPLICATION_FLOOR,
        100 : CENARIO,
        1000 : OBJECT,
        10000 : USER_INTERFACE,
        1000000000000 : DRAG_AND_DROP,
        10000000000000 : MESSAGE
    }

    blitOrder = ( lambda types=types : { types[key]:key for key in types.keys() } )()


def getType(index):
    return Type.types[index]

def getBlitOrder(object):
    if object.type == object.father.type :
        return object.father.blitOrder + 1
    else :
        return Type.blitOrder[object.type] + Type.blitOrder[object.father.type]
