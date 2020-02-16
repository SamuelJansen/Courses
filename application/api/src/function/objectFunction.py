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

    types = {
        0 : APPLICATION,
        10 : APPLICATION_FLOOR,
        100 : CENARIO,
        1000 : OBJECT,
        10000 : USER_INTERFACE
    }

    blitOrder = ( lambda types=types : { types[key]:key for key in types.keys() } )()
    # print(f'blitOrder = {(lambda types=types : { types[key]:key for key in types.keys() })()}')


def getType(index):
    return Type.types[index]

def getBlitOrder(object):
    if object.type == object.father.type :
        blitOrder = object.father.blitOrder + 1
    else :
        # blitOrder = list(ObjectType.types.keys())[list(ObjectType.types.values()).index(object.type)]
        blitOrder = Type.blitOrder[object.type] + Type.blitOrder[object.father.type]
    return blitOrder
