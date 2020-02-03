import Object

def resolveSelection(event) :

    if requestingAttributes(event) :
        return getAttributes(event)
    import Event

    print(f'    EventFunction called: esolveSelection({event.object.application.name})')
    return Event.Event.NOT_RESOLVED


def requestingAttributes(event):
    return type(event) == type('')

def getAttributes(type) :
    if type == Object.Object.SINGLE_CLICK_SELECTABLE : return True
    if type == Object.Object.DOUBLE_CLICK_SELECTABLE : return False
    return None
