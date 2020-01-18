from model import Object

TAB = '        '

def isNotAplication(object) :
    print(f'{TAB}{object.name}.screen.fatherFunction.isNotAplication(object) --> object.name = {object.name}')
    print(f'{TAB}   isNotAplication = {object.name!=object.father.name}')
    print(f'{TAB}      object.name = {object.name}')
    print(f'{TAB}      object.father.name = {object.father.name}')
    return object.type!=Object.ObjectTypes.APLICATION
    # return object.name!=object.father.name and object.type!=object.father.type

def absoluteFather(aplication):
    return aplication
