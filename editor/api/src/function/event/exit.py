import Object

def exit(event) :

    if requestingAttributes(event) :
        return getAttributes(event)
    import Event

    event.object.application.running = False
    print(f'    EventFunction called: exit({event.object.application.name})')
    return Event.Event.RESOLVED


def requestingAttributes(event):
    return type(event) == type('')

def getAttributes(type) :
    if type == Object.Object.SINGLE_CLICK_SELECTABLE : return True
    if type == Object.Object.DOUBLE_CLICK_SELECTABLE : return False
    return None
