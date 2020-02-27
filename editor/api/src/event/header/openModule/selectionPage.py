import os

import ItemDto
import imageFunction, selectedPage

def selectionPage(event) :

    imagePath = f'{event.itemsPath}image\\'
    itemNames = imageFunction.getImageFileNames(imagePath,'png')
    father = event.application.session.desk
    imagePath = imagePath
    audioPath = None

    deskItems = []
    for index in range(len(itemNames)) :
        deskItems.append(ItemDto.ItemDto(
            itemNames[index],
            selectedPage.selectedPage
        ))

    event.application.session.addAllDeskItem(deskItems,father,imagePath,audioPath)

    print(f'event.application.session.name = {event.application.session.name}')

    print(f'{event.name}.pageSelection()')
