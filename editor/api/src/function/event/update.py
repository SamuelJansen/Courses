import Object
import eventFunction

def update(event) :

    if requestingAttributes(event) :
        return getAttributes(event)

    father = event.object.father
    father.handler.deleteObject(event.object.name)
    father.resetButtonsPosition()
    print(f'    EventFunction called: update({event.object.application.name})')

def requestingAttributes(event):
    return type(event) == type('')

def getAttributes(type) :
    if type == Object.Object.SINGLE_CLICKABLE : return True
    if type == Object.Object.DOUBLE_CLICKABLE : return False
    return None
