import MenuAccessEvent
import eventFunction
from event.pageSelection import *

def openModule(event) :

    object = event.object
    apiModule = 'course'
    itemsPackage = 'resourse\\'
    itemsPathTree = 'modules\\'
    externalFunction = pageSelection

    MenuAccessEvent.MenuAccessEvent(
        object,
        apiModule,
        itemsPackage,
        itemsPathTree,
        externalFunction
    )
    print(f'    EventFunction called: {event.object.name}.openModule()')
