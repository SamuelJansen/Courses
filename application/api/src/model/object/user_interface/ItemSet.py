import Surface, Modal, Button

print('ItemSet library imported')

class ItemSet(Modal.Modal):

    DOWN = 'DOWN'
    RIGHT = 'RIGHT'

    def __init__(self,name,position,father,
        functionKey = None,
        itemsName = None,
        itemsText = None,
        itemSize = None,
        itemDirection = DOWN,
        itemsFunctionKey = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        self.selectable = False

        self.itemsName = itemsName
        self.itemDirection = itemDirection
        self.itemSize = Surface.parseSize(itemSize,father)
        print(f'                ItemSet.itemSize = {self.itemSize}')
        size = self.getSize(father)

        Modal.Modal.__init__(
            self,name,position,size,father,
            functionKey = functionKey,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = imagePath
        )

        self.itemsText = itemsText
        self.itemFontSize = self.getFontSize()
        print(f'                                ItemSet.itemFontSize = {self.itemFontSize}')

        self.itemsFunctionKey = itemsFunctionKey

        self.initialChildPosition = self.getInitialChildPosition()
        self.buildItems()

    def getSize(self,father):
        if self.itemDirection == ItemSet.DOWN :
            return [
                self.itemSize[0],
                self.itemSize[1] * len(self.itemsName) + father.size[1]
            ]
        elif self.itemDirection == ItemSet.RIGHT :
            return [
                self.itemSize[0] + father.size[0],
                self.itemSize[1] * len(self.itemsName)
            ]
        return None

    def getFontSize(self):
        print(f'ItemSet.padding = {self.padding}')
        if self.itemsText :
            return Surface.getSizePadded(self.itemSize,self.padding)[1]
        return None

    def getInitialChildPosition(self):
        if self.itemDirection == ItemSet.DOWN :
            return [
                0,
                self.modalFather.size[1] + self.padding[1]
            ]
        elif self.itemDirection == ItemSet.RIGHT :
            return [
                self.modalFather.size[0] + self.padding[0],
                0
            ]
        return None

    def buildItems(self):
        itemsFather = self

        for itemIndex in range(len(self.itemsName)) :
            if self.itemDirection == ItemSet.DOWN :
                itemPosition = [
                    0,
                    self.initialChildPosition[1] + itemIndex * (self.itemSize[1]-self.padding[1])
                ]
            elif self.itemDirection == ItemSet.RIGHT :
                itemPosition = [
                    self.initialChildPosition[0],
                    self.initialChildPosition[1] + itemIndex * (self.itemSize[1]-self.padding[1])
                ]

            if self.itemsFunctionKey :
                functionKey = self.itemsFunctionKey
            else :
                functionKey = self.itemsName[itemIndex]

            newItem = Button.Button(
                self.itemsName[itemIndex],
                itemPosition,
                self.itemSize.copy(),
                itemsFather,
                functionKey = functionKey
            )

            if self.itemsText :
                print(f'        ItemSet.itemsName[{itemIndex}].name = {newItem.name}, itemPosition = {newItem.position}, size = {newItem.size}, itemFontSize = {self.itemFontSize}')
                newItem.addText(
                    self.itemsText[itemIndex],
                    [Surface.getPositionPadded([0],self.padding)[0],Surface.getPositionPadded([0],self.padding)[0]],
                    self.itemFontSize
                )
