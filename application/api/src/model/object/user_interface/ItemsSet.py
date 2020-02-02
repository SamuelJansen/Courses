import Surface, Modal, Button

print('ItemSetCollumn library imported')

class ItemsSet(Modal.Modal):

    DOWN = 'down'

    def __init__(self,name,position,itemsFunctionKey,father,
        itemsName = [],
        itemsText = [],
        itemSize = [0,0],
        itemDirection = DOWN,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        self.selectable = False

        self.itemsName = itemsName
        self.itemsText = itemsText
        self.itemSize = Surface.parseSize(itemSize,father)
        print(f'        ItemsSet.itemSize = {self.itemSize}')
        self.itemDirection = itemDirection
        size = self.getSize(father)

        Modal.Modal.__init__(
            self,
            name,
            position,
            size,
            father,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = imagePath
        )

        self.itemsFunctionKey = itemsFunctionKey
        self.fontSize = self.getFontSize()
        print(f'ItemsSet.fontSize = {self.fontSize}')
        self.initialChildPosition = self.getInitialChildPosition()
        self.buildItems()

    def getFontSize(self):
        print(f'ItemsSet.padding = {self.padding}')
        return Surface.getSizePadded([self.itemSize[1]],self.padding)[0]

    def getInitialChildPosition(self):
        if self.itemDirection==ItemsSet.DOWN :
            return [0,self.modalFather.size[1]+self.padding[1]]
        else :
            return [0,0]

    def getSize(self,father):
        if self.itemDirection==ItemsSet.DOWN :
            return [self.itemSize[0],father.size[1]+self.itemSize[1]*len(self.itemsName)]
        else :
            return [0,0]

    def buildItems(self):
        size = self.itemSize
        functionKey = self.itemsFunctionKey
        father = self

        for itemIndex in range(len(self.itemsName)) :
            itemPosition = [0,self.initialChildPosition[1]+itemIndex*(self.itemSize[1]-self.padding[1])].copy()

            newItem = Button.Button(
                self.itemsName[itemIndex],
                itemPosition,
                size,
                functionKey,
                father,
            )
            print(f'ItemsSet.itemsText = {self.itemsText}, itemPosition = {newItem.position}, size = {newItem.size}')

            if self.itemsText :
                print(f'        self.itemsName[{itemIndex}].name = {newItem.name}, fontSize = {self.fontSize}')
                newItem.addText(
                    self.itemsText[itemIndex],
                    [Surface.getPositionPadded([0],self.padding)[0],Surface.getPositionPadded([0],self.padding)[0]],
                    self.fontSize
                )

        self.screen.mustUpdateNextFrame()
