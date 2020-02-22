import buttonFunction, modalFunction, surfaceFunction, eventFunction

class Attribute:

    NAME = 'Event'


class Type:

    SURFACE = surfaceFunction.Attribute.NAME
    MODAL = modalFunction.Attribute.NAME
    BUTTON = buttonFunction.Attribute.NAME

    EVENT = eventFunction.Attribute.NAME
    FOCUS_EVENT = 'FocusEvent'
    CLICK_EVENT = 'ClickEvent'
    FALSE_CLICK_EVENT = 'FalseClickEvent'
    REMOVE_FOCUS_EVENT = 'RemoveFocusEvent'


class Status:

    RESOLVED = 'RESOLVED'
    NOT_RESOLVED = 'NOT_RESOLVED'
    REMOVED = 'REMOVED'
