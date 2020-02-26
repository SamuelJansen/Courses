import eventFunction

def launch(event) :
    event.status = eventFunction.Status.NOT_RESOLVED
    print(f'    EventFunction called: launch({event.object.application.name})')
