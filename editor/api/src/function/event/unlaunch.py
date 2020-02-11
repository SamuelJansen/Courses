import Object
import eventFunction

def unlaunch(event) :

    if requestingAttributes(event) :
        return getAttributes(event)

    print(f'    EventFunction called: unlaunch({event.object.application.name})')
    return eventFunction.EventStatus.NOT_RESOLVED


def requestingAttributes(event):
    return type(event) == type('')

def getAttributes(type) :
    if type == Object.Object.SINGLE_CLICKABLE : return True
    if type == Object.Object.DOUBLE_CLICKABLE : return False
    return None
