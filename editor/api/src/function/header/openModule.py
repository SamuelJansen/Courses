import MenuAccessEvent, MenuNavigationEvent

import pageSelection, textFunction

def openModule(event) :

    pathMannanger = event.application.pathMannanger
    itemsPathTree = pathMannanger.getPathTreeFromPath(f'''{pathMannanger.getApiModulePath('course')}resourse\\modules\\''')

    MenuAccessEvent.MenuAccessEvent(
        event.object,
        itemsPathTree,
        onLeftClick = MenuNavigationEvent.MenuNavigationEvent,
        onMenuResolve = pageSelection.pageSelection,
        itemSize = [textFunction.Attribute.WORD_WIDTH,26]
    )

    print(f'{event.name}.openModule()')
