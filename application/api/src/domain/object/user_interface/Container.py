import UserInterface, Button
import applicationFunction, containerFunction

class Container(UserInterface.UserInterface):

    def __init__(self,name,position,size,father,
        itemsDto = None,
        text = None,
        textPosition = None,
        fontSize = None,
        noImage = False,
        surfaceColor = None,
        imagePath = None,
        audioPath = None
    ):

        if not name :
            name = f'{containerFunction.Attribute.NAME}.{father.tutor.name}'
        position = containerFunction.parsePosition(position,size,father)

        UserInterface.UserInterface.__init__(self,name,position,size,father,
            text = text,
            textPosition = textPosition,
            fontSize = fontSize,
            scale = None,
            padding = None,
            noImage = noImage,
            surfaceColor = surfaceColor,
            imagePath = imagePath,
            audioPath = audioPath
        )

        if itemsDto :
            itemsFather = self
            for itemDto in itemsDto :
                if not itemDto.position :
                    itemDto.position = [
                        containerFunction.Attribute.FILL,
                        containerFunction.Attribute.CENTER
                    ]
            itemsDto = containerFunction.parseItemsDtoPosition(itemsFather,
                itemsDto = itemsDto
            )

            itemsMemoryOptimizationDto = []
            for itemDto in itemsDto :
                itemsMemoryOptimizationDto.append([
                    [
                        itemDto.name,
                        itemDto.position.copy(),
                        itemDto.size.copy(),
                        itemsFather
                    ],
                    {
                        applicationFunction.Key.TEXT : itemDto.text,
                        applicationFunction.Key.TEXT_POSITION : itemDto.textPosition,
                        applicationFunction.Key.FONT_SIZE : self.fontSize,
                        applicationFunction.Key.ON_LEFT_CLICK : itemDto.onLeftClick,
                        applicationFunction.Key.IMAGE_PATH : self.imagePath,
                        applicationFunction.Key.AUDIO_PATH : self.audioPath
                    },
                    {
                        applicationFunction.Key.PRIORITY : applicationFunction.Priority.HIGHT
                    }
                ])
            self.application.memoryOptimizer.newObjects(itemsMemoryOptimizationDto,Button.Button,
                priority = applicationFunction.Priority.HIGHT
            )
