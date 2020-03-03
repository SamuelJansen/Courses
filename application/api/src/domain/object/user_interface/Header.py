import UserInterface, Button
import surfaceFunction, applicationFunction

print('Header library imported')

class Header(UserInterface.UserInterface):

    def __init__(self,name,position,size,father,
        items = None,
        itemSize = None,
        itemsImagePath = None,
        itemsAudioPath = None,
        text = None,
        textPosition = None,
        fontSize = None,
        padding = None
    ):

        padding,originalPadding = surfaceFunction.stashPadding(padding,father)

        UserInterface.UserInterface.__init__(self,name,position,size,father,
            text = text,
            textPosition = textPosition,
            fontSize = fontSize,
            padding = padding
        )

        self.padding = originalPadding

        self.items = items
        itemFather = self
        self.itemSize = surfaceFunction.parseSize(itemSize,itemFather)
        self.initialChildPosition = [0,0]
        self.itemsImagePath = itemsImagePath
        self.itemsAudioPath = itemsAudioPath

        self.buildItems()

    def buildItems(self):
        itemsAttributes = []
        itemFather = self
        for index in range(len(self.items)) :
            itemPosition = self.getItemPosition(index)
            itemsAttributes.append([
                [
                    self.items[index].name,
                    itemPosition.copy(),
                    self.itemSize.copy(),
                    itemFather,
                ],
                {
                    applicationFunction.Key.ON_LEFT_CLICK : self.items[index].onLeftClick,
                    applicationFunction.Key.IMAGE_PATH : self.itemsImagePath,
                    applicationFunction.Key.AUDIO_PATH : self.itemsAudioPath
                },
                {
                    applicationFunction.Key.PRIORITY : applicationFunction.Priority.HIGHT
                }
            ])
        self.application.memoryOptimizer.newObjects(itemsAttributes,Button.Button,
            priority = applicationFunction.Priority.HIGHT
        )

    def resetButtonsPosition(self):
        self.screen.reset()
        itemsList = list(self.handler.objects.values())
        for index in range(len(itemsList)) :
            itemPosition = surfaceFunction.getPositionPadded(self.getItemPosition(index),self.padding)
            button = itemsList[index]
            button.setPosition(itemPosition)

    def getItemPosition(self,index):
        return [
            index * (self.itemSize[0] - self.padding[0]) + self.initialChildPosition[0],
            self.initialChildPosition[1]
        ]
