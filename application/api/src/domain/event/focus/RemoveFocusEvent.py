import FocusEvent
import eventFunction, mouseFunction

print('RemoveFocusEvent library imported')

class RemoveFocusEvent(FocusEvent.FocusEvent):

    def update(self):
        self.removeFocus()
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,application,
        name = None,
        type = eventFunction.Type.REMOVE_FOCUS_EVENT,
        inherited = False
    ):

        FocusEvent.FocusEvent.__init__(self,application,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited
        self.execute()
