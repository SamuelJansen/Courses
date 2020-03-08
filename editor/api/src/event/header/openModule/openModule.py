import MenuAccessEvent, MenuNavigationEvent

import pageSelection, textFunction

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
        onMenuResolve = pageSelection.pageSelection,
        navigationItemSize = [textFunction.Attribute.WORD_WIDTH,26]
    )
    print(f'{event.name}.openModule()')
