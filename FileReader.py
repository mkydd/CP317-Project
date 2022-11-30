from Student import Student
from FileUtilities import FileUtilities

class FileReader():
    def fileReader(self, NameFile, CourseFile, GradeFileDirectory):

        # initialize a FileUtilities Object
        FileUtil = FileUtilities(NameFile, CourseFile)

        # open files containing data
        NameFile, CourseFile, GradeFile = FileUtil.openFiles(NameFile, CourseFile, GradeFileDirectory)

        errors = ""

        name_line_count = 0

        # iterate through NameFile and extract each students info
        for line in NameFile.readlines():
            name_info = line.split(", ")
            name_info[-1] = name_info[-1].replace("\n", "") # remove newline character from last str object in array

            name_line_count = name_line_count + 1

            if (len(name_info) != 2):
                error = "Error: Missing field -- NameFile line {}\n".format(name_line_count)
                if (not (error in errors)):
                    errors = errors + error

                continue

            elif (not name_info[0].replace(" ", "").isnumeric()):
                error = "Error: Student ID not a number -- NameFile line {}\n".format(name_line_count)
                if (not (error in errors)):
                    errors = errors + error

                continue

            found = False
            course_line_count = 0

            # iterate through CourseFile, find any matching student data, _
            #   add this new data to GradeFile
            for data in CourseFile.readlines():
                course_line_count = course_line_count + 1

                course_info = data.split(", ")

                # if end of file is reached and student umber not found in courseFile add error
                if (not("\n" in course_info[-1]) and course_info[0] != name_info[0] and not found):
                    error = "Error: No valid courses found for Student: {}\n".format(name_info[0])
                    if (not (error in errors)):
                        errors = errors + error
                    
                course_info[-1] = course_info[-1].replace("\n", "") # remove newline character from last str object in array

                # check if line in CourseFile contains all 6 fields
                if (len(course_info) != 6):
                    error = "Error: Missing field -- CourseFile line {}\n".format(course_line_count)
                    if (not (error in errors)):
                        errors = errors + error

                    continue

                # check if student number in current line is a number
                if (not course_info[0].replace(" ", "").isnumeric()):
                    error = "Error: Student ID not a number -- CourseFile line {}\n".format(course_line_count)
                    if (not (error in errors)):
                        errors = errors + error

                    continue
                
                # check if all grades in the current line are a number
                if ((not course_info[2].replace(" ", "").isnumeric()) or (not course_info[3].replace(" ", "").isnumeric()) or (not course_info[4].replace(" ", "").isnumeric()) or (not course_info[5].replace(" ", "").isnumeric())):
                    error = "Error: At least one grade is not a number -- CourseFile line {}\n".format(course_line_count)
                    if (not (error in errors)):
                        errors = errors + error

                    continue

                # check if course code is valid
                course = course_info[1]
                if (len(course) != 5):
                    error = "Error: Incorrect course code length -- CourseFile line {}\n".format(course_line_count)
                    if (not (error in errors)):
                        errors = errors + error

                    continue

                elif (not course[0:2].isalpha()):
                    error = "Error: First 2 characters of course code not letters -- CourseFile line {}\n".format(course_line_count)
                    if (not (error in errors)):
                        errors = errors + error

                    continue

                elif (not course[2:5].isnumeric()):
                    error = "Error: Last 3 characters of course code not numbers -- CourseFile line {}\n".format(course_line_count)
                    if (not (error in errors)):
                        errors = errors + error

                    continue

                student = Student(name_info[0].replace(" ", ""), name_info[1], course_info[1])

                if (course_info[0].replace(" ", "") == name_info[0].replace(" ", "")):   
                    # extract test scores
                    test1 = float(course_info[2])
                    test2 = float(course_info[3])
                    test3 = float(course_info[4])
                    exam = float(course_info[5])

                    # if any grade is less than 0 or greater than 100 dont add it to GradeFile
                    if (test1 < 0 or test1 > 100):
                        continue
                    elif (test2 < 0 or test2 > 100):
                        continue
                    elif (test3 < 0 or test3 > 100):
                        continue
                    elif (exam < 0 or exam > 100):
                        continue

                    # use student method to calculate the grade of the student
                    student.calculateGrade(test1, test2, test3, exam)

                    # place grade_info in GradeFile
                    GradeFile.write(repr(student) + '\n') # add newline char so next set of data is recorded on newline

                    found = True

                CourseFile.seek(0) # Move file pointer to start of CourseFile

        # if errors found write errors to error file
        if (len(errors) > 0):
            FileUtil.createErrorFile(errors)

        # close all files
        FileUtil.closeFiles(NameFile, CourseFile, GradeFile)

        # in console display any errors found 
        # print(errors)


    
        

