import eventFunction

def nextPage(event) :
    event.status = eventFunction.Status.NOT_RESOLVED
    print(f'    EventFunction called: nextPage({event.object.application.name})')
