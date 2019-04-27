# -*- coding: utf-8 -*-
# 점수만 입력, 과목을 모름
class SimpleGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

# 과목명으로 세분화
class BySubjectGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)

        return total / count


class WeightedGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for subject, scores in by_subject.items():
            print(subject, scores)
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                print(score, weight)

        return total / count



# 함수 보다는 클래스화
# 튜플은 결국 데이터의 복잡도가 올라간다.
# 클래스로 분활 및 collection를 활용하자
import collections
Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


if __name__ == '__main__':
    book = SimpleGradeBook()
    book.add_student("Isaac")
    book.report_grade("Isaac", 90)
    book.report_grade("Isaac", 80)
    book.report_grade("Isaac", 100)

    print(book.average_grade("Isaac"))

    book = BySubjectGradeBook()
    book.add_student("Isaac")
    book.report_grade("Isaac", 'Maht', 90)
    book.report_grade("Isaac", 'Math', 80)
    book.report_grade("Isaac", 'Gym', 10)
    book.report_grade("Isaac", 'Gym', 20)

    print(book.average_grade("Isaac"))

    book = Gradebook()
    albert = book.student('albert')
    math = albert.subject('Math')
    math.report_grade(80, 0.10)
    print(albert.average_grade())
