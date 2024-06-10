array = [int(input('What Word?\n')) for x in range(5)]
array_ = []
for a in range(len(array)):
    if array[a-1] < array[a]:
        array_.append(array[a])




print(array_)