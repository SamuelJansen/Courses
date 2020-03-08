import setting, coursePathFunction

from tokenRepository import *

def add(event) :
    if event.application.session :
        audioExtension = 'mp3'
        imageExtension = 'png'
        backwardButton = f'{OPEN_SQUARE_BRACKETS}92x765 172x840{CLOSE_SQUARE_BRACKETS}'
        forwardButton = f'{OPEN_SQUARE_BRACKETS}1393x761 1500x844{CLOSE_SQUARE_BRACKETS}'
        audioNames = setting.getFileNames(f'{event.application.session.path}audio\\',audioExtension)
        imageNames = setting.getFileNames(f'{event.application.session.path}image\\',imageExtension)
        lessonScriptList = []
        for index in range(len(imageNames)) :
            scriptList = []
            if f'{index}' in audioNames :
                scriptList.append(f'audio{COLON}{index}')
            script = OPEN_SQUARE_BRACKETS
            for instruction in scriptList :
                script += f'{instruction} '
            script = f'{script.strip()}{CLOSE_SQUARE_BRACKETS}'
            lessonScriptList.append(f'{PAGE}{COLON}{index}{COMA}{IMAGE}{COLON}{imageNames[index]}{COMA}{BACKWARD_BUTTON}{COLON}{backwardButton}{COMA}{FOWARD_BUTTON}{COLON}{forwardButton}{COMA}{PAGE_SCRIPT}{COLON}{script}')
        lessonScriptPath = f'{event.application.session.path}{coursePathFunction.getLessonScriptName(event.application.session.path)}.{event.application.extension}'
        with open(lessonScriptPath,"w+",encoding="utf-8") as lessonScriptFile :
            lessonScriptFile.write('\n\n'.join(lessonScriptList))

    print(f'{event.name}.add()')
