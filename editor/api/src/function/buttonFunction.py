buttonFunctions = {}
buttonFunction = lambda function:buttonFunctions.setdefault(function.__name__,function)

@buttonFunction
def nextPage(input) :
    print(f'    function called: nextPage({input})')
    pass

@buttonFunction
def previousPage(input) :
    print(f'    function called: previousPage({input})')
    pass

@buttonFunction
def exit():
    print(f'    function called: exit()')
    pass
