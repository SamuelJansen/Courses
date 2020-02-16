import eventFunction

def save(event) :
    event.status = eventFunction.Status.NOT_RESOLVED
    print(f'    EventFunction called: save({event.object.application.name})')
