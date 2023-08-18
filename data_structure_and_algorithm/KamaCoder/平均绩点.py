import sys


grade_dict = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
for line in sys.stdin:
    grade = line.split()
    avg = 0
    unknown = False
    for g in grade:
        if g not in grade_dict:
            print('Unknown')
            unknown = True
            break
        avg += grade_dict[g]
    if not unknown:
        print(round(avg/len(grade), 2))