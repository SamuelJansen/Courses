import Event
import eventFunction

print('ExecussionEvent library imported')

class ExecussionEvent(Event.Event):

    def update(self):
        self.object.execute(self.event)
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,event,
        name = None,
        type = eventFunction.Type.EXECUSSION_EVENT,
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

        self.event = event

        self.execute()
