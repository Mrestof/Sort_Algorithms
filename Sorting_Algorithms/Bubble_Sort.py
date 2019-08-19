import time

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

print('Have this list: \n' + str(num_list) + '\nStart sorting...')

start_time = time.time()

length_unsorted = len(num_list)
wp = length_unsorted - 1
i = [0, 0, 1]

while i[1] < length_unsorted:

    print('=' * len(str(num_list)))

    while i[0] < length_unsorted - i[2]:
        if num_list[wp] < num_list[wp - 1]:
            num_list[wp], num_list[wp - 1] = num_list[wp - 1], num_list[wp]

        wp -= 1
        i[0] += 1
        print(num_list)

    wp = length_unsorted - 1
    i[0] = 0
    i[1] += 1
    i[2] += 1

finish_time = time.time()

print('Sorting done' + '\nSorted list: ' + str(num_list) + '\nin '
      + str(round(finish_time - start_time, 5)) + ' seconds')
