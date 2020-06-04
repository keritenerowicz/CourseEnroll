'''
TODO
 - Why aren't the course files being read
'''

import courseenroll as ce

class CourseList:

    def __init__(self):
        self.adds = []
        self.dropMes = []

    # updates course list array
    def updateCourses(self):
        self.addMes = open('addcourses.txt').read().split('\n')
        self.dropMes = open('dropcourses.txt').read().split('\n')

    def deleteContents(fileName):
        f = open(fileName, 'r+')
        f.seek(0)
        f.truncate()

    # updates previous course list to most recent
    # self.courses is checked against this for updates

    # checks for course changes
    def addsDrops(self):
        self.updateCourses()
        addMes = self.addMes
        dropMes = self.dropMes
        if len(addMes) > 0:
            for courseNum in addMes:
                self.ce.adds(courseNum)
            self.deleteContents('addcourses.txt')
        elif len(dropMes) > 0:
            for courseNum in dropMes:
                self.ce.drops(courseNum)
            self.deleteContents('dropcourses.txt')
        self.updateCourses()
