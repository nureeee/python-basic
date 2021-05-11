class Student:
    def __int__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

students = [
    Student("윤인성", 87, 93, 88, 67),
    Student("연하진", 78, 89, 74, 83),
    Student("가나다", 45, 56, 66, 67),
    Student("라마바", 45, 56, 67, 78)
]

print("이름", "총점", "평균", sep="\t")
for Student in students:
    print(Student.to_string())