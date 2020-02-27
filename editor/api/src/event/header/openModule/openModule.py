import MenuAccessEvent

import selectionPage

def openModule(event) :
    object = event.object
    apiModule = 'course'
    itemsPackage = 'resourse\\'
    itemsPathTree = 'modules\\'
    externalFunction = selectionPage.selectionPage

    MenuAccessEvent.MenuAccessEvent(
        object,
        apiModule,
        itemsPackage,
        itemsPathTree,
        externalFunction
    )
    print(f'{event.name}.openModule()')
