import Modal, Container, Button
import surfaceFunction, objectFunction, eventFunction, applicationFunction, containerFunction

print('Message library imported')

class Message(Modal.Modal):

    STANDARD_SIZE = [300,180]

    def __init__(self,object,message,
        name = None,
        size = None,
        position = None,
        messageButtonsDto = None,
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
        fontSize = self.calculateFontSize(fontSize,father)
        textPosition = self.calculateTextPosition(size,fontSize)

        Modal.Modal.__init__(self,name,size,father,
            position = position,
            text = message,
            textPosition = textPosition,
            fontSize = fontSize,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            audioPath = audioPath
        )

        if messageButtonsDto :
            containerName = None
            containerFather = self
            containerPosition = [0,containerFunction.Attribute.BOTTOM]
            containerSize = ['100%',60]
            Container.Container(containerName,containerPosition,containerSize,containerFather,
                itemsDto = messageButtonsDto,
                fontSize = self.fontSize,
                noImage = True,
                imagePath = None,
                audioPath = None
            )

    def calculateSize(self,size,father):
        if not size :
            return Message.STANDARD_SIZE
        else :
            return surfaceFunction.parseSize(size,father)

    def calculatePosition(self,position,size,father):
        if not position :
            return [
                int((father.application.size[0] - size[0]) / 2),
                int((father.application.size[1] - size[1]) / 2 - (father.application.size[1] - size[1]) / 2 / 10) 
            ]

    def calculateFontSize(self,fontSize,father):
        if fontSize :
            return fontSize
        else:
            return father.application.standardFontSize

    def calculateTextPosition(self,size,fontSize):
        if size and fontSize :
            return [35,size[1]/2 - fontSize]
        return [0,0]

    def closeMessage(self):
        self.father.handler.removeObject(self)
