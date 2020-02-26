import os

import ItemSessionDto
import imageFunction, selectedPage

def selectionPage(event) :

    imagePath = f'{event.itemsPath}image\\'
    itemNames = imageFunction.getImageFileNames(imagePath,'png')
    father = event.application.session.desk
    initialPosition = [2,2]
    size = [55,40]

    deskItems = []
    for index in range(len(itemNames)) :
        name = itemNames[index]
        externalFunction = selectedPage.selectedPage
        imagePath = imagePath
        audioPath = None
        session = ItemSessionDto.ItemSessionDto(name,size,father,externalFunction,imagePath,audioPath)
        deskItems.append(session)

    event.application.session.addAllDeskItem(deskItems)

    print(f'event.application.session.name = {event.application.session.name}')

    print(f'{event.name}.pageSelection()')
