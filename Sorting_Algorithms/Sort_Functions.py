import time

file = open('nums.txt', 'r')
file_list = file.read().split(':')
file.close()

num_list = []

for i in file_list:
    num_list.append(int(i))


def sort_test(original_list: list, sorted_list: list):
    """
    This function takes two lists: 'unsorted' and 'sorted by one of algorithms'.
    If list sorted correctly it returns 1, in other case - 0.

    :param list original_list: unsorted list
    :param list sorted_list: output from one of sort functions
    :return: 1 or 0
    """
    list1 = list(original_list)
    list1.sort()
    if list1 == sorted_list:
        return 1
    else:
        return 0


def bubble_sort(int_list: list):
    """
    This function implements 'Bubble Sort' algorithm.

    :param list int_list: list to sort
    :return: sorted list and execution time
    """
    int_list = list(int_list)

    start_time = time.time()

    length_unsorted = len(int_list)
    wp = length_unsorted - 1
    counter = [0, 0, 1]

    while counter[1] < length_unsorted:

        while counter[0] < length_unsorted - counter[2]:
            if int_list[wp] < int_list[wp - 1]:
                int_list[wp], int_list[wp - 1] = int_list[wp - 1], int_list[wp]

            wp -= 1
            counter[0] += 1

        wp = length_unsorted - 1
        counter[0] = 0
        counter[1] += 1
        counter[2] += 1

    finish_time = time.time()

    return {'list': int_list, 'time': finish_time - start_time}


def quick_sort(int_list: list):
    """
    This function implements 'Quick Sort' algorithm.

    :param list int_list: list to sort
    :return: sorted list and execution time
    """
    def q_s(l: list):

        if len(l) <= 1:
            return l

        base_pointer = len(l) - 1
        left_pointer = 0
        right_pointer = base_pointer - 1

        while 1:
            while l[left_pointer] < l[base_pointer] and left_pointer < len(l) - 1:
                left_pointer += 1

            while l[right_pointer] >= l[base_pointer] and right_pointer > left_pointer:
                right_pointer -= 1

            if right_pointer == left_pointer or left_pointer == base_pointer:
                sorted_pointer = left_pointer
                l[base_pointer], l[left_pointer] = l[left_pointer], l[base_pointer]
                break

            l[right_pointer], l[left_pointer] = l[left_pointer], l[right_pointer]

        l1 = l[:sorted_pointer]
        l2 = l[sorted_pointer + 1:]

        tmp_list = q_s(l1)
        tmp_list.append(l[sorted_pointer])

        return tmp_list + q_s(l2)
    int_list = list(int_list)

    start_time = time.time()
    sorted_list = q_s(int_list)
    finish_time = time.time()

    return {'list': sorted_list, 'time': finish_time - start_time}


def merge_sort(int_list: list):
    """
    This function is in development
    :param list int_list: list to sort
    :return: sorted list and execution time
    """
    int_list = list(int_list)

    return {'list': int_list, 'time': None}


def selection_sort(int_list: list):
    """
    This function implements 'Selection Sort' algorithm.

    :param list int_list: list to sort
    :return: sorted list and execution time
    """
    int_list = list(int_list)

    start_time = time.time()

    counter = [0, 0]

    while counter[1] < len(int_list):

        num_min = int_list[counter[1]]
        pos_min = counter[1]

        for num in int_list:
            if num < num_min and counter[0] >= counter[1]:
                num_min = num
                pos_min = counter[0]
            counter[0] += 1

        int_list[counter[1]], int_list[pos_min] = int_list[pos_min], int_list[counter[1]]

        counter[1] += 1
        counter[0] = 0

    finish_time = time.time()

    return {'list': int_list, 'time': finish_time - start_time}


def insertion_sort(int_list: list):
    """
    This function implements 'Insertion Sort' algorithm.

    :param list int_list: list to sort
    :return: sorted list and execution time
    """
    int_list = list(int_list)

    start_time = time.time()

    sorted_length = 1
    counter = [0, 1]

    while counter[1] < len(int_list):

        counter[0] = sorted_length

        while counter[0] > 0:
            if int_list[counter[0]] < int_list[counter[0] - 1]:
                int_list[counter[0]], int_list[counter[0] - 1] = int_list[counter[0] - 1], int_list[counter[0]]
                counter[0] -= 1
            else:
                break

        sorted_length += 1
        counter[1] += 1

    finish_time = time.time()

    return {'list': int_list, 'time': finish_time - start_time}


print(f'Have this list:\n {num_list} \nStart tests...\n' + '===' * 30)

print('\nBubble Sort:')
print('Test success!' if sort_test(num_list, bubble_sort(num_list)['list']) else "Test failed!")

print('\nQuick Sort:')
print('Test success!' if sort_test(num_list, quick_sort(num_list)['list']) else "Test failed!")

print('\nMerge Sort:')
print('Test success!' if sort_test(num_list, merge_sort(num_list)['list']) else "Test failed!")

print('\nSelection Sort:')
print('Test success!' if sort_test(num_list, selection_sort(num_list)['list']) else "Test failed!")

print('\nInsertion Sort:')
print('Test success!' if sort_test(num_list, insertion_sort(num_list)['list']) else "Test failed!")
