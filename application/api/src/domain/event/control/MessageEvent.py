import ExecussionEvent, ItemDto
import eventFunction, textFunction

print('MessageEvent library imported')

class MessageEvent(ExecussionEvent.ExecussionEvent):

    def update(self):
        import Message
        Message.Message(self.object,self.message,
            size = [550,300],
            messageButtonsDto = [
                ItemDto.ItemDto(f'messageOk.{self.message}.{self.object.name}',
                    size = ItemDto.BUTTON_SIZE,
                    text = 'Ok',
                    textPosition = [
                        textFunction.Attribute.CENTER,
                        textFunction.calculateTextPositionPaddedOnMenu(ItemDto.BUTTON_SIZE,[1,1],18)[1]
                    ],
                    onLeftClick = self.onMessageResolve
                )
            ]
        )
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,event,
        name = None,
        message = None,
        type = eventFunction.Type.MESSAGE_EVENT,
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
        self.message = self.buildMessage(message)
        # self.messageObject = None

        self.execute()

    def buildMessage(self,message):
        return message

    def onMessageResolve(self,event) :
        message = event.object.father.father
        print(f'Message name = {message.name}, message.father.name = {message.father.name}, event.object.name = {event.object.name}')
        message.father.handler.removeObject(message)
