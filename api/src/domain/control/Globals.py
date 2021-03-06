import os, sys

print('Globals library imported')

class AttributeKey:

    KW_API = 'api'
    KW_EXTENSION = 'extension'
    KW_DEPENDENCY = 'dependency'
    KW_LIST = 'list'

    GLOBALS_API_LIST = f'{KW_API}.{KW_LIST}'

    API_EXTENSION = f'{KW_API}.extension'
    UPDATE_GLOBALS = 'update-globals'
    PRINT_STATUS = 'print-status'
    DEPENDENCY_UPDATE = f'{KW_API}.{KW_DEPENDENCY}.update'
    DEPENDENCY_LIST = f'{KW_API}.{KW_DEPENDENCY}.{KW_LIST}'

    def getKey(api,key):
        return f'{api.apiName}.{key}'

    def getKeyByClassNameAndKey(cls,key):
        return f'{cls.__name__}.{key}'


class Globals:
    ### There are 'places' where backslash is not much wellcome
    ### Having it stored into a variable helps a lot
    TAB_UNITS = 2
    SPACE = ''' '''
    TAB = TAB_UNITS * SPACE
    BACK_SLASH = '''\\'''
    HASH_TAG = '''#'''
    COLON = ''':'''
    COMA = ''','''
    SPACE = ''' '''
    DOT = '''.'''
    NEW_LINE = '''\n'''
    BAR_N = '''\\n'''
    NOTHING = ''''''
    SINGLE_QUOTE = """'"""
    DOUBLE_QUOTE = '''"'''
    TRIPLE_SINGLE_QUOTE = """'''"""
    TRIPLE_DOUBLE_QUOTE = '''"""'''

    BASE_API_PATH = f'api{BACK_SLASH}src{BACK_SLASH}'
    LOCAL_GLOBALS_API_PATH = f'domain{BACK_SLASH}control{BACK_SLASH}'

    EXTENSION = 'gbl'
    PYTHON_EXTENSION = 'py'

    ENCODING = 'utf-8'
    OVERRIDE = 'w+'
    READ = 'r'

    RESOURCE_AS_PATH = f'resource{BACK_SLASH}'

    PIP_INSTALL = f'pip install'
    UPDATE_PIP_INSTALL = 'python -m pip install --upgrade pip'

    CHARACTERE_FILTER = [
        '__'
    ]

    NODE_IGNORE_LIST = [
        '.git',
        '__pycache__',
        '__init__',
        '__main__',
        'image',
        'audio'
    ]

    STRING = 'str'
    INTEGER = 'int'
    BOOLEAN = 'bool'

    TRUE = 'True'
    FALSE = 'False'

    OPEN_TUPLE_CLASS = 'tuple'
    OPEN_LIST_CLASS = 'list'
    DICTIONARY_CLASS = 'dict'
    OPEN_TUPLE = '('
    OPEN_LIST = '['
    OPEN_DICTIONARY = '{'

    SAFE_AMOUNT_OF_TRIPLE_SINGLE_OR_DOUBLE_QUOTES_PLUS_ONE = 4

    WRONG_WAY_TO_IMPLEMENT_IT = 'WRONG_WAY_TO_IMPLEMENT_IT'
    PROPER_WAY_TO_IMPLEMENT_IT = 'PROPER_WAY_TO_IMPLEMENT_IT'

    DEBUG = '[Debug]'

    def __init__(self,
        mode = PROPER_WAY_TO_IMPLEMENT_IT,
        encoding = ENCODING,
        debugStatus = False
    ):

        from pathlib import Path
        clear = lambda: os.system('cls')
        # clear() # or simply os.system('cls')

        self.globalsApiName = self.__class__.__name__

        self.mode = mode
        self.backSlash = Globals.BACK_SLASH
        self.charactereFilterList = Globals.CHARACTERE_FILTER
        self.nodeIgnoreList = Globals.NODE_IGNORE_LIST
        self.currentPath = f'{str(Path(__file__).parent.absolute())}{self.backSlash}'
        self.localPath = f'{str(Path.home())}{self.backSlash}'
        if encoding :
            self.encoding = encoding
        else :
            self.encoding = Globals.ENCODING
        self.backSlash = Globals.BACK_SLASH
        self.debugStatus = debugStatus
        if self.mode == Globals.PROPER_WAY_TO_IMPLEMENT_IT :
            self.baseApiPath = Globals.BASE_API_PATH
            self.apiPath = self.currentPath.split(self.baseApiPath)[0]
            self.apiName = self.apiPath.split(self.backSlash)[-2]
            self.apisRoot = self.currentPath.split(self.localPath)[1].split(self.apiName)[0]

            self.settingTree = self.getSettingTree()
            self.addSettingtree(f'{self.apiPath}{self.baseApiPath}{Globals.RESOURCE_AS_PATH}{self.apiName}.{self.extension}')

            self.printStatus = self.getGlobalsPrintStatus()
            self.apiNames = self.getGlobalsApiList()

            self.localGlobalsApiFilePath = f'{Globals.LOCAL_GLOBALS_API_PATH}{self.globalsApiName}.{Globals.PYTHON_EXTENSION}'
            self.globalsApiPath = f'{self.getApiPath(self.globalsApiName)}{self.localGlobalsApiFilePath}'
            self.apisPath = f'{self.backSlash.join(self.currentPath.split(self.localGlobalsApiFilePath)[-1].split(self.backSlash)[:-2])}{self.backSlash}'

            self.updateGlobals = self.getUpdateGlobalsClassFile()

            if self.printStatus :
                print(f'''                {self.__class__.__name__} = {self}
                {self.__class__.__name__}.currentPath =                 {self.currentPath}
                {self.__class__.__name__}.localPath =                   {self.localPath}
                {self.__class__.__name__}.baseApiPath =                 {self.baseApiPath}
                {self.__class__.__name__}.apiPath =                     {self.apiPath}
                {self.__class__.__name__}.apiName =                     {self.apiName}
                {self.__class__.__name__}.apisRoot =                    {self.apisRoot}
                {self.__class__.__name__}.apiNames =                    {self.apiNames}
                {self.__class__.__name__}.localGlobalsApiFilePath =     {self.localGlobalsApiFilePath}
                {self.__class__.__name__}.globalsApiName =              {self.globalsApiName}
                {self.__class__.__name__}.globalsApiPath =              {self.globalsApiPath}
                {self.__class__.__name__}.apisPath =                    {self.apisPath}
                {self.__class__.__name__}.extension =                   {self.extension}\n''')

                print('SettingsTree:')
                self.printTree(self.settingTree)

            self.update()

        elif self.mode == Globals.WRONG_WAY_TO_IMPLEMENT_IT :
            self.localGlobalsApiFilePath = f'{Globals.BASE_API_PATH}{Globals.LOCAL_GLOBALS_API_PATH}'
            self.baseApiPath = f'{self.backSlash.join(self.currentPath.split(self.localGlobalsApiFilePath)[-2].split(self.backSlash)[:-1])}{self.backSlash}'
            self.apisPath = f'{self.backSlash.join(self.currentPath.split(self.localGlobalsApiFilePath)[-2].split(self.backSlash)[:-2])}{self.backSlash}'

            self.apisTree = self.getPathTreeFromPath(self.apisPath)
            self.makePathTreeVisible(self.apisPath)

            if self.printStatus :
                print(f'''                {self.__class__.__name__} = {self}
                {self.__class__.__name__}.currentPath =                 {self.currentPath}
                {self.__class__.__name__}.localPath =                   {self.localPath}
                {self.__class__.__name__}.baseApiPath =                 {self.baseApiPath}
                {self.__class__.__name__}.localGlobalsApiFilePath =     {self.localGlobalsApiFilePath}
                {self.__class__.__name__}.apisPath =                    {self.apisPath}
                {self.__class__.__name__}.extension =                   {self.extension}\n''')
                self.printTree(self.apisTree)

    def getApiPath(self,apiName):
        return f'{self.localPath}{self.apisRoot}{apiName}{self.backSlash}{self.baseApiPath}'

    def update(self) :
        self.updateApplicationDependencies()
        self.updateGlobalsClassFile()
        self.makeApisAvaliable()

    def makeApisAvaliable(self) :
        self.apisTree = []
        for apiName in self.apiNames :
            apiTree = self.makePathTreeVisible(self.getApiPath(apiName))
            apiTree = {apiName:apiTree}
            self.apisTree.append(apiTree)
        if self.printStatus :
            print(f'{self.__class__.__name__}.apisTree')
            for apiTree in self.apisTree :
                print()
                self.printTree(apiTree)
            print()

    def makePathTreeVisible(self,path):
        node = {}
        nodeSons = os.listdir(path)
        for nodeSon in nodeSons :
            if self.nodeIsValid(nodeSon) :
                nodeSonPath = f'{path}{self.backSlash}{nodeSon}'
                try :
                    node[nodeSon] = self.makePathTreeVisible(nodeSonPath)
                except : pass
        sys.path.append(path)
        return node

    def nodeIsValid(self,node):
        return self.nodeIsValidByFilter(node) and (node not in self.nodeIgnoreList)

    def nodeIsValidByFilter(self,node):
        for charactere in self.charactereFilterList :
            if not len(node.split(charactere)) == 1 :
                return False
        return True

    def getPathTreeFromPath(self,path):
        node = {}
        nodeSons = os.listdir(path)
        for nodeSon in nodeSons :
            if self.nodeIsValid(nodeSon) :
                nodeSonPath = f'{path}{self.backSlash}{nodeSon}'
                try :
                    node[nodeSon] = self.getPathTreeFromPath(nodeSonPath)
                except : pass
        return node

    def getSettingTree(self,settingFilePath=None) :
        if not settingFilePath :
            settingFilePath = f'{self.apiPath}{self.baseApiPath}{Globals.RESOURCE_AS_PATH}{self.globalsApiName}.{Globals.EXTENSION}'

        with open(settingFilePath,Globals.READ,encoding=Globals.ENCODING) as settingsFile :
            allSettingLines = settingsFile.readlines()
        longStringCapturing = False
        quoteType = None
        longStringList = None
        depth = 0
        depthPass = None
        nodeRefference = 0
        nodeKey = Globals.NOTHING
        settingTree = {}
        for line, settingLine in enumerate(allSettingLines) :
            if not settingLine == Globals.NEW_LINE :
                if longStringCapturing :
                    if not depthPass :
                        depthPass = Globals.TAB_UNITS
                    if not currentDepth :
                        currentDepth = 0
                    longStringList.append(settingLine.split(Globals.HASH_TAG)[0][depth:])
                    if quoteType in str(settingLine) :
                        longStringList[-1] = Globals.NOTHING.join(longStringList[-1].split(quoteType))[:-1] + quoteType
                        settingValue = Globals.NOTHING.join(longStringList)
                        nodeKey = self.updateSettingTreeAndReturnNodeKey(nodeKey,settingTree,settingKey,settingValue)
                        longStringCapturing = False
                        quoteType = None
                        longStringList = None
                else :
                    currentDepth = self.getDepth(settingLine)
                    if currentDepth == depth :
                        settingKey,settingValue,nodeKey,longStringCapturing,quoteType,longStringList = self.settingsTreeInnerLoop(
                            settingLine,
                            nodeKey,
                            settingTree,
                            longStringCapturing,
                            quoteType,
                            longStringList
                        )
                    elif currentDepth > depth :
                        if not depthPass :
                            depthPass = currentDepth - depth
                        currentNodeRefference = currentDepth // (currentDepth - depth)
                        if currentNodeRefference - nodeRefference == 1 :
                            settingKey,settingValue,nodeKey,longStringCapturing,quoteType,longStringList = self.settingsTreeInnerLoop(
                                settingLine,
                                nodeKey,
                                settingTree,
                                longStringCapturing,
                                quoteType,
                                longStringList
                            )
                            nodeRefference = currentNodeRefference
                            depth = currentDepth
                    elif currentDepth < depth :
                        nodeRefference = currentDepth // depthPass
                        depth = currentDepth
                        splitedNodeKey = nodeKey.split(Globals.DOT)[:nodeRefference]
                        splitedNodeKeyLength = len(splitedNodeKey)
                        if splitedNodeKeyLength == 0 :
                            nodeKey = Globals.NOTHING
                        elif splitedNodeKeyLength == 1 :
                            nodeKey = splitedNodeKey[0]
                        else :
                            nodeKey = Globals.DOT.join(splitedNodeKey)
                        settingKey,settingValue,nodeKey,longStringCapturing,quoteType,longStringList = self.settingsTreeInnerLoop(
                            settingLine,
                            nodeKey,
                            settingTree,
                            longStringCapturing,
                            quoteType,
                            longStringList
                        )
                        depth = currentDepth
        if self.apiName not in settingTree.keys() :
            try : self.extension = settingTree[f'{self.globalsApiName}.{AttributeKey.API_EXTENSION}']
            except : self.extension = Globals.EXTENSION
        return settingTree

    def settingsTreeInnerLoop(self,settingLine,nodeKey,settingTree,longStringCapturing,quoteType,longStringList):
        settingKey,settingValue = self.getAttributeKeyValue(settingLine)
        settingValueAsString = str(settingValue)
        if settingValue and Globals.STRING == settingValue.__class__.__name__ :
            ammountOfTripleSingleOrDoubleQuotes = settingValue.count(Globals.TRIPLE_SINGLE_QUOTE) + settingValue.count(Globals.TRIPLE_DOUBLE_QUOTE)
        else :
            ammountOfTripleSingleOrDoubleQuotes = 0
        if settingValue and (Globals.TRIPLE_SINGLE_QUOTE in settingValueAsString or Globals.TRIPLE_DOUBLE_QUOTE in settingValueAsString) and ammountOfTripleSingleOrDoubleQuotes < Globals.SAFE_AMOUNT_OF_TRIPLE_SINGLE_OR_DOUBLE_QUOTES_PLUS_ONE :
            longStringCapturing = True
            splitedSettingValueAsString = settingValueAsString.split(Globals.TRIPLE_SINGLE_QUOTE)
            if Globals.TRIPLE_SINGLE_QUOTE in settingValueAsString and splitedSettingValueAsString and Globals.TRIPLE_DOUBLE_QUOTE not in splitedSettingValueAsString[0] :
                quoteType = Globals.TRIPLE_SINGLE_QUOTE
            else :
                quoteType = Globals.TRIPLE_DOUBLE_QUOTE
            longStringList = [settingValue + Globals.NEW_LINE]
        else :
            nodeKey = self.updateSettingTreeAndReturnNodeKey(nodeKey,settingTree,settingKey,settingValue)
        return settingKey,settingValue,nodeKey,longStringCapturing,quoteType,longStringList

    def addSettingtree(self,settingFilePath):
        newSetting = self.getSettingTree(settingFilePath)
        for settingKey in newSetting :
            self.settingTree[settingKey] = newSetting[settingKey]

    def getApiSetting(self,attributeKeyWithoutApiNameAsRoot):
        return self.getSetting(AttributeKey.getKey(self,attributeKeyWithoutApiNameAsRoot))

    def getSetting(self,nodeKey,settingTree=None) :
        if settingTree :
            return self.accessTree(nodeKey,settingTree)
        return self.accessTree(nodeKey,self.settingTree)

    def accessTree(self,nodeKey,tree) :
        if nodeKey == Globals.NOTHING :
            return tree
        else :
            nodeKeyList = nodeKey.split(Globals.DOT)
            lenNodeKeyList = len(nodeKeyList)
            if lenNodeKeyList > 0 and lenNodeKeyList == 1 :
                 nextNodeKey = Globals.NOTHING
            else :
                nextNodeKey = Globals.DOT.join(nodeKeyList[1:])
            return self.accessTree(nextNodeKey,tree[nodeKeyList[0]])

    def getAttributeKeyValue(self,settingLine):
        settingKey = self.getAttributeKey(settingLine)
        settingValue = self.getAttibuteValue(settingLine)
        return settingKey,settingValue

    def updateSettingTreeAndReturnNodeKey(self,nodeKey,settingTree,settingKey,settingValue):
        if settingValue or settingValue.__class__.__name__ == Globals.BOOLEAN :
            self.accessTree(nodeKey,settingTree)[settingKey] = settingValue
        else :
            self.accessTree(nodeKey,settingTree)[settingKey] = {}
            if Globals.NOTHING == nodeKey :
                nodeKey += f'{settingKey}'
            else :
                nodeKey += f'{Globals.DOT}{settingKey}'
        return nodeKey

    def getDepth(self,settingLine):
        depthNotFount = True
        depth = 0
        while not settingLine[depth] == Globals.NEW_LINE and depthNotFount:
            if settingLine[depth] == Globals.SPACE:
                depth += 1
            else :
                depthNotFount = False
        return depth

    def getAttributeKey(self,settingLine):
        possibleKey = self.filterString(settingLine)
        return settingLine.strip().split(Globals.HASH_TAG)[0].split(Globals.COLON)[0].strip()

    def getAttibuteValue(self,settingLine):
        possibleValue = self.filterString(settingLine)
        return self.getValue(Globals.COLON.join(possibleValue.strip().split(Globals.HASH_TAG)[0].split(Globals.COLON)[1:]).strip())

    def filterString(self,string) :
        if string[-1] == Globals.NEW_LINE :
            string = string[:-1]
        string = string.strip()
        return string

    def getValue(self,value) :
        if value :
            if Globals.OPEN_LIST == value[0] :
                return self.getList(value)
            elif Globals.OPEN_TUPLE == value[0] :
                return self.getTuple(value)
            elif Globals.OPEN_DICTIONARY == value[0] :
                return self.getDictionary(value)
            try :
                return int(value)
            except :
                try :
                    return float(value)
                except :
                    try :
                        if value == Globals.TRUE : return True
                        elif value == Globals.FALSE : return False
                        return value
                    except:
                        return value

    def getList(self,value):
        roughtValues = value[1:-1].split(Globals.COMA)
        values = []
        for value in roughtValues :
            values.append(self.getValue(value))
        return values

    def getTuple(self,value):
        roughtValues = value[1:-1].split(Globals.COMA)
        values = []
        for value in roughtValues :
            values.append(self.getValue(value))
        return tuple(values)

    def getDictionary(self,value) :
        splitedValue = value[1:-1].split(Globals.COLON)
        keyList = []
        for index in range(len(splitedValue) -1) :
            keyList.append(splitedValue[index].split(Globals.COMA)[-1].strip())
        valueList = []
        valueListSize = len(splitedValue) -1
        for index in range(valueListSize) :
            if index == valueListSize -1 :
                correctValue = splitedValue[index+1].strip()
            else :
                correctValue = Globals.COMA.join(splitedValue[index+1].split(Globals.COMA)[:-1]).strip()
            valueList.append(self.getValue(correctValue))
        resultantDictionary = {}
        for index in range(len(keyList)) :
            resultantDictionary[keyList[index]] = valueList[index]
        return resultantDictionary

    def printTree(self,tree):
        depth = 0
        self.printNodeTree(tree,depth)

    def printNodeTree(self,tree,depth):
        depthSpace = ''
        for nodeDeep in range(depth) :
            depthSpace += f'{Globals.TAB_UNITS * Globals.SPACE}'
        depth += 1
        for node in list(tree) :
            if tree[node].__class__.__name__ == Globals.DICTIONARY_CLASS :
                print(f'{depthSpace}{node}{Globals.SPACE}{Globals.COLON}')
                self.printNodeTree(tree[node],depth)
            else :
                print(f'{depthSpace}{node}{Globals.SPACE}{Globals.COLON}{Globals.SPACE}{tree[node]}')

    def updateApplicationDependencies(self):
        try :
            if self.getApiSetting(AttributeKey.DEPENDENCY_UPDATE) :
                import subprocess
                modules = self.getApiSetting(AttributeKey.DEPENDENCY_LIST)
                if modules :
                    subprocess.Popen(Globals.UPDATE_PIP_INSTALL).wait()
                    for module in modules :
                        subprocess.Popen(f'{Globals.PIP_INSTALL} {module}').wait()
        except : pass

    def getGlobalsPrintStatus(self):
        return self.getSetting(AttributeKey.getKeyByClassNameAndKey(Globals,AttributeKey.PRINT_STATUS))

    def getGlobalsApiList(self):
        return self.getSetting(AttributeKey.getKeyByClassNameAndKey(Globals,AttributeKey.GLOBALS_API_LIST))

    def getUpdateGlobalsClassFile(self):
        return self.getSetting(AttributeKey.getKeyByClassNameAndKey(Globals,AttributeKey.UPDATE_GLOBALS))

    def updateGlobalsClassFile(self):
        if self.updateGlobals and self.updateGlobals.__class__.__name__ == Globals.BOOLEAN :
            try :
                globalsScript = []
                with open(self.globalsApiPath,Globals.READ,encoding = Globals.ENCODING) as globalsFile :
                    for line in globalsFile :
                        globalsScript.append(line)
                for apiName in self.apiNames :
                    updatingApiPath =f'{self.getApiPath(apiName)}{self.localGlobalsApiFilePath}'
                    if apiName != self.globalsApiName :
                        with open(updatingApiPath,Globals.OVERRIDE,encoding = Globals.ENCODING) as globalsFile :
                            globalsFile.write(''.join(globalsScript))
            except :
                if self.printStatus :
                    print(f'''Globals api wans't found in your directory. {self.__class__.__name__} may not work properly in some edge cases''')

    def getExtension(self):
        return self.extension

    def getSettingFromSettingFilePathAndKeyPair(self,path,settingKey) :
        self.debug(f'''Getting {settingKey} from {path}''')
        with open(path,Globals.READ,encoding=Globals.ENCODING) as settingsFile :
            allSettingLines = settingsFile.readlines()
        for line, settingLine in enumerate(allSettingLines) :
            depth = self.getDepth(settingLine)
            setingKeyLine = self.getAttributeKey(settingLine)
            if settingKey == setingKeyLine :
                settingValue = self.getAttibuteValue(settingLine)
                self.debug(f'''{Globals.TAB}key : value --> {settingKey} : {settingValue}''')
                return settingValue

    def debug(self,string):
        if self.debugStatus :
            print(f'{Globals.DEBUG}{string}')
