import Modal, Button
import surfaceFunction, itemSetFunction

print('ItemSet library imported')

class ItemSet(Modal.Modal):

    def __init__(self,name,position,father,
        externalFunction = None,
        itemsName = None,
        itemsText = None,
        itemSize = None,
        itemDirection = itemSetFunction.Type.DOWN,
        itemsExternalFunction = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        audioPath = None
    ):

        if not itemSize :
            itemSize = self.calculateItemSize(itemsText,father)

        size = self.calculateSize(itemDirection,itemSize,itemsName,father)

        Modal.Modal.__init__(
            self,name,position,size,father,
            externalFunction = externalFunction,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            audioPath = imagePath
        )

        self.selectable = False

        self.itemsName = itemsName
        self.itemDirection = itemDirection
        self.itemSize = surfaceFunction.parseSize(itemSize,father)

        self.itemsText = itemsText
        self.itemFontSize = self.getFontSize()

        self.itemsExternalFunction = itemsExternalFunction

        self.initialChildPosition = self.calculateInitialChildPosition()

        self.buildItems()

    def calculateItemSize(self,itemsText,father):
        if itemsText :
            largerItemText = 0
            for itemText in itemsText :
                if len(itemText) > largerItemText :
                    largerItemText = len(itemText)
            return [
                int(father.handler.originalSize[1] / 2 * largerItemText),
                father.handler.originalSize[1]
            ]
        else :
            return father.tutor.size

    def calculateSize(self,itemDirection,itemSize,itemsName,father):
        if itemDirection == itemSetFunction.Type.DOWN :
            return [
                itemSize[0],
                (itemSize[1] - father.padding[1]) * len(itemsName) + father.handler.originalSize[1]
            ]
        elif itemDirection == itemSetFunction.Type.RIGHT :
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
        if self.itemDirection == itemSetFunction.Type.DOWN :
            return [
                0,
                self.tutor.handler.getOriginalSize()[1] - self.padding[1]
            ]
        elif self.itemDirection == itemSetFunction.Type.RIGHT :
            return [
                self.tutor.handler.getOriginalSize()[0] - self.padding[0],
                0
            ]
        return None

    def buildItems(self):
        itemsFather = self

        for itemIndex in range(len(self.itemsName)) :
            if self.itemDirection == itemSetFunction.Type.DOWN :
                itemPosition = [
                    self.initialChildPosition[0],
                    self.initialChildPosition[1] + itemIndex * (self.itemSize[1] - self.padding[1])
                ]
            elif self.itemDirection == itemSetFunction.Type.RIGHT :
                itemPosition = [
                    self.initialChildPosition[0],
                    self.initialChildPosition[1] + itemIndex * (self.itemSize[1] - self.padding[1])
                ]

            if self.itemsExternalFunction :
                externalFunction = self.itemsExternalFunction
            else :
                externalFunction = self.itemsName[itemIndex]

            newItem = Button.Button(
                self.itemsName[itemIndex],
                itemPosition,
                self.itemSize.copy(),
                itemsFather,
                externalFunction = externalFunction
            )

            if self.itemsText :
                newItem.addText(
                    self.itemsText[itemIndex],
                    [surfaceFunction.getPositionPadded([0],self.padding)[0],surfaceFunction.getPositionPadded([0],self.padding)[0]],
                    self.itemFontSize
                )

        self.handler.addTutorImage(self.tutor,surfaceFunction.getPositionPadded([0,0],self.padding))
