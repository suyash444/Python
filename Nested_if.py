def scores():

        students = []
        for _ in range(int(input("Enter the range:"))):
            name = input("Enter the name:")
            score = float(input("Enter the score:"))
            students.append([name, score])

        # sort the list by grade
        students.sort(key=lambda x: x[1])

        # find the second lowest grade
        # find the second lowest grade
        second_lowest_grade = None
        lowest_grade = students[0][1]
        for student in students:
            if student[1] > lowest_grade:
                if second_lowest_grade is None or student[1] < second_lowest_grade:
                    second_lowest_grade = student[1]

    # print the names of any students with the second lowest grade
        for student in students:
            if student[1] == second_lowest_grade:
                print(student[0])
scores()