if __name__ == '__main__':
    nested = []
    for _ in range(int(input())):
        li = []
        name = input()
        li.append(name)
        score = float(input())
        li.append(score)
        nested.append(li)
    print(nested)
    unique_marks = set()
    for i in range(len(nested)):
        unique_marks.add(nested[i][1])
    marks = list(unique_marks)
    marks.sort()
    print(marks)
    second_min = marks[1]
    print(second_min)
    second_min_names = []
    for names in range(len(nested)):
        if second_min == nested[names][1]:
            second_min_names.append(nested[names][0])
    second_min_names.sort()

    for names in range(len(second_min_names)):
        print(second_min_names[names])
