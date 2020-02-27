import UserInterface, Button
import surfaceFunction

print('Header library imported')

class Header(UserInterface.UserInterface):

    def __init__(self,name,position,size,father,
        items = None,
        itemSize = None,
        itemsImagePath = None,
        itemsAudioPath = None,
        padding = None
    ):

        padding,originalPadding = surfaceFunction.stashPadding(padding,father)

        UserInterface.UserInterface.__init__(self,name,position,size,father,
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
            itemsAttributes.append([[
                self.items[index].name,
                itemPosition.copy(),
                self.itemSize.copy(),
                itemFather,
            ],
            {
                'externalFunction' : self.items[index].externalFunction,
                'imagePath' : self.itemsImagePath,
                'audioPath' : self.itemsAudioPath
            }])
        self.application.newObjects(itemsAttributes,Button.Button)

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
