import os

import Button, Surface
import eventFunction, imageFunction, headerFunction

def pageSelection(event) :
    # event = eventFunction.findEventByType([eventFunction.Type.MENU_NAVIGATION_EVENT],event.object.handler.events.values())
    print(f'{event.name}.itemsPath = {event.itemsPath}')

    name = event.name
    position = [
        0,
        event.application.getFloor().handler.objects[headerFunction.Attribute.NAME].size[1] + 1
    ]
    print(f'position = {position}')
    size = [
        event.application.size[0],
        event.application.size[1] - event.application.getFloor().handler.objects[headerFunction.Attribute.NAME].size[1]
    ]
    print(f'size = {size}')
    father = event.application.getFloor()
    padding = [2,2]

    itemsModal = Surface.Surface(name,position,size,father,
        padding = padding,
        noImage = True
    )

    itemNames = imageFunction.getImageFileNames(f'{event.itemsPath}image\\','png')
    print(itemNames)

    father = itemsModal
    initialPosition = [10,10]
    size = [55,40]

    for nameIndex in range(len(itemNames)) :

        name = itemNames[nameIndex]
        position = [
            initialPosition[0] + size[0] * nameIndex,
            initialPosition[1]
        ]

        print(f'imagePath = {event.itemsPath}image\\{name}.png')

        Button.Button(
            name,
            position,
            size,
            father,
            externalFunction = None,
            imagePath = f'{event.itemsPath}image\\',
            audioPath = None
        )

    event.updateStatus(eventFunction.Status.RESOLVED)
