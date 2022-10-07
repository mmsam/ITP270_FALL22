#!/bin/python3

#Task-1
subjects = ["physics", "calculus", "poetry", "history"]

#Task-2
grades = [98, 97, 85, 88]

#Task-3
gradebook = [[subjects[0], grades[0]], [subjects[1], grades[1]], [subjects[2], grades[2]], [subjects[3], grades[3]]  ]

#Task-4
print(gradebook)

#Task-5
gradebook.append(["computer science", 100])

#Task-6
gradebook.append(["visual arts", 93])
#print(gradebook)

#Task-7
gradebook[5][1] = 98

#Task-8
gradebook[2].remove(85)

#Task-9
gradebook[2].append("Pass")
#print(gradebook)

#Task-10
last_semester_gradebook = [["Subject1", 90], ["Subject2", 88], ["Subject3", 87]]
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
