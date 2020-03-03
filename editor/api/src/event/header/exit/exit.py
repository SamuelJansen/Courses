import Message, ItemDto
import eventFunction

def exit(event) :

    cancelButtonDto = ItemDto.ItemDto('cancel',
        position = [40,100],
        size = [80,40],
        text = 'Cancel',
        textPosition = [0,0],
        onLeftClick = cancel
    )
    okButtonDto = ItemDto.ItemDto('ok',
        position = [120,100],
        size = [80,40],
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
