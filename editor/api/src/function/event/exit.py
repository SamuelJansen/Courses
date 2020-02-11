import Object
import eventFunction

def exit(event) :

    if requestingAttributes(event) :
        return getAttributes(event)

    event.object.application.running = False
    print(f'    EventFunction called: exit({event.object.application.name})')
    event.status = eventFunction.EventStatus.RESOLVED
    return eventFunction.EventStatus.RESOLVED


def requestingAttributes(event):
    return type(event) == type('')

def getAttributes(type) :
    if type == Object.Object.SINGLE_CLICKABLE : return True
    if type == Object.Object.DOUBLE_CLICKABLE : return False
    return None
