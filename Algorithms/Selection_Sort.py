# Надо попробовать сортировать список, не работая только с одним, а создавая новый
import time

# num_list = []
#
# print('Start collecting nums')
#
# while True:
#     try:
#         user_num = int(input('Enter any num:'))
#     except ValueError:
#         print('Stop collecting nums')
#         break
#     num_list.append(user_num)

file = open('nums.txt', 'r')
file_list = file.read().split(':')
file.close()

num_list = []

for i in file_list:
    num_list.append(int(i))

print('=' * len(str(num_list)))

start_time = time.time()

i = [0, 0]

while i[1] < len(num_list):

    num_min = num_list[i[1]]
    pos_min = i[1]

    print(num_list)
    print('=' * len(str(num_list)))

    for num in num_list:
        if num < num_min and i[0] >= i[1]:
            num_min = num
            pos_min = i[0]
        i[0] += 1

    print('min: ' + str(num_min))
    print('pos min: ' + str(pos_min))
    print('pos now: ' + str(i[1]))

    num_list[i[1]], num_list[pos_min] = num_list[pos_min], num_list[i[1]]

    i[1] += 1
    i[0] = 0

    print('=' * len(str(num_list)))

finish_time = time.time()

print('Sorting done' + '\nSorted list: ' + str(num_list) + '\nin '
      + str(round(finish_time - start_time, 5)) + ' seconds')
