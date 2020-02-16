import eventFunction

def update(event) :
    father = event.object.father
    father.handler.removeObjectTree(event.object)
    father.resetButtonsPosition()

    event.status = eventFunction.Status.RESOLVED
    print(f'    EventFunction called: update({event.object.application.name})')
