import Modal, Button
import surfaceFunction

print('ItemSet library imported')

class ItemSet(Modal.Modal):

    ABOVE_LEFT = 'ABOVE_LEFT'

    DOWN = 'DOWN'
    RIGHT = 'RIGHT'

    def __init__(self,name,position,father,
        externalEvent = None,
        itemsName = None,
        itemsText = None,
        itemSize = None,
        itemDirection = DOWN,
        itemsExternalEvent = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        size = self.calculateSize(itemDirection,itemSize,itemsName,father)

        Modal.Modal.__init__(
            self,name,position,size,father,
            externalEvent = externalEvent,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = imagePath
        )

        self.selectable = False

        self.itemsName = itemsName
        self.itemDirection = itemDirection
        self.itemSize = surfaceFunction.parseSize(itemSize,father)

        self.itemsText = itemsText
        self.itemFontSize = self.getFontSize()

        self.itemsExternalEvent = itemsExternalEvent

        self.initialChildPosition = self.calculateInitialChildPosition()

        self.buildItems()

    def calculateSize(self,itemDirection,itemSize,itemsName,father):
        if itemDirection == ItemSet.DOWN :
            return [
                itemSize[0],
                (itemSize[1] - father.padding[1]) * len(itemsName) + father.handler.originalSize[1]
            ]
        elif itemDirection == ItemSet.RIGHT :
            return [
                itemSize[0] + father.handler.originalSize[0] - father.padding[0],
                (itemSize[1] - father.padding[1]) * len(itemsName) + father.padding[1]
            ]
        return None

    def getFontSize(self):
        if self.itemsText :
            return surfaceFunction.getSizePadded(self.itemSize,self.padding)[1]
        else :
            return 0

    def calculateInitialChildPosition(self):
        if self.itemDirection == ItemSet.DOWN :
            return [
                0,
                self.tutor.handler.getOriginalSize()[1] - self.padding[1]
            ]
        elif self.itemDirection == ItemSet.RIGHT :
            return [
                self.tutor.handler.getOriginalSize()[0] - self.padding[0],
                0
            ]
        return None

    def buildItems(self):
        itemsFather = self

        for itemIndex in range(len(self.itemsName)) :
            if self.itemDirection == ItemSet.DOWN :
                itemPosition = [
                    self.initialChildPosition[0],
                    self.initialChildPosition[1] + itemIndex * (self.itemSize[1] - self.padding[1])
                ]
            elif self.itemDirection == ItemSet.RIGHT :
                itemPosition = [
                    self.initialChildPosition[0],
                    self.initialChildPosition[1] + itemIndex * (self.itemSize[1] - self.padding[1])
                ]

            if self.itemsExternalEvent :
                externalEvent = self.itemsExternalEvent
            else :
                externalEvent = self.itemsName[itemIndex]

            newItem = Button.Button(
                self.itemsName[itemIndex],
                itemPosition,
                self.itemSize.copy(),
                itemsFather,
                externalEvent = externalEvent
            )

            if self.itemsText :
                newItem.addText(
                    self.itemsText[itemIndex],
                    [surfaceFunction.getPositionPadded([0],self.padding)[0],surfaceFunction.getPositionPadded([0],self.padding)[0]],
                    self.itemFontSize
                )

        self.handler.addTutorImage(self.tutor,surfaceFunction.getPositionPadded([0,0],self.padding))
