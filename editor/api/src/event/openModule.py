import MenuAccessEvent
import eventFunction

def openModule(event) :

    object = event.object
    apiModule = 'course'
    itemsPackage = 'resourse\\'
    itemsPathTree = 'modules\\'
    
    MenuAccessEvent.MenuAccessEvent(
        object,
        apiModule,
        itemsPackage,
        itemsPathTree
    )
    print(f'    EventFunction called: {event.object.name}.openModule()')
