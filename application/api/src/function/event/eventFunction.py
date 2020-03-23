import os

import buttonFunction, modalFunction, surfaceFunction, eventFunction

class Attribute:

    NAME = 'Event'


class Type:

    SURFACE = surfaceFunction.Attribute.NAME
    MODAL = modalFunction.Attribute.NAME
    BUTTON = buttonFunction.Attribute.NAME

    EVENT = eventFunction.Attribute.NAME
    EXECUSSION_EVENT = 'ExecussionEvent'
    MESSAGE_EVENT = 'MessageEvent'
    ERROR_EVENT = 'ErrorEvent'

    SESSION_EVENT = 'SessionEvent'

    FOCUS_EVENT = 'FocusEvent'
    REMOVE_FOCUS_EVENT = 'RemoveFocusEvent'

    CLICK_EVENT = 'ClickEvent'
    FALSE_CLICK_EVENT = 'FalseClickEvent'
    MODAL_CLICK_EVENT = 'ModalClickEvent'

    MENU_EVENT = 'MenuEvent'
    MENU_ACCESS_EVENT = 'MenuAccessEvent'
    MENU_NAVIGATION_EVENT = 'MenuNavigationEvent'

    HOVER_EVENT = 'HoverEvent'


class Status:

    RESOLVED = 'RESOLVED'
    NOT_RESOLVED = 'NOT_RESOLVED'
    REMOVED = 'REMOVED'


def getObjectName(event) :
    return event.name.split('.')[-1]

def getEventType(event) :
    return event.name.split('.')[0]

def getItemNames(itemsPath) :
    itemNames = []
    names = os.listdir(itemsPath)
    for name in names :
        itemNames.append(name)
    return itemNames

def getEventNames(event) :
    return list(event.object.handler.events.keys())

def findEventByType(eventTypeList,eventList) :
    for event in eventList :
        eventType = getEventType(event)
        if eventType in eventTypeList :
            if notExecussionEvent(event) :
                return event

def notExecussionEvent(event):
    return Type.EXECUSSION_EVENT not in event.name
