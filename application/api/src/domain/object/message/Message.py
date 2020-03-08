import Modal, Container, Button
import surfaceFunction, objectFunction, eventFunction, applicationFunction, containerFunction

print('Message library imported')

class Message(Modal.Modal):

    def __init__(self,object,message,
        name = None,
        size = None,
        position = None,
        optionsDto = None,
        fontSize = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        audioPath = None
    ):

        father = object
        if not name :
            name = 'Message'
        size = self.calculateSize(size,father)
        position = self.calculatePosition(position,size,father)

        Modal.Modal.__init__(self,name,size,father,
            position = position,
            text = message,
            textPosition = [35,size[1]/2 - fontSize],
            fontSize = fontSize,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            audioPath = audioPath
        )

        if optionsDto :
            containerName = None
            containerFather = self
            containerPosition = [0,containerFunction.Attribute.BOTTOM]
            containerSize = ['100%',60]
            Container.Container(containerName,containerPosition,containerSize,containerFather,
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

    def closeMessage(self):
        self.father.handler.removeObject(self)
