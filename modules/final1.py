grades   = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = list(students)
students_list.sort()

grades_average = {}
for i, student in enumerate(students_list):
	# Можно округлить round(, 2), чтобы не получать слишком длинное число
	grades_average[student] = (sum(grades[i]) / len(grades[i]))

print(grades_average)