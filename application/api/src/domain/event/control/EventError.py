import os

import Modal, ExecussionEvent
import eventFunction

print('EventError library imported')

class EventError(ExecussionEvent.ExecussionEvent):

    def update(self):
        print(f'ErrorEvent.update(): error message = {self.message}')
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,event,
        name = None,
        type = eventFunction.Type.MENU_EVENT,
        message = None,
        inherited = False
    ):

        ExecussionEvent.ExecussionEvent.__init__(self,event,
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
