import os

import ItemDto, Button
import pageSelected, pageFunction, applicationFunction, pages

def pageSelection(event) :

    event.application.session.updatePage(pages.SELECTION_PAGE)

    pathMannanger = event.application.pathMannanger
    lessonScriptPath = f'''{pathMannanger.getApiModulePath('course')}resourse\\modules\\{event.navigationHistory}'''
    pageNames = event.application.repository.getPageNamesFromLessonScriptPath(lessonScriptPath)
    imagePath = f'{lessonScriptPath}image\\'
    audioPath = None

    deskItemsDto = []
    for index in range(len(pageNames)) :
        deskItemsDto.append(ItemDto.ItemDto(
            pageNames[index],
            onLeftClick = pageSelected.pageSelected,
            imagePath = imagePath,
            audioPath = audioPath
        ))

    event.application.session.updateDesk(deskItemsDto,
        onDeskUpdate = buildDeskItems
    )
    print(f'{event.name}.pageSelection()')


def buildDeskItems(deskItemsDto,session) :
    THUMB = 'thumb'
    itemsDto = []
    itemPositionAdjustment = (session.desk.size[0] - (session.deskItemSize[0] - session.desk.padding[0]) * session.desk.itemsPerLine - session.desk.padding[0]) / (session.desk.itemsPerLine + 1)
    initialPosition = [
        itemPositionAdjustment,
        itemPositionAdjustment
    ]
    for index in range(len(deskItemsDto)) :
        itemPosition = [
            initialPosition[0] + (session.deskItemSize[0] - session.desk.padding[0] + itemPositionAdjustment) * (index % session.desk.itemsPerLine),
            initialPosition[1] + (session.deskItemSize[1] - session.desk.padding[1] + itemPositionAdjustment) * (index // session.desk.itemsPerLine)
        ]
        itemsDto.append([
            [
                f'{deskItemsDto[index].name}.{THUMB}',
                itemPosition.copy(),
                session.deskItemSize.copy(),
                session.desk
            ],
            {
                applicationFunction.Key.ON_LEFT_CLICK : deskItemsDto[index].onLeftClick,
                applicationFunction.Key.ON_HOVERING : onHovering,
                applicationFunction.Key.IMAGE_PATH : f'{deskItemsDto[index].imagePath}{THUMB}\\',
                applicationFunction.Key.AUDIO_PATH : deskItemsDto[index].audioPath
            },
            {
                applicationFunction.Key.PRIORITY : applicationFunction.Priority.HIGHT
            }
        ])
    return itemsDto,Button.Button,applicationFunction.Priority.MEDIUM

def onHovering(event):
    print(f'{event.object.name}.onHovering() called')
