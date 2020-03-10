import os

import ItemDto, Button
import pageSelected, pageFunction, applicationFunction, sessionPage

def pageSelection(event) :

    event.application.session.updatePage(sessionPage.SELECTION_PAGE)

    lessonScriptPath = event.itemsPath
    pageNames = event.application.repository.getPageNamesFromLessonScriptPath(lessonScriptPath)
    # print(f'pageNames = {pageNames}')

    imagePath = f'{event.itemsPath}image\\'
    audioPath = None

    deskItems = []
    for index in range(len(pageNames)) :
        deskItems.append(ItemDto.ItemDto(
            pageNames[index],
            onLeftClick = pageSelected.pageSelected,
            imagePath = imagePath,
            audioPath = audioPath
        ))

    onDeskUpdate = scriptItems
    event.application.session.updateDesk(deskItems,onDeskUpdate)
    print(f'{event.name}.pageSelection()')


def scriptItems(deskItems,session) :
    itemsDto = []
    itemPositionAdjustment = (session.desk.size[0] - (session.deskItemSize[0] - session.desk.padding[0]) * session.desk.itemsPerLine - session.desk.padding[0]) / (session.desk.itemsPerLine + 1)
    initialPosition = [
        itemPositionAdjustment,
        itemPositionAdjustment
    ]
    for index in range(len(deskItems)) :
        itemPosition = [
            initialPosition[0] + (session.deskItemSize[0] - session.desk.padding[0] + itemPositionAdjustment) * (index % session.desk.itemsPerLine),
            initialPosition[1] + (session.deskItemSize[1] - session.desk.padding[1] + itemPositionAdjustment) * (index // session.desk.itemsPerLine)
        ]
        itemsDto.append([
            [
                deskItems[index].name,
                itemPosition.copy(),
                session.deskItemSize.copy(),
                session.desk
            ],
            {
                applicationFunction.Key.ON_LEFT_CLICK : deskItems[index].onLeftClick,
                applicationFunction.Key.ON_HOVERING : onHovering,
                applicationFunction.Key.IMAGE_PATH : deskItems[index].imagePath,
                applicationFunction.Key.AUDIO_PATH : deskItems[index].audioPath
            },
            {
                applicationFunction.Key.PRIORITY : applicationFunction.Priority.HIGHT
            }
        ])
    return itemsDto,Button.Button,applicationFunction.Priority.MEDIUM

def onHovering(event):
    print(f'{event.object.name}.onHovering() called')
