import Object

def update(event) :

    if requestingAttributes(event) :
        return getAttributes(event)
    import Event

    father = event.object.father
    father.handler.deleteObject(event.object.name)
    father.resetButtonsPosition()
    print(f'    EventFunction called: update({event.object.application.name})')
    return Event.Event.NOT_RESOLVED


def requestingAttributes(event):
    return type(event) == type('')

def getAttributes(type) :
    if type == Object.Object.SINGLE_CLICK_SELECTABLE : return True
    if type == Object.Object.DOUBLE_CLICK_SELECTABLE : return False
    return None
