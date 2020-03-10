import Event, ExecussionEvent
import eventFunction

print('HoverEvent library imported')

class HoverEvent(Event.Event):

    def update(self):
        ExecussionEvent.ExecussionEvent(self)
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,object,
        name = None,
        type = eventFunction.Type.HOVER_EVENT,
        inherited = False
    ):

        Event.Event.__init__(self,object,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited
        self.execute()
