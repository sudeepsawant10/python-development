"""
Get name and subjets of students 3, marks from 5 student and store it in list or dict so when you enter any name you will get that student subject marks.
"""

# student = []
# student_marks = []
# for x in range(0, 3):
#     name = input("Enter your name: ")
#     student.append(name)
#     marks = []
#     for m in range(0, 6):
#         m = int(input("Enter subject marks: "))
#         marks.append(m)
#     student_marks.append(marks)

# check = input("Enter name: ")

# # check name is present in student list
# if name in student:
#     x = student.index(name)
#     print(student_marks[x])
# else:
#     print("Student does not exists!")
# print("All student marks \n", student_marks)

"""
convert
list1 = [[1,2,3],[4,5,6]]
list2 = [[a,b,c],[d,e,f]]

into
list3 = [[1:'a', 2:'b', 3:'c'], [4:'d', 5:'e', 6: 'f']]
"""

# here list index are different for eg. to access 'b' list2[0][1]
list1 = [[1, 2, 3], [4, 5, 6]]
list2 = [['a', 'b', 'c'], ['d', 'e', 'f']]

list3 = []

dict1 = {}
for x in range(0, len(list1)):
    for y in range(0, len(list1)):
        dict1.update({list1[x][y]: list2[x][y]})
    list3.append(dict1)
print(list3)
