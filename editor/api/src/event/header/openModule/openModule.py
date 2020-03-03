import MenuAccessEvent, MenuNavigationEvent

import pageSelection

def openModule(event) :
    object = event.object
    apiModule = 'course'
    itemsPackage = 'resourse\\'
    itemsPathTree = 'modules\\'

    MenuAccessEvent.MenuAccessEvent(
        object,
        apiModule,
        itemsPackage,
        itemsPathTree,
        onLeftClick = MenuNavigationEvent.MenuNavigationEvent,
        onMenuResolve = pageSelection.pageSelection
    )
    print(f'{event.name}.openModule()')
