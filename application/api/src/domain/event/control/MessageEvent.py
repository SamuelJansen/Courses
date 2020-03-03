import ExecussionEvent
import eventFunction

print('EventError library imported')

class MessageEvent(ExecussionEvent.ExecussionEvent):

    def update(self):
        import Message
        Message.Message(
            self.object,
            onMessageResolve = messageResolve
        )
        print(f'{self.name}.update(): message = {self.message}')
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,event,
        name = None,
        type = eventFunction.Type.MESSAGE_EVENT,
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
            message = f'{self.name}.message'
        self.event = event
        self.message = eventFunction.buildMessage(message)

        self.execute()

    def buildMessage(self,message):
        return message


def resolveMessage(event) :
    print(f'{event.name}.messageResolve()')
