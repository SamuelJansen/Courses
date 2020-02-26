import eventFunction

def add(event) :
    event.status = eventFunction.Status.NOT_RESOLVED
    print(f'    EventFunction called: add({event.object.application.name})')
