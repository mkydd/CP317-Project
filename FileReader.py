from Student import Student
from FileUtilities import FileUtilities

class FileReader():
    def fileReader(self, NameFile, CourseFile, GradeFileDirectory):

        # initialize a FileUtilities Object
        FileUtil = FileUtilities(NameFile, CourseFile)

        # open files containing data
        NameFile, CourseFile, GradeFile = FileUtil.openFiles(NameFile, CourseFile, GradeFileDirectory)


        # iterate through NameFile and extract each students info
        for line in NameFile.readlines():
            name_info = line.split(", ")
            name_info[-1] = name_info[-1].replace("\n", "") # remove newline character from last str object in array

            if (len(name_info) != 2):
                continue

            elif (not name_info[0].isnumeric()):
                continue


            # iterate through CourseFile, find any matching student data, _
            #   add this new data to GradeFile
            for data in CourseFile.readlines():
                course_info = data.split(", ")
                course_info[-1] = course_info[-1].replace("\n", "") # remove newline character from last str object in array

                if (len(course_info) != 6):
                    continue

                elif (not course_info[0].isnumeric()):
                    continue
                
                elif (not course_info[2].isnumeric() or not course_info[3].isnumeric() or not course_info[4].isnumeric() or not course_info[5].isnumeric()):
                    continue

                student = Student(name_info[0], name_info[1], course_info[1])

                if (course_info[0] == name_info[0]):   
                    # extract test scores
                    test1 = float(course_info[2])
                    test2 = float(course_info[3])
                    test3 = float(course_info[4])
                    exam = float(course_info[5])

                    # use student method to calculate the grade of the student
                    student.calculateGrade(test1, test2, test3, exam)

                    # place grade_info in GradeFile
                    GradeFile.write(repr(student) + '\n') # add newline char so next set of data is recorded on newline

                CourseFile.seek(0) # Move file pointer to start of CourseFile

        # close all files
        FileUtil.closeFiles(NameFile, CourseFile, GradeFile)


    
        

