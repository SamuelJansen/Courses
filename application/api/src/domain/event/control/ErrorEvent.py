import MessageEvent
import eventFunction

print('ErrorEvent library imported')

class ErrorEvent(MessageEvent.MessageEvent):

    def update(self):
        print(f'{self.name}.update(): -- DEBUGING -- ')
        print(self.message)
        while(True) :
            pass
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,event,
        name = None,
        type = eventFunction.Type.ERROR_EVENT,
        message = None,
        inherited = False
    ):
        if not event :
            print(f'ErrorEvent -- DEBUGING -- ')
            print(message)
            while(True) :
                pass
        else :

            ExecussionEvent.ExecussionEvent.__init__(self,event,
                name = name,
                type = type,
                inherited = True
            )
            self.inherited = inherited
            self.execute()
