from __future__ import print_function
students = []
scoreList = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name,score])
    scoreList.append(score)
#students.sort(key=lambda x:x[1])
scoreSet = sorted(set(scoreList))
studentSecondLowestGrade = [x[0] for x in students if x[1] == scoreSet[1]]
studentSecondLowestGrade.sort()
print(*studentSecondLowestGrade, sep='\n')