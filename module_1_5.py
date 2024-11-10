immutable_var = 1,2,'a','b'
print('immutable_var:', immutable_var)
#immutable_var[0] = 5
#print(immutable_var)  элементы кортежа являются неизменяемыми
mutable_list = [1,2,'a','b']
mutable_list[0] = 5
mutable_list.append('Modified')
print('mutable_list:', mutable_list)