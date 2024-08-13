immutable_var = ([1,2],3, 'Привет', True)
print(immutable_var)
#print(type(immutable_var))
#immutable_war[0] = 25
#print(immutable_war) - не сработало из-за неизменяемости данных типа "tuple"
mutable_list = 1,2,3,4,5
mutable_list = list(mutable_list)
print(mutable_list)
#print(type(mutable_list))
mutable_list[0] = 25
print(mutable_list)