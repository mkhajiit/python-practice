# 60점 이상인 학생들만 골라서, 이름과 함께 "합격" 이라고 출력하기
students = [
    ("철수", 85),
    ("영희", 58),
    ("민수", 70),
    ("지수", 45),
    ("하나", 90)
]

def passed_student(students):
  for student, score in students:
    if score >= 60:
      print(f"{student}:합격")

passed_student(students)