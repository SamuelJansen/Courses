from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()

print(
f'''pathMannanger = {pathMannanger}
pathMannanger.currentPath =                             {pathMannanger.currentPath}
pathMannanger.localPath =                               {pathMannanger.localPath}
pathMannanger.apiName =                                 {pathMannanger.apiName}
pathMannanger.apiPath =                                 {pathMannanger.apiPath}
pathMannanger.baseApiPath =                             {pathMannanger.baseApiPath}
pathMannanger.apiModules =                              {pathMannanger.apiModules}
pathMannanger.importMannangerRootInsideBaseApiPath =    {pathMannanger.importMannangerRootInsideBaseApiPath}
pathMannanger.globalsModule =                           {pathMannanger.globalsModule}
pathMannanger.globalsModulePath =                       {pathMannanger.globalsModulePath}''')