array = [int(input('What Word?\n')) for x in range(5)]
array_ = []
print(array_)
print('Useless')
for a in range(len(array)):
    if array[a-1] < array[a]:
        array_.append(array[a])




print(array_)