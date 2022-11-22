class Student:
    def __init__(self, id, name, course_id):
        self.id = id
        self.name = name
        self.course_id = course_id
        self.grade = -1

    def calculateGrade(self, test1, test2, test3, exam):
        grade = (test1*0.2) + (test2*0.2) + (test3*0.2) + (exam*0.4)
        self.grade = round(grade, 1)

        return 

    def __str__(self):
        return "{}, {}, {}, {}".format(self.id, self.name, self.course_id, self.grade)

    def __repr__(self):
        return "{}, {}, {}, {}".format(self.id, self.name, self.course_id, self.grade)
