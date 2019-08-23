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

st = time.time()

num_list.sort()

ft = time.time()

print('Sorting done' + '\nSorted list: ' + str(num_list) + '\nin '
      + str(round(ft - st, 5)) + ' seconds')
