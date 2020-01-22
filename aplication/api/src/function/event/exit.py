def exitFunction(event) :
    event.aplication.running = False
    print(f'    EventFunction called: exit({event.aplication.name})')
