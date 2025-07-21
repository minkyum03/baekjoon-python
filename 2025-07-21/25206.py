# # 백준 25206번
# # 입력:
# ObjectOrientedProgramming1 3.0 A+
# IntroductiontoComputerEngineering 3.0 A+
# ObjectOrientedProgramming2 3.0 A0
# CreativeComputerEngineeringDesign 3.0 A+
# AssemblyLanguage 3.0 A+
# InternetProgramming 3.0 B0
# ApplicationProgramminginJava 3.0 A0
# SystemProgramming 3.0 B0
# OperatingSystem 3.0 B0
# WirelessCommunicationsandNetworking 3.0 C+
# LogicCircuits 3.0 B0
# DataStructure 4.0 A+
# MicroprocessorApplication 3.0 B+
# EmbeddedSoftware 3.0 C0
# ComputerSecurity 3.0 D+
# Database 3.0 C+
# Algorithm 3.0 B0
# CapstoneDesigninCSE 3.0 B+
# CompilerDesign 3.0 D0
# ProblemSolving 4.0 P
# # 출력:
# 3.284483

Student_grade = []

for i in range(3):
    major, credits, grade= input().split()
    credits = float(credits) #실수로 변환
    Student_info = {
        "major" : major,
        "credits" : credits,
        "grade" : grade
    }
    Student_grade.append(Student_info)

grade_to_point = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

total_points = 0
total_credits = 0
for student in Student_grade:
    credit = student["credits"]
    grade = student["grade"]

    if grade != 'P':
        total_credits += credit
        total_points += credit * grade_to_point[grade]

gpa = total_credits / total_points
print(round(gpa, 6))