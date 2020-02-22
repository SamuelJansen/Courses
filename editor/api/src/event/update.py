import eventFunction

def update(event) :
    event.object.father.handler.removeObject(event.object)
    event.object.father.resetButtonsPosition()

    event.status = eventFunction.Status.RESOLVED
    print(f'    EventFunction called: update({event.object.application.name})')
