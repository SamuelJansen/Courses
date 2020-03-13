import Message, ItemDto
import eventFunction, textFunction, containerFunction

import save

messageName = 'exitEditor'

def exit(event) :

    buttonPosition = [
        containerFunction.Attribute.FILL,
        containerFunction.Attribute.CENTER
    ]
    buttonSize = [85,45]
    messageFontSize = 18
    textPosition = [
        textFunction.Attribute.CENTER,
        textFunction.calculateTextPositionPaddedOnMenu(buttonSize,event.object.padding,messageFontSize)[1]
    ]

    cancelButtonDto = ItemDto.ItemDto('cancel',
        position = buttonPosition,
        size = buttonSize,
        text = 'Cancel',
        textPosition = textPosition,
        onLeftClick = cancel
    )
    okButtonDto = ItemDto.ItemDto('ok',
        position = buttonPosition,
        size = buttonSize,
        text = 'Ok',
        textPosition = textPosition,
        onLeftClick = ok
    )
    saveButtonDto = ItemDto.ItemDto('save',
        position = buttonPosition,
        size = buttonSize,
        text = 'Save',
        textPosition = textPosition,
        onLeftClick = saveWork
    )
    if event.application.session :
        messageButtonsDto = [cancelButtonDto,saveButtonDto,okButtonDto]
    else :
        messageButtonsDto = [cancelButtonDto,okButtonDto]

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
