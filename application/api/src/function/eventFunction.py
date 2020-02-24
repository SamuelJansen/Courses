import buttonFunction, modalFunction, surfaceFunction, eventFunction

class Attribute:

    NAME = 'Event'


class Type:

    SURFACE = surfaceFunction.Attribute.NAME
    MODAL = modalFunction.Attribute.NAME
    BUTTON = buttonFunction.Attribute.NAME

    EVENT = eventFunction.Attribute.NAME
    EXECUTE_EVENT = 'ExecuteEvent'

    FOCUS_EVENT = 'FocusEvent'
    REMOVE_FOCUS_EVENT = 'RemoveFocusEvent'

    CLICK_EVENT = 'ClickEvent'
    FALSE_CLICK_EVENT = 'FalseClickEvent'

    MENU_EVENT = 'MenuEvent'
    MENU_ACCESS_EVENT = 'MenuAccessEvent'
    MENU_NAVIGATION_EVENT = 'MenuNavigationEvent'


class Status:

    RESOLVED = 'RESOLVED'
    NOT_RESOLVED = 'NOT_RESOLVED'
    REMOVED = 'REMOVED'



def getObjectName(event) :
    return event.name.split('.')[-1]

def getEventType(event) :
    return event.name.split('.')[0]
