import Modal, Container, Button
import surfaceFunction, objectFunction, eventFunction, applicationFunction, containerFunction

print('Message library imported')

class Message(Modal.Modal):

    def __init__(self,object,message,
        size = None,
        position = None,
        optionsDto = None,
        fontSize = None,
        scale = None,
        padding = None,
        noImage = True,
        imagePath = None,
        audioPath = None
    ):

        father = object
        name = f'Message.{object.name}'
        size = self.calculateSize(size,father)
        position = self.calculatePosition(position,size,father)

        Modal.Modal.__init__(self,name,size,father,
            position = position,
            fontSize = fontSize,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            audioPath = audioPath
        )

        self.message = message

        containerFather = self
        containerPosition = [0,containerFunction.Attribute.BOTTOM]
        containerSize = ['100%',30]
        Container.Container(containerPosition,containerSize,containerFather,
            itemsDto = optionsDto,
            fontSize = self.fontSize,
            noImage = True,
            imagePath = None,
            audioPath = None
        )

    def calculateSize(self,size,father):
        if not size :
            return [300,180]
        else :
            return surfaceFunction.parseSize(size,father)

    def calculatePosition(self,position,size,father):
        if not position :
            return [50,50]
