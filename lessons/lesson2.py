homework_completed = 12
hours_spent  = 1.5
course_title = 'Python'
time_on_task = hours_spent / homework_completed

print(
    f'Курс: {course_title}, '
    f'всего задач: {homework_completed}, '
    f'затрачено часов: {hours_spent}, '
    f'среднее время выполнения: {time_on_task:.3f}.'
)

# Обязательно писать в стиле snake_case? Если мне больше по душе camelCase? Или нужно привыкать к snake_case?