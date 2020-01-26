def exit(event) :
    event.object.aplication.running = False
    print(f'    EventFunction called: exit({event.object.aplication.name})')
