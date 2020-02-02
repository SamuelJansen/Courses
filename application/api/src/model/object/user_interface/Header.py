import Surface, Button

print('Header library imported')

class Header(Surface.Surface):
    def __init__(self,*args,**kargs):

        Surface.Surface.__init__(self,*args,**kargs)

        self.previousChildrenPosition = [0,0]

    def addButton(self,name,size):

        father = self
        size = Surface.parseSize(size,father)

        position = [self.previousChildrenPosition[0],0].copy()
        self.previousChildrenPosition = position.copy()
        self.previousChildrenPosition[0] = self.previousChildrenPosition[0] + size[0] - self.padding[0]

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
            position = Surface.getPositionPadded(position,self.padding)
            self.previousChildrenPosition = position.copy()
            self.previousChildrenPosition[0] = position[0] + button.size[0]
            button.setPosition(position)
            print(f'button.name = {button.name}, button.position = {position}')
