import setting, coursePathFunction

def add(event) :
    if event.application.session :
        audioExtension = 'mp3'
        imageExtension = 'png'
        backwardButton = '[92x765 172x840]'
        forwardButton = '[1393x761 1500x844]'
        audioNames = setting.getFileNames(f'{event.application.session.path}audio\\',audioExtension)
        imageNames = setting.getFileNames(f'{event.application.session.path}image\\',imageExtension)
        print(f'audioNames = {audioNames}')
        print(f'imageNames = {imageNames}')
        lessonScriptList = []
        for index in range(len(imageNames)) :
            scriptList = []
            if str(index) in audioNames :
                scriptList.append(f'audio:{index}')
            script = '['
            for instruction in scriptList :
                script += f'{instruction} '
            script = script.strip() + ']'
            lessonScriptList.append(f'page:{index},image:{imageNames[index]},BackwardButton:{backwardButton},ForwardButton:{forwardButton},script:{script}')
        lessonScriptPath = f'{event.application.session.path}{coursePathFunction.getLessonScriptName(event.application.session.path)}.{event.application.extension}'
        with open(lessonScriptPath,"w+",encoding="utf-8") as lessonScriptFile :
            lessonScriptFile.write('\n\n'.join(lessonScriptList))

    print(f'{event.name}.add()')
