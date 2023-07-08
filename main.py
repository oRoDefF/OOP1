class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        try:
            average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])
            result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
            return result
        except:
            return 'Недостаточно данных'

    def __lt__(self, other):
        self.average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])
        other.average_grade = sum([sum(grade) for grade in other.grades.values()]) / sum([len(grade) for grade in other.grades.values()])

        if not isinstance(other, Student):
            print('Это не студент')
        else:
            return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __str__(self):

        average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in lecturer_1.grades.values()])

        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade} '
        return result

    def __lt__(self, other):
        self.average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])
        other.average_grade = sum([sum(grade) for grade in other.grades.values()]) / sum([len(grade) for grade in other.grades.values()])

        if not isinstance(other, Student):
            print('Это не лектор')
        else:
            return self.average_grade < other.average_grade





class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)