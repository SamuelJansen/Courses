class Attribute:

    NAME = 'Handler'


class Type:
    pass


def renderOrder(object) :
    return object.blitOrder,object.collidableRect.bottom
