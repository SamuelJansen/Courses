import os

import eventFunction

def pageSelection(event) :
    event = eventFunction.findEventByType([eventFunction.Type.MENU_NAVIGATION_EVENT],event.object.handler.events.values())
    print(event.name)
