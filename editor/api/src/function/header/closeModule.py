import eventFunction

def closeModule(event) :
    if event.application.session :
        event.application.session.close(event,
            onClose = onClose
        )
    print(f'{event.name}.closeModule()')

def onClose(event):
    pass
