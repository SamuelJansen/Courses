import Modal, Container, Button
import surfaceFunction, objectFunction, eventFunction, applicationFunction

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

        # itemsMemoryOptimizationDto = []
        # for optionDto in optionsDto :
        #     itemsMemoryOptimizationDto.append([
        #         [
        #             optionDto.name,
        #             optionDto.position.copy(),
        #             optionDto.size.copy(),
        #             self,
        #         ],
        #         {
        #             applicationFunction.Key.ON_LEFT_CLICK : optionDto.onLeftClick,
        #             applicationFunction.Key.TEXT : optionDto.text,
        #             applicationFunction.Key.TEXT_POSITION : optionDto.textPosition,
        #             applicationFunction.Key.FONT_SIZE : self.fontSize,
        #             applicationFunction.Key.IMAGE_PATH : self.imagePath,
        #             applicationFunction.Key.AUDIO_PATH : self.audioPath
        #         },
        #         {
        #             applicationFunction.Key.PRIORITY : applicationFunction.Priority.HIGHT
        #         }
        #     ])
        # self.application.memoryOptimizer.newObjects(itemsMemoryOptimizationDto,Button.Button,
        #     priority = applicationFunction.Priority.HIGHT
        # )

        containerFather = self
        containerPosition = [0,50]
        containerSize = [300,100]
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
