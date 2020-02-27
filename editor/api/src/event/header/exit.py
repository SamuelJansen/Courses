import eventFunction

def exit(event) :
    event.application.close()
    print(f'{event.name}.exit()')
