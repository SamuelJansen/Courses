import UserInterface, Button
import applicationFunction, containerFunction

class Container(UserInterface.UserInterface):

    def __init__(self,position,size,father,
        itemsDto = None,
        fontSize = None,
        noImage = False,
        imagePath = None,
        audioPath = None
    ):

        name = f'{containerFunction.Attribute.NAME}.{father.name}'
        position = containerFunction.parsePosition(position,size,father)

        UserInterface.UserInterface.__init__(self,name,position,size,father,
            fontSize = fontSize,
            scale = None,
            padding = None,
            noImage = noImage,
            imagePath = imagePath,
            audioPath = audioPath
        )

        itemsFather = self
        if not itemsDto[0].position :
            for itemDto in itemsDto :
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
