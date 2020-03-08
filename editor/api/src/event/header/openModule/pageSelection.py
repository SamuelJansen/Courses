import os

import ItemDto
import imageFunction, pageSelected, pageFunction

def pageSelection(event) :

    lessonScriptPath = event.itemsPath
    pageNames = pageFunction.getPageNames(lessonScriptPath,event.application)

    imagePath = f'{event.itemsPath}image\\'
    audioPath = None

    deskItems = []
    for index in range(len(pageNames)) :
        deskItems.append(ItemDto.ItemDto(
            pageNames[index],
            onLeftClick = pageSelected.pageSelected
        ))

    event.application.session.updateDeskItems(deskItems,imagePath,audioPath)
    print(f'{event.name}.pageSelection()')
