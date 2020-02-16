import eventFunction

def resolveLessonClick(event) :
    event.status = eventFunction.Status.NOT_RESOLVED
    print(f'    EventFunction called: {event.object.name}.resolveLessonClick({event.object.application.name})')
