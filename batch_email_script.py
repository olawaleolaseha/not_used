
names = input("Enter names separated by commas: ").split(",")
assignments = input("Enter assignments number missed separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")


for name, assignment, grade in zip(names, assignments, grades):

    message = f"Hi {name},\n\nThis is a reminder that you have {assignment} assignments left to\nsubmit before you can graduate. You're current grade is {grade} and can increase\nto {int(grade) + int(assignment)*2} if you submit all assignments before the due date.\n\n"

    print(message)