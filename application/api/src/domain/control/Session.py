import Button, Message
import imageFunction, applicationFunction, sessionFunction

print('Session library imported')

class Session:

    def __init__(self,desk,path):

        self.desk = desk
        self.application = self.desk.application

        self.name = f'{sessionFunction.Attribute.NAME}.{desk.name}'
        self.path = path

        self.deskItemSize = [
            self.desk.size[0] // self.desk.itemsPerLine,
            int(self.desk.size[0] // self.desk.itemsPerLine / 1.57)
        ]
        self.page = sessionFunction.Page.HOME

        self.itemNames = {}

    def updateDeskItems(self,itemsSessionDtoList,itemsImagePath,itemsAudioPath):
        self.desk.handler.removeObjectTree()
        itemsMemoryOptimizationDto = []
        itemPositionAdjustment = (self.desk.size[0] - (self.deskItemSize[0] - self.desk.padding[0]) * self.desk.itemsPerLine - self.desk.padding[0]) / (self.desk.itemsPerLine + 1)
        initialPosition = [
            itemPositionAdjustment,
            itemPositionAdjustment
        ]
        for index in range(len(itemsSessionDtoList)) :
            item = itemsSessionDtoList[index]
            itemPosition = [
                initialPosition[0] + (self.deskItemSize[0] - self.desk.padding[0] + itemPositionAdjustment) * (index % self.desk.itemsPerLine),
                initialPosition[1] + (self.deskItemSize[1] - self.desk.padding[1] + itemPositionAdjustment) * (index // self.desk.itemsPerLine)
            ]
            itemsMemoryOptimizationDto.append([
                [
                    item.name,
                    itemPosition.copy(),
                    self.deskItemSize.copy(),
                    self.desk,
                ],
                {
                    applicationFunction.Key.ON_LEFT_CLICK : item.onLeftClick,
                    applicationFunction.Key.IMAGE_PATH : itemsImagePath,
                    applicationFunction.Key.AUDIO_PATH : itemsAudioPath,
                },
                {
                    applicationFunction.Key.PRIORITY : applicationFunction.Priority.HIGHT
                }
            ])
            self.addItemName(item)
        self.application.memoryOptimizer.newObjects(itemsMemoryOptimizationDto,Button.Button,
            priority = applicationFunction.Priority.MEDIUM
        )

    def addItemName(self,item):
        if self.page not in self.itemNames :
            self.itemNames[self.page] = []
        if item.name not in self.itemNames[self.page] :
            self.itemNames[self.page].append(item.name)

    def removeItemNames(self,itemNames):
        for itemName in itemNames :
            for page in self.itemNames :
                pageItemNames = self.itemNames[page].copy()
                if itemName in pageItemNames :
                    self.itemNames[page].remove(itemName)

    def removeItemNamesFromPage(self,page):
        if page in self.itemNames :
            del self.itemNames[page]

    def revealDeskItems(self,itemNames):
        self.desk.screen.reveaObjects(itemNames)

    def hideAllDeskItems(self):
        self.desk.screen.hideAllObjects()

    def removeDesk(self):
        self.application.getFloor().handler.removeObject(self.desk)

    def save(self):
        Message.Message(self.desk,f'{self.name}.save()',
            fontSize = 16
        )

    def getNamesFromItemsDto(self,itemsSessionDtoList):
        return [itemDto.name for itemDto in itemsSessionDtoList]

    def keepCurrentSession(self):
        pass
