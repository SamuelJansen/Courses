import os

import ItemSet, Event
import eventFunction, itemSetFunction

print('MenuEvent library imported')

class MenuEvent(Event.Event):

    def update(self):
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,object,apiModule,itemsPackage,itemsPathTree,
        name = None,
        type = eventFunction.Type.MENU_EVENT,
        inherited = False
    ):

        Event.Event.__init__(self,object,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited

        self.apiModule = apiModule
        self.itemsPackage = f'{itemsPackage}'
        self.itemsPathTree = itemsPathTree
        self.itemsPathTreePointer = self.getItemsPathTreePointer()
        self.itemsPath = self.getItemsPath()
        self.itemNamesFilePath = self.getItemNamesFilePath()
        self.itemNames = self.getItemNames()

        self.execute()

    def getItemsPathTreePointer(self):
        BACK_SLASH = self.application.pathMannanger.backSlash
        return len(self.itemsPathTree[:-1].split(BACK_SLASH)) - 1

    def getItemsPath(self):
        itemsPath = ''
        BACK_SLASH = self.application.pathMannanger.backSlash
        for itemNameIndex in range(self.itemsPathTreePointer+1) :
            itemsPath += f'{self.itemsPathTree[:-1].split(BACK_SLASH)[itemNameIndex]}{BACK_SLASH}'
        return f'{self.object.application.pathMannanger.getApiModulePath(self.apiModule)}{self.itemsPackage}{itemsPath}'

    def getItemNamesFilePath(self):
        BACK_SLASH = self.application.pathMannanger.backSlash
        return f'{self.getItemsPath()}{self.getItemsPath()[:-1].split(BACK_SLASH)[-1]}.{self.application.extension}'

    def getItemNames(self):
        itemNames = []
        names = os.listdir(self.itemsPath)
        for name in names :
            itemNames.append(name)
        return itemNames

    def buildItems(self,itemDirection,itemsExternalEvent):
        itemSetName = f'{itemSetFunction.Attribute.NAME}'
        itemSetPosition = self.object.getAbsolutePosition()
        itemSetFather = self.object

        ItemSet.ItemSet(itemSetName,itemSetPosition,itemSetFather,
            itemsName = self.itemNames,
            itemsText = self.itemNames,
            itemDirection = itemDirection,
            itemsExternalEvent = itemsExternalEvent,
            noImage = True,
            imagePath = None,
            soundPath = None
        )
