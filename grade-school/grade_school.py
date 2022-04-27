class School:
    def __init__(self):
        self.student_grades = {}
        self.roster_list = []
        self.added_list = []
    def add_student(self, name, grade):
        if name in self.student_grades:
            self.added_list.append(False)
        else:
            self.roster_list.append(name)
            self.student_grades[name] = grade
            self.added_list.append(True)
    def roster(self):
        r = sorted(self.roster_list)
        return sorted(r, key=lambda x: self.student_grades[x])
    def added(self):
        return self.added_list
    def grade(self, grade_number):
        return [
            name for name in self.roster()
            if self.student_grades[name] == grade_number
        ]