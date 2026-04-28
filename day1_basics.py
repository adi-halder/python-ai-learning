# Python Day 1 - Basics
# BTech AI/ML | Vacation Learning

# Lists
marks = [85, 92, 78, 95, 88]
print("All marks:", marks)
print("First mark:", marks[0])
print("Average:", sum(marks) / len(marks))

# If/else
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
else:
    print("Grade: C")

# Functions
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"

students = [("Riya", 92), ("Arjun", 86), ("Priya", 73)]
for name, score in students:
    print(name, "→ Grade", calculate_grade(score))

# Marks analyzer - built from scratch!
def analyze_marks(marks):
    print("Max:", max(marks))
    print("Min:", min(marks))
    print("Average:", sum(marks) / len(marks))
    print("Total subjects:", len(marks))

analyze_marks([99, 82, 75, 83, 65, 97])
