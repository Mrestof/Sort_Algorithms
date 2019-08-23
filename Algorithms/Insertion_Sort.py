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

print('Have this list: \n' + str(num_list) + '\nStart sorting...')

start_time = time.time()

sorted_length = 1
i = [0, 1]

while i[1] < len(num_list):
    print('=' * len(str(num_list)) + '\n' + str(num_list) + '\n' + '=' * len(str(num_list)) +
          '\nLength of sorted: ' + str(sorted_length))

    i[0] = sorted_length

    while i[0] > 0:
        if num_list[i[0]] < num_list[i[0] - 1]:
            num_list[i[0]], num_list[i[0] - 1] = num_list[i[0] - 1], num_list[i[0]]
            i[0] -= 1
        else:
            break

    sorted_length += 1
    i[1] += 1

finish_time = time.time()

print('Sorting done' + '\nSorted list: ' + str(num_list) + '\nin '
      + str(round(finish_time - start_time, 5)) + ' seconds')
