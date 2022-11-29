if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

    students = sorted(students,key=lambda x:x[1])
    second_lowest = sorted(list(set([x[1] for x in students])))[1]
    output = []
    for student in students:
        if student[1] == second_lowest:
            output.append(student[0])
    print("\n".join(sorted(output)))