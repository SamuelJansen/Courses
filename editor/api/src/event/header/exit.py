import eventFunction

def exit(event) :
    event.object.application.running = False
    print(f'    EventFunction called: exit({event.object.application.name})')
    event.status = eventFunction.Status.RESOLVED
