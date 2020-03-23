import Modal, Container, Button
import surfaceFunction, objectFunction, eventFunction, applicationFunction, containerFunction, sessionFunction

print('Message library imported')

class Message(Modal.Modal):

    STANDARD_SIZE = [300,180]

    def __init__(self,object,message,
        type = None,
        name = None,
        size = None,
        position = None,
        messageButtonsDto = None,
        fontSize = None,
        scale = None,
        padding = None,
        messageColor = None,
        noImage = False,
        surfaceColor = objectFunction.Attribute.MODAL_MESSAGE_COLOR,
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

        if not type :
            type = objectFunction.Type.MESSAGE

        Modal.Modal.__init__(self,name,size,father,
            type = type,
            position = position,
            text = message,
            textPosition = textPosition,
            fontSize = fontSize,
            scale = scale,
            padding = padding,
            noImage = noImage,
            surfaceColor = surfaceColor,
            imagePath = imagePath,
            audioPath = audioPath
        )

        # session = o\
        #     deskPosition = sessionFunction.getDeskPosition(object.application)
        #     deskSize = sessionFunction.getDeskSize(object.application)
        #
        # Modal.Modal.__init__(self,name,deskSize,father,
        #     type = type,
        #     position = deskPosition,
        #     fontSize = fontSize,
        #     scale = scale,
        #     padding = padding,
        #     noImage = True,
        #     surfaceColor = surfaceColor,
        #     imagePath = imagePath,
        #     audioPath = audioPath
        # )
        #
        # messageFather = self
        # containerFather = Container.Container(f'{name}.messageContainer',position,size,messageFather,
        #     itemsDto = [],
        #     text = message,
        #     textPosition = textPosition,
        #     fontSize = self.fontSize,
        #     noImage = False,
        #     imagePath = None,
        #     audioPath = None
        # )

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

        self.application.forcedUpdate()

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

    def close(self):
        self.father.handler.removeObject(self)
