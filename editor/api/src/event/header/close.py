import eventFunction

def close(event) :
    event.status = eventFunction.Status.NOT_RESOLVED
    print(f'    EventFunction called: adclosed({event.object.application.name})')
