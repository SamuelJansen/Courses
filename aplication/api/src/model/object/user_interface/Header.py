from model.object.user_interface import UserInterface, UserInterfaceSurface, Button

print('Header library imported')

class Header(UserInterfaceSurface.UserInterfaceSurface):
    def __init__(self,name,position,size,father,
        scale = None,
        padding = [0,0],
        imagePath = None,
        soundPath = None
    ):

        UserInterfaceSurface.UserInterfaceSurface.__init__(
            self,
            name,
            position,
            size,
            father,
            scale = scale,
            padding = padding,
            imagePath = imagePath,
            soundPath = imagePath
        )

        self.previousChildrenPosition = [0,0]

    def addButton(self,name,size):

        father = self
        size = UserInterface.parseSize(size,father)
        size = UserInterface.getSizePadded(size,self.padding)

        position = [self.previousChildrenPosition[0],0].copy()
        position = UserInterface.getPositionPadded(position,self.padding)
        self.previousChildrenPosition = position.copy()
        self.previousChildrenPosition[0] = position[0] + size[0]

        functionKey = name

        Button.Button(
            name,
            position,
            size,
            functionKey,
            father,
        )

    def resetButtonsPosition(self):

        self.previousChildrenPosition = [0,0]
        self.screen.reset()

        for button in self.handler.objects.values() :
            position = [self.previousChildrenPosition[0],0].copy()
            position = UserInterface.getPositionPadded(position,self.padding)
            self.previousChildrenPosition = position.copy()
            self.previousChildrenPosition[0] = position[0] + button.size[0]
            button.setPosition(position)
            print(f'button.name = {button.name}, button.position = {position}')
