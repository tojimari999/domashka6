class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and isinstance(grade, int) and 1 <= grade <= 10:
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course].append(grade)
            else:
                lecturer.grades_from_students[course] = [grade]
            return 'Успех'
        else:
            return 'Ошибка'

    def get_grade(self):
        sum_self_grades = 0
        cnt_self_grades = 0
        for grades in self.grades.values():
            sum_self_grades += sum(grades)
            cnt_self_grades += len(grades)

        self_grade = 0
        if cnt_self_grades != 0:
            self_grade = sum_self_grades / cnt_self_grades

        return self_grade

    def __str__(self):
        sum_all_grades = 0
        cnt_all_grades = 0
        for grades in self.grades.values():
            sum_all_grades += sum(grades)
            cnt_all_grades += len(grades)
        avg_grade = 'нет оценки'
        if cnt_all_grades != 0:
            avg_grade = sum_all_grades / cnt_all_grades
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other):
        return self.get_grade() == other.get_grade()

    def __ne__(self, other):
        return self.get_grade() != other.get_grade()

    def __gt__(self, other):
        return self.get_grade() > other.get_grade()

    def __lt__(self, other):
        return self.get_grade() < other.get_grade()

    def __ge__(self, other):
        return self.get_grade() >= other.get_grade()

    def __le__(self, other):
        return self.get_grade() <= other.get_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}

    def get_grades(self):
        return self.grades_from_students

    def get_grade(self):
        sum_self_grades = 0
        cnt_self_grades = 0
        for grades in self.grades_from_students.values():
            sum_self_grades += sum(grades)
            cnt_self_grades += len(grades)

        self_grade = 0
        if cnt_self_grades != 0:
            self_grade = sum_self_grades / cnt_self_grades

        return self_grade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_grade()}'

    def __eq__(self, other):
        return self.get_grade() == other.get_grade()

    def __ne__(self, other):
        return self.get_grade() == other.get_grade()

    def __gt__(self, other):
        return self.get_grade() > other.get_grade()

    def __lt__(self, other):
        return self.get_grade() < other.get_grade()

    def __ge__(self, other):
        return self.get_grade() >= other.get_grade()

    def __le__(self, other):
        return self.get_grade() <= other.get_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def get_avg_grade_of_homeworks(list_of_students, course):
    sum_all_grades = 0
    cnt_all_grades = 0
    for student in list_of_students:
        for name_course, grades in student.grades.items():
            if name_course == course:
                sum_all_grades += sum(grades)
                cnt_all_grades += len(grades)

    return None if cnt_all_grades == 0 else sum_all_grades / cnt_all_grades


def get_avg_grade_of_lecturers(list_of_lecturers, course):
    sum_all_grades = 0
    cnt_all_grades = 0
    for lecturer in list_of_lecturers:
        for name_course, grades in lecturer.grades_from_students.items():
            if name_course == course:
                sum_all_grades += sum(grades)
                cnt_all_grades += len(grades)

    return None if cnt_all_grades == 0 else sum_all_grades / cnt_all_grades


best_student = Student('Ruoy', 'Eman', 'your_gender')  # вызывается __init__
best_student.courses_in_progress += ['Python', 'Java']
best_student.finished_courses += ['Git']

# Задание 2

cool_lecturer = Lecturer('Some', 'Buddy')
cool_reviewer = Reviewer('Another', 'Buddy')
cool_lecturer.courses_attached += ['Python', 'Java']
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 1)
cool_reviewer.rate_hw(best_student, 'Python', 1)
cool_reviewer.rate_hw(best_student, 'Python', 1)

print(best_student.rate_lecture(cool_lecturer, 'Python', 10))
print(best_student.rate_lecture(cool_lecturer, 'Python', 9))
print(best_student.rate_lecture(cool_lecturer, 'Java', 1))
print(best_student.rate_lecture(cool_lecturer, 'Java', 1))

print(best_student.grades)
print(cool_lecturer.get_grades())

# Задание 3

print(best_student)
print(cool_lecturer)
print(cool_reviewer)

other_student = Student('Alexa', 'Fisher', 'helicopter')
other_student.courses_in_progress += ['Python']

cool_reviewer.rate_hw(other_student, 'Python', 10)
cool_reviewer.rate_hw(other_student, 'Python', 10)
cool_reviewer.rate_hw(other_student, 'Python', 10)

print(best_student == other_student)
print(best_student != other_student)
print(best_student > other_student)
print(best_student < other_student)
print(best_student >= other_student)
print(best_student <= other_student)

print('------')

other_lecturer = Lecturer('Vanya', 'Anya')
other_lecturer.courses_attached += ['Python']

other_student.rate_lecture(other_lecturer, 'Python', 1)
other_student.rate_lecture(other_lecturer, 'Python', 1)
other_student.rate_lecture(other_lecturer, 'Python', 1)

print(cool_lecturer == other_lecturer)
print(cool_lecturer != other_lecturer)
print(cool_lecturer > other_lecturer)
print(cool_lecturer < other_lecturer)
print(cool_lecturer >= other_lecturer)
print(cool_lecturer <= other_lecturer)

print('------')

# Задание 4
print(get_avg_grade_of_homeworks([best_student, other_student], 'Python'))
print(get_avg_grade_of_lecturers([cool_lecturer, other_lecturer], 'Python'))
