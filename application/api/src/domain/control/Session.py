import Button

print('Session library imported')

class Session:

    def __init__(self,desk,path):

        self.desk = desk
        self.application = self.desk.application

        self.name = f'Session.{desk.name}'
        self.path = path

        self.deskItemSize = [
            self.desk.size[0] // self.desk.itemsPerLine,
            int(self.desk.size[0] // self.desk.itemsPerLine / 1.57)
        ]
        self.deskItems = {}

    def addDeskItem(self,item):
        self.deskItems[item.name] = item

    def addAllDeskItem(self,itemSessionDtoList):

        itemsQuantity = len(itemSessionDtoList)
        itemPositionAdjustment = (self.desk.size[0] - (self.deskItemSize[0] - self.desk.padding[0]) * self.desk.itemsPerLine - self.desk.padding[0]) / (self.desk.itemsPerLine + 1)
        initialPosition = [
            itemPositionAdjustment,
            itemPositionAdjustment
        ]
        for index in range(itemsQuantity) :
            item = itemSessionDtoList[index]
            itemPosition = [
                    initialPosition[0] + (self.deskItemSize[0] - self.desk.padding[0] + itemPositionAdjustment) * (index % self.desk.itemsPerLine),
                    initialPosition[1] + (self.deskItemSize[1] - self.desk.padding[1] + itemPositionAdjustment) * (index // self.desk.itemsPerLine)
            ]

            button = Button.Button(
                item.name,
                itemPosition.copy(),
                self.deskItemSize.copy(),
                item.father,
                externalFunction = item.externalFunction,
                imagePath = item.imagePath,
                audioPath = item.audioPath
            )

    def removeDeskItem(self,item):
        if item.name in self.deskItems :
            self.deskItems[item.name].father.handler.removeObject(item)

    def removeAllDeskItems(self):
        itemNames = list(self.deskItems.keys())
        for itemName in itemNames :
            self.removeDeskItem(self.deskItems[itemName])

    def cleanDesk(self):
        self.removeAllDeskItems()

    def save(self):
        print(f'{self.name}.save()')

    def close(self):
        self.save()
        self.cleanDesk()
        self.application.getFloor().handler.removeObject(self.desk)
