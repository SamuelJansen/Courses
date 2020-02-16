import buttonFunction, surfaceFunction

class Attribute:

    NAME = 'Event'


class Type:

    BUTTON = buttonFunction.Attribute.NAME
    SURFACE = surfaceFunction.Attribute.NAME
    CLICK_EVENT = 'ClickEvent'


class Status:

    RESOLVED = 'RESOLVED'
    NOT_RESOLVED = 'NOT_RESOLVED'
    ELIMINATED = 'ELIMINATED'
