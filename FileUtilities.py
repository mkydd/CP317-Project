from Files import Files

class FileUtilities(Files):
    def __init__(self, NameFile, CourseFile) -> None:
        super().__init__(NameFile, CourseFile)
        self.GradeFileDirectory = ""

    def openFiles(self, NameFile, CourseFile, GradeFileDirectory):
        self.GradeFileDirectory = GradeFileDirectory

        NameFile = open(NameFile, 'r', encoding="utf-8")
        CourseFile = open(CourseFile, 'r', encoding="utf-8")

        #  create new file to store maipulated data
        GradeFile = open(str(GradeFileDirectory) + "/GradeFile.txt", 'w+', encoding="utf-8")
        
        return NameFile, CourseFile, GradeFile

    def closeFiles(self, NameFile, CourseFile, GradeFile):
        NameFile.close()
        CourseFile.close()
        GradeFile.close()

    def createErrorFile(self, errors):
        ErrorFile = open(str(self.GradeFileDirectory) + "/ErrorFile.txt", 'w+', encoding="utf-8")

        ErrorFile.write(errors)

        ErrorFile.close()

        return