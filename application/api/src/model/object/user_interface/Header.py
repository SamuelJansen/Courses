import Surface, UserInterface, Button
import modalFunction

print('Header library imported')

class Header(UserInterface.UserInterface):
    def __init__(self,name,position,size,father,
        itemsName = None,
        itemSize = None,
        padding = None
    ):

        padding,originalPadding = modalFunction.stashPadding(padding,father)

        UserInterface.UserInterface.__init__(self,name,position,size,father,
            padding = padding
        )

        self.padding = originalPadding
        self.itemsName = itemsName
        itemFather = self
        self.itemSize = Surface.parseSize(itemSize,itemFather)
        self.initialChildPosition = [0,0]

        self.buildItems()

    def setHeadderAttributesBack(self,tutor,originalPadding):
        self.tutor = tutor
        self.blitOrder = self.tutor.blitOrder + 1
        self.userInterfaceSurface = self.tutor.userInterfaceSurface
        self.padding = originalPadding
        self.handler.addRelative(self.tutor,[0,0])

    def buildItems(self):
        itemFather = self
        for itemIndex in range(len(self.itemsName)) :
            itemPosition = self.getItemPosition(itemIndex)
            itemName = self.itemsName[itemIndex]
            itemFunctionKey = self.itemsName[itemIndex]

            mewButton = Button.Button(
                itemName,
                itemPosition,
                self.itemSize,
                itemFather,
                functionKey = itemFunctionKey
            )

    def addButton(self,name,size):

        father = self
        size = Surface.parseSize(size,father)
        itemIndex = len(self.handler.objects)
        position = getItemPosition(itemIndex)
        functionKey = name

        mewButton = Button.Button(
            name,
            position,
            size,
            father,
            functionKey = functionKey
        )

    def resetButtonsPosition(self):
        self.screen.reset()
        itemsList = list(self.handler.objects.values())
        for itemIndex in range(len(itemsList)) :
            itemPosition = Surface.getPositionPadded(self.getItemPosition(itemIndex),self.padding)
            button = itemsList[itemIndex]
            button.setPosition(itemPosition)

    def getItemPosition(self,itemIndex):
        return [
            itemIndex * (self.itemSize[0] - self.padding[0]) + self.initialChildPosition[0],
            self.initialChildPosition[1]
        ].copy()
