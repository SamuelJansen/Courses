import eventFunction

def unlaunch(event) :
    event.status = eventFunction.Status.NOT_RESOLVED
    print(f'    EventFunction called: unlaunch({event.object.application.name})')
