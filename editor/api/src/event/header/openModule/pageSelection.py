import os

import ItemDto
import imageFunction, pageSelected

def pageSelection(event) :

    imagePath = f'{event.itemsPath}image\\'
    itemNames = imageFunction.getImageFileNames(imagePath,'png')
    imagePath = imagePath
    audioPath = None

    deskItems = []
    for index in range(len(itemNames)) :
        deskItems.append(ItemDto.ItemDto(
            itemNames[index],
            onLeftClick = pageSelected.pageSelected
        ))

    event.application.session.updateDeskItems(deskItems,imagePath,audioPath)
    print(f'{event.name}.pageSelection()')
