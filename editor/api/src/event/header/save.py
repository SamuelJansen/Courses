import eventFunction

def save(event) :
    if event.application.session :
        event.application.session.save()
    print(f'{event.name}.save()')
