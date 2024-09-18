immutable_var = (1, 2, [3, 4], 'string', False)
print(immutable_var)
# кортежи являются неизменяеммым типом данных, поэтому при попытке изменить элемент кортежа, например, immutable_var[0] = 5, программа выдает ошибку, которая сообщает, что кортеж не поддерживает обращение по элементам
mutable_list = [1, 2,  'string', False]
mutable_list[0] = True
print(mutable_list)
