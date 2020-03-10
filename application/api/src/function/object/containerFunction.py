import surfaceFunction

class Attribute:

    NAME = 'Container'

    ###- container and its items x and y direction
    CENTER = 'center'

    ###- y direction
    BOTTOM = 'bottom'

    ###- items x and y direction
    FILL = 'fill'

def parsePosition(position,size,father) :

    for feature in range(len(position)) :
        if position[feature] == Attribute.CENTER :
            position[feature] = (father.size[feature] - size[feature]) / 2

    if position[1] == Attribute.BOTTOM :
        position[1] = father.size[1] - size[1]

    return position

def parseItemsDtoPosition(father,
    itemsDto = []
) :
    for item in itemsDto :
        item.position = parsePosition(item.position,item.size,father)

    for feature in range(len(itemsDto[0].position)) :
        if itemsDto[0].position[feature] == Attribute.FILL :
            totalFeatureSize = 0
            for item in itemsDto :
                totalFeatureSize += item.size[feature] # surfaceFunction.parseSize(item.size,father)[feature]
            evenSpace = (father.size[feature] - totalFeatureSize) / (len(itemsDto) + 1)
            initialPosition = evenSpace
            cumulativeSizes = 0
            for index in range(len(itemsDto)) :
                if index > 0 :
                    cumulativeSizes += itemsDto[index - 1].size[feature]

                itemsDto[index].position[feature] = initialPosition + index * evenSpace + cumulativeSizes

    return itemsDto
