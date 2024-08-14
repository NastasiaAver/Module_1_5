# immutable_var = 'student', False, 96, 'Багратион', 1.55
# print(immutable_var)
# immutable_var[0] = 'teacher'
# print(immutable_var)
mutable_list = ['student', False, 96, 'Багратион', 1.99]
print(mutable_list)
mutable_list[0] = 'teacher'
mutable_list[1] = (mutable_list[3] != mutable_list[0])
mutable_list[-1] = int(mutable_list[-1])
print(mutable_list)