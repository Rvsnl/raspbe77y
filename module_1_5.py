immutable_var = 1, 'hi', True, 3.2
print(immutable_var)
# immutable_var[2]= False
# print(immutable_var)
# значения элементов кортежа нельзя изменить, потому что в этом суть кортежа.
mutable_list = [3, 'second', 'home', 28]
print(mutable_list)
mutable_list[0] = 'food'
mutable_list[1] = 'at'
mutable_list.remove(28)
print(mutable_list)