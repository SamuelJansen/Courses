import eventFunction

def closeModule(event) :
    event.application.removeSession()
    print(f'{event.name}.closeModule()')
