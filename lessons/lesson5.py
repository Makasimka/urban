immutable_var = (1, 2, 3, 'a', 'b', 'c', ['d', 'f', 'g'], True, None, )
print(immutable_var)

try:
    immutable_var[0] = 0
except:
    print("Кортеж - не список, его нельзя изменять, но можно изменять его изменяемые значения")

mutable_list = [1, 2, 3, 'a', 'b', 'c'] + [3, 4, 5,]
print(mutable_list)

mutable_list.extend(['d', 'e', 'f'])
print(mutable_list)

mutable_list.append(6)
print(mutable_list)

# Добавляем в начало списка "0"
mutable_list.insert(0, 0)
print(mutable_list)
print(mutable_list)

# Очистили список
mutable_list.clear()
print(mutable_list)