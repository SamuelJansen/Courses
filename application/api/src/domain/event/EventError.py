import os

import Modal, Event
import eventFunction

print('EventError library imported')

class EventError(Event.Event):

    def update(self):
        print(f'ErrorEvent.update(): error message = {self.message}')
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,event,
        name = None,
        type = eventFunction.Type.MENU_EVENT,
        message = None,
        inherited = False
    ):

        object = event.object
        name = f'{event.type}.{type}.{event.object.name}'

        Event.Event.__init__(self,object,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited

        if not message :
            message = f'{self.name} error'
        self.message = eventFunction.buildErrorMessage(message)
        self.event = event

        self.execute()
