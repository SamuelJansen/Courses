import Object
import eventFunction

def resolveLessonClick(event) :

    if requestingAttributes(event) :
        return getAttributes(event)

    print(f'    EventFunction called: {event.object.name}.resolveLessonClick({event.object.application.name})')

def requestingAttributes(event):
    return type(event) == type('')

def getAttributes(type) :
    if type == Object.Object.SINGLE_CLICKABLE : return True
    if type == Object.Object.DOUBLE_CLICKABLE : return False
    return None
