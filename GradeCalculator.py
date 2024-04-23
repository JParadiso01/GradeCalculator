
def calculate():
    grades = []
    percentages = []
    totals = []
    subsectionNames = []
    sum = 0
    amount = input("Enter how many subsections of the grade there are: ")

    for i in range(int(amount)):
        name = input("Enter the subsection name: ")
        subsectionNames.append(name)
        grade = input(f"Enter your grade in {name}: ")
        if grade.isnumeric():
            grades.append(grade)
        else:
            print("ERROR: You did not enter a number")
            exit(1)
        percentage = input(f"Enter what percentage of your final grade is {name} worth: ")
        if percentage.isnumeric() and int(percentage) <= 100:
            percentages.append(percentage)
            sum += int(percentage)
        else:
            print("ERROR: You did not enter a number or entered a number bigger than 100")
            exit(1)

    if sum != 100:
        print("ERROR: percentages do not add up to 100%")
        exit(1)

    for i in range(len(grades)):
        totals.append(int(grades[i])*(int(percentages[i])/100))
    
    totalSum = 0
    for t in totals:
        totalSum += t

    print(f"Your grade is {totalSum}")

def find():
    grades = []
    percentages = []
    totals = []
    subsectionNames = []
    sum = 0
    gradeToPass = input("Enter the grade you want to get: ")
    amount = input("Enter how many subsections of the grade there are: ")
    print("Enter a ? if this is the grade you want to find out")

    for i in range(int(amount)):
        name = input("Enter the subsection name: ")
        subsectionNames.append(name)
        grade = input(f"Enter your grade in {name}: ")
        if grade.isnumeric() or grade == '?':
            grades.append(grade)
        else:
            print("ERROR: You did not enter a number")
            exit(1)
        percentage = input(f"Enter what percentage of your final grade is {name} worth: ")
        if percentage.isnumeric() and int(percentage) <= 100:
            percentages.append(percentage)
            sum += int(percentage)
        else:
            print("ERROR: You did not enter a number or entered a number bigger than 100")
            exit(1)

    if sum != 100:
        print("ERROR: percentages do not add up to 100%")
        exit(1)

    for i in range(len(grades)):
        if (grades[i] == '?'):
            impPercentage = int(percentages[i])/100
            subsect = subsectionNames[i]
            continue
        totals.append(int(grades[i])*(int(percentages[i])/100))

    totalSum = 0
    for t in totals:
        totalSum += t

    passingGrade = (int(gradeToPass) - totalSum)/impPercentage

    print()
    print(f"The grade you need to get in {subsect} to get a {gradeToPass} is {passingGrade}")


def main():
    choice = input("Would you like to calculate your grade or find what grade is needed to get a specific grade? (calculate/find) ")
    if choice.lower() == "calculate":
        calculate()
    elif choice.lower() == "find":
        find()
    else:
        print("ERROR: choose one of the options (calculate or find)")
        exit(1)

if __name__ == '__main__':
    main()
