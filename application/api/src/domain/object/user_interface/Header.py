import UserInterface, Button
import surfaceFunction

print('Header library imported')

class Header(UserInterface.UserInterface):

    def __init__(self,name,position,size,father,
        itemsName = None,
        itemsExternalFunction = None,
        itemSize = None,
        padding = None
    ):

        padding,originalPadding = surfaceFunction.stashPadding(padding,father)

        UserInterface.UserInterface.__init__(self,name,position,size,father,
            padding = padding
        )

        self.padding = originalPadding
        self.itemsName = itemsName
        self.itemsExternalFunction = itemsExternalFunction
        itemFather = self
        self.itemSize = surfaceFunction.parseSize(itemSize,itemFather)
        self.initialChildPosition = [0,0]

        self.buildItems()

    def buildItems(self):
        itemFather = self
        for itemIndex in range(len(self.itemsName)) :
            itemPosition = self.getItemPosition(itemIndex)
            itemName = self.itemsName[itemIndex]
            itemExternalFunction = self.itemsExternalFunction[itemIndex]

            Button.Button(
                itemName,
                itemPosition,
                self.itemSize,
                itemFather,
                externalFunction = itemExternalFunction
            )

    # def addButton(self,name,size):
    #     father = self
    #     size = surfaceFunction.parseSize(size,father)
    #     itemIndex = len(self.handler.objects)
    #     position = self.getItemPosition(itemIndex)
    #     externalFunction = name
    #
    #     mewButton = Button.Button(
    #         name,
    #         position,
    #         size,
    #         father,
    #         externalFunction = externalFunction
    #     )

    def resetButtonsPosition(self):
        self.screen.reset()
        itemsList = list(self.handler.objects.values())
        for itemIndex in range(len(itemsList)) :
            itemPosition = surfaceFunction.getPositionPadded(self.getItemPosition(itemIndex),self.padding)
            button = itemsList[itemIndex]
            button.setPosition(itemPosition)

    def getItemPosition(self,itemIndex):
        return [
            itemIndex * (self.itemSize[0] - self.padding[0]) + self.initialChildPosition[0],
            self.initialChildPosition[1]
        ].copy()
