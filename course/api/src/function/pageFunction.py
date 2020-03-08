import PathMannanger, CourseRepository
import courseFunction, coursePathFunction

class Attribute:

    NAME = 'Page'


def getPageNames(lessonScriptPath,plataform) :
    return CourseRepository.CourseRepository.getPageNamesFromLessonScriptPath(plataform.repository,lessonScriptPath)
