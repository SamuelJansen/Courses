def update(event) :
    father = event.object.father
    father.handler.deleteObject(event.object.name)
    father.resetButtonsPosition()
    print(f'    EventFunction called: update({event.object.aplication.name})')
