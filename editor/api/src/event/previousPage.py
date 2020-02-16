import eventFunction

def previousPage(event) :
    event.status = eventFunction.Status.NOT_RESOLVED
    print(f'    EventFunction called: previousPage({event.object.application.name})')
