import os
from Files import Files

class FileErrorHandling(Files):
    def __init__(self, NameFile, CourseFile, GradeFileDirectory) -> None:
        super().__init__(NameFile, CourseFile)
        self.GradeFileDirectory = GradeFileDirectory

    def isEmpty(self):
        # returns true if either file is empty, false if both files contain text
        NameFile = os.stat(self.NameFile)
        CourseFile = os.stat(self.CourseFile)
        
        return (not(NameFile.st_size and CourseFile.st_size)) 

    def validGradeFileDirectory(self):
        if (not self.GradeFileDirectory):
            print("no grade file directory selected")
            return False
    
