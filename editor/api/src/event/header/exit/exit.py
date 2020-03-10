import Message, ItemDto
import eventFunction, textFunction

import save

messageName = 'exitEditor'

def exit(event) :

    messageFontSize = 18
    buttonSize = [85,45]
    textPosition = [
        textFunction.Attribute.CENTER,
        textFunction.calculateTextPositionPaddedOnMenu(buttonSize,event.object.padding,messageFontSize)[1]
    ]

    cancelButtonDto = ItemDto.ItemDto('cancel',
        size = buttonSize,
        text = 'Cancel',
        textPosition = textPosition,
        onLeftClick = cancel
    )
    okButtonDto = ItemDto.ItemDto('ok',
        size = buttonSize,
        text = 'Ok',
        textPosition = textPosition,
        onLeftClick = ok
    )
    saveButtonDto = ItemDto.ItemDto('save',
        size = buttonSize,
        text = 'Save',
        textPosition = textPosition,
        onLeftClick = saveWork
    )
    messageButtonsDto = [cancelButtonDto,saveButtonDto,okButtonDto]

    message = Message.Message(event.object,
        name = messageName,
        message = 'Do you want to exit the editor?',
        messageButtonsDto = messageButtonsDto,
        fontSize = messageFontSize
    )
    # message.addText('Do you want to exit the editor?',[0,0],16)
    # message.addText('Do you want to exit the editor?',[0,20],16)
    # message.addText('Do you want to exit the editor?',[0,40],16)

    print(f'{event.name}.exit()')


def cancel(event) :
    event.application.findObjectByName(messageName).closeMessage()
    print(f'{event.name}.cancel()')

def ok(event) :
    event.application.close()
    print(f'{event.name}.ok()')

def saveWork(event) :
    save.save(event)
    event.application.findObjectByName(messageName).closeMessage()
    print(f'{event.name}.saveWork()')
