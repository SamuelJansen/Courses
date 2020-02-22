import eventFunction

def resolveLessonClick(event) :
    import RemoveFocusEvent

    RemoveFocusEvent.RemoveFocusEvent(event.application)

    event.status = eventFunction.Status.RESOLVED
    print(f'    EventFunction called: {event.object.name}.resolveLessonClick({event.object.application.name})')
