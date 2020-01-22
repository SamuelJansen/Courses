def unlaunchFunction(object) :
    object.father.objectHandler.deleteObject(object.name)
    print(f'    EventFunction called: unlaunch({object.aplication.name})')
