import Modal, Button
import surfaceFunction, itemSetFunction, imageFunction, applicationFunction, textFunction

print('ItemSet library imported')

class ItemSet(Modal.Modal):

    def __init__(self,name,father,
        position = None,
        itemsDto = None,
        itemSize = None,
        itemsDirection = itemSetFunction.Type.DOWN,
        itemsPriority = applicationFunction.Priority.NO_PRIORITY,
        text = None,
        textPosition = None,
        fontSize = None,
        scale = None,
        padding = None,
        noImage = False,
        onLeftClick = None,
        onMenuResolve = None,
        imagePath = None,
        audioPath = None
    ):

        itemSize = self.parseItemSize(itemSize,itemsDto,father)

        size = self.calculateSize(itemsDirection,itemSize,itemsDto,father)

        Modal.Modal.__init__(self,name,size,father,
            position = position,
            onLeftClick = onLeftClick,
            onMenuResolve = onMenuResolve,
            text = text,
            textPosition = textPosition,
            fontSize = fontSize,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            audioPath = imagePath
        )

        self.selectable = False

        self.itemsDto = itemsDto
        self.itemsName = self.getItemsName()
        self.itemsDirection = itemsDirection
        self.itemsPriority = itemsPriority
        self.itemSize = surfaceFunction.parseSize(itemSize,father)
        self.itemFontSize = self.calculateFontSize()
        self.itemTextPosition = textFunction.calculateTextPositionPaddedOnMenu(self.itemSize,self.padding,self.itemFontSize)
        self.initialChildPosition = self.calculateInitialChildPosition()

        self.buildItems()

    def parseItemSize(self,itemSize,itemsDto,father):
        if itemSize :
            if itemSize[0] == textFunction.Attribute.WORD_WIDTH :
                if itemsDto[0].text :
                    largerItemText = 0
                    for itemDto in itemsDto :
                        if len(itemDto.text) > largerItemText :
                            largerItemText = len(itemDto.text)
                    return [
                        int(father.handler.originalSize[1] / 2 * largerItemText),
                        itemSize[1]
                    ]
        return father.tutor.size

    def calculateSize(self,itemsDirection,itemSize,itemsDto,father):
        if itemsDirection == itemSetFunction.Type.DOWN :
            return [
                itemSize[0],
                (itemSize[1] - father.padding[1]) * len(itemsDto) + father.handler.originalSize[1]
            ]
        elif itemsDirection == itemSetFunction.Type.RIGHT :
            return [
                itemSize[0] + father.handler.originalSize[0] - father.padding[0],
                (itemSize[1] - father.padding[1]) * len(itemsDto) + father.padding[1]
            ]

    def calculateFontSize(self):
        if self.itemsDto :
            return textFunction.calculateFontSize(self.itemSize,self.padding)
        else :
            return 0

    def calculateInitialChildPosition(self):
        if self.itemsDirection == itemSetFunction.Type.DOWN :
            if itemSetFunction.Attribute.NAME in self.tutor.father.handler.getInheritanceTree() :
                return [
                    0,
                    self.tutor.handler.getOriginalSize()[1] - self.padding[1]
                ]
            else :
                return [
                    0,
                    self.tutor.handler.getOriginalSize()[1]
                ]
        elif self.itemsDirection == itemSetFunction.Type.RIGHT :
            if itemSetFunction.Attribute.NAME in self.tutor.father.handler.getInheritanceTree() :
                return [
                    self.tutor.handler.getOriginalSize()[0] - self.padding[0],
                    0
                ]
            else :
                return [
                    self.tutor.handler.getOriginalSize()[0],
                    0
                ]

    def buildItems(self):
        itemsMemoryOptimizationDto = []
        itemsFather = self
        for index in range(len(self.itemsDto)) :
            if self.itemsDirection == itemSetFunction.Type.DOWN :
                itemPosition = [
                    self.initialChildPosition[0],
                    self.initialChildPosition[1] + index * (self.itemSize[1] - self.padding[1])
                ]
            elif self.itemsDirection == itemSetFunction.Type.RIGHT :
                itemPosition = [
                    self.initialChildPosition[0],
                    self.initialChildPosition[1] + index * (self.itemSize[1] - self.padding[1])
                ]
            itemsMemoryOptimizationDto.append([
                [
                    self.itemsDto[index].name,
                    itemPosition.copy(),
                    self.itemSize.copy(),
                    itemsFather,
                ],
                {
                    applicationFunction.Key.ON_LEFT_CLICK : self.itemsDto[index].onLeftClick,
                    applicationFunction.Key.ON_MENU_RESOLVE : self.itemsDto[index].onMenuResolve,
                    applicationFunction.Key.TEXT : self.itemsDto[index].text,
                    applicationFunction.Key.TEXT_POSITION : self.itemTextPosition,
                    applicationFunction.Key.FONT_SIZE : self.itemFontSize,
                    applicationFunction.Key.IMAGE_PATH : None,
                    applicationFunction.Key.AUDIO_PATH : None
                },
                {
                    applicationFunction.Key.PRIORITY : self.itemsPriority
                }
            ])

        self.application.memoryOptimizer.newObjects(itemsMemoryOptimizationDto,Button.Button,
            priority = self.itemsPriority
        )

    def getItemsName(self):
        return [itemDto.name for itemDto in self.itemsDto]

    def getItemsText(self):
        return [itemDto.text for itemDto in self.itemsDto]
