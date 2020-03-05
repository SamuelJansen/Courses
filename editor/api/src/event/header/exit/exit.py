import Message, ItemDto
import eventFunction

def exit(event) :

    cancelButtonDto = ItemDto.ItemDto('cancel',
        size = [55,24],
        text = 'Cancel',
        textPosition = [0,0],
        onLeftClick = cancel
    )
    okButtonDto = ItemDto.ItemDto('ok',
        size = [55,24],
        text = 'Ok',
        textPosition = [0,0],
        onLeftClick = ok
    )
    butonsDto = [cancelButtonDto,okButtonDto]

    message = Message.Message(event.object,
        message = 'Do you want to exit the editor?',
        optionsDto = butonsDto,
        fontSize = 16
    )

    print(f'{event.name}.exit()')


def cancel(event) :
    print(f'{event.name}.cancel()')

def ok(event) :
    event.application.close()
    print(f'{event.name}.ok()')
