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

num_heap = [num_list[0]]
i = [1, 1]

while i[1] < len(num_list):

    num_heap.append(num_list[i[0]])
    current_pos = len(num_heap) - 1
    parent_pos = int((current_pos + current_pos % 2 - 2) / 2)

    while current_pos != 0 and num_heap[current_pos] < num_heap[parent_pos]:
        num_heap[current_pos], num_heap[parent_pos] = num_heap[parent_pos], num_heap[current_pos]
        current_pos = parent_pos

        parent_pos = int((current_pos + current_pos % 2 - 2) / 2)

    i[0] += 1
    i[1] += 1

print('Have this heap: \n' + str(num_heap))

fin_list = []

while len(num_heap) != 0:
    num_heap[0], num_heap[len(num_heap) - 1] = num_heap[len(num_heap) - 1], num_heap[0]
    fin_list.append(num_heap[len(num_heap) - 1])
    num_heap.pop(len(num_heap) - 1)
    parent_pos = 0
    child_pos = [1, 2]

    while child_pos[0] < len(num_heap) and child_pos[1] < len(num_heap):
        if num_heap[child_pos[0]] <= num_heap[child_pos[1]] and num_heap[child_pos[0]] <= num_heap[parent_pos]:
            num_heap[child_pos[0]], num_heap[parent_pos] = num_heap[parent_pos], num_heap[child_pos[0]]
            parent_pos = child_pos[0]
        elif num_heap[child_pos[1]] <= num_heap[child_pos[0]] and num_heap[child_pos[1]] <= num_heap[parent_pos]:
            num_heap[child_pos[1]], num_heap[parent_pos] = num_heap[parent_pos], num_heap[child_pos[1]]
            parent_pos = child_pos[1]
        else:
            break

        child_pos = [2 * parent_pos + 1, 2 * parent_pos + 2]

    if child_pos[0] < len(num_heap) and num_heap[child_pos[0]] < num_heap[parent_pos]:
        num_heap[child_pos[0]], num_heap[parent_pos] = num_heap[parent_pos], num_heap[child_pos[0]]

    print('=' * len(str(num_heap)) + '\n' + str(num_heap))

finish_time = time.time()

print('Sorting done' + '\nSorted list: ' + str(fin_list) + '\nin '
      + str(round(finish_time - start_time, 5)) + ' seconds')
