import Event
import eventFunction

class ExecussionEvent(Event.Event):

    def update(self):
        print(f'{self.name}.update(): {self.name}.object.name = {self.object.name}')
        self.object.execute(self)
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
        self.execute()
