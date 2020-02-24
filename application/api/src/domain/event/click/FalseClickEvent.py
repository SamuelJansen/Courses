import Event, RemoveFocusEvent
import eventFunction, mouseFunction

print('FalseClickEvent library imported')

class FalseClickEvent(Event.Event):

    def update(self):
        RemoveFocusEvent.RemoveFocusEvent(self.object)
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,application,
        name = None,
        type = eventFunction.Type.FALSE_CLICK_EVENT,
        inherited = False
    ):

        Event.Event.__init__(self,application,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited
        self.execute()
