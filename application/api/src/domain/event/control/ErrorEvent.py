import MessageEvent, ItemDto
import eventFunction, textFunction

print('ErrorEvent library imported')

class ErrorEvent(MessageEvent.MessageEvent):

    def update(self):
        import Message
        Message.Message(self.object,self.message,
            messageButtonsDto = [
                ItemDto.ItemDto(f'errorSkip.{self.message}.{self.object.name}',
                    size = ItemDto.BUTTON_SIZE,
                    text = 'Skip',
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

            MessageEvent.MessageEvent.__init__(self,event,
                name = name,
                type = type,
                message = message,
                inherited = True
            )
            self.inherited = inherited
            self.execute()
