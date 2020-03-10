import eventFunction

def closeModule(event) :
    event.application.session.close()
    print(f'{event.name}.closeModule()')
