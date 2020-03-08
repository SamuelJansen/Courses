import Message
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

    def updateDesk(self,itemsSessionDtoList,onDeskUpdate):
        self.desk.handler.removeObjectTree()
        itemsDto,itemsClass,priority = onDeskUpdate(itemsSessionDtoList,self)
        print(f'itemsDto = {itemsDto}')
        for itemDtoFeatures in itemsDto :
            print('newItemDto')
            for featureType in itemDtoFeatures :
                try :
                    for feature in featureType.values() :
                        print(f'    {feature}')
                except :
                    for feature in featureType :
                        print(f'    {feature}')
            print()
        print(f'itemsClass = {itemsClass}')
        print(f'priority = {priority}')
        self.application.memoryOptimizer.newObjects(itemsDto,itemsClass,
            priority = priority
        )

        for itemSessionDto in itemsSessionDtoList :
            self.addItemName(itemSessionDto)
        print(self.itemNames[self.page])

    def addItemName(self,itemDto):
        if self.page not in self.itemNames :
            self.itemNames[self.page] = []
        if itemDto.name not in self.itemNames[self.page] :
            self.itemNames[self.page].append(itemDto.name)

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
