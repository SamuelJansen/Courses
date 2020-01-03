def parseName(name) :
    try :
        nameSplited = name.split()
        name = nameSplited[0]
        try :
            if len(nameSplited)>1 :
                print(f'len(nameSplited) = {len(nameSplited)}, nameSplited = {nameSplited}')
                try :
                    indice = int(nameSplited[1])
                    indice = nameSplited[1]
                except :
                    print(f'parseName(name) error --> nameSplited[1] = {nameSplited[1]}')
                    indice = 'indiceNotParsed'
            else :
                indice = '1'
        except :
            print(f'parseName(name) error --> nameSplited = {nameSplited}')
            indice = 'indiceNotParsed'
    except :
        print(f'parseName(name) error --> name = {name}')
        name = 'nameNotParsed'
        indice = 'indiceNotParsed'
    return name + ' ' + indice
