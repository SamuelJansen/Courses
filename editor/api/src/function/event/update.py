def update(event) :
    father = event.object.father
    father.objectHandler.deleteObject(event.object.name)
    father.resetButtonsPosition()
    print(f'    EventFunction called: update({event.object.aplication.name})')
    
