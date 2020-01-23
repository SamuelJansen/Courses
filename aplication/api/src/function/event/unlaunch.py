def unlaunch(event) :
    event.object.father.objectHandler.deleteObject(event.object.name)
    print(f'    EventFunction called: unlaunch({event.object.aplication.name})')
