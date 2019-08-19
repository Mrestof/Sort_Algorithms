from random import randint as rint

file = open('nums.txt', 'r')
file_list = file.read().split(':')
file.close()

num_list = []

for i in file_list:
    num_list.append(int(i))

print('Have this list: \n' + str(num_list) + '\nStart sorting...')


def quick_sort(l: list):
    if len(l) <= 1:
        return l

    bp = rint(0, len(l) - 1)
    l[bp], l[-1] = l[-1], l[bp]
    print(f'Swap last and "{bp}" elements\n{l}')
    bp = -1

    lp = 0
    rp = len(l) - 1 if bp != len(l) - 1 else bp - 1

    print('b_point: ' + str(bp) + '\nl_point: ' + str(lp) + '\nr_point: ' + str(rp))

    while 1:
        while l[lp] < l[bp] and lp < len(l) - 1:
            lp += 1

        while l[rp] >= l[bp] and rp > lp:
            rp -= 1

        if rp == lp:
            sorted_pointer = lp
            print('s_point ' + str(sorted_pointer))
            l[bp], l[rp] = l[rp], l[bp]
            break

        print('changing r_point and l_point')
        l[rp], l[lp] = l[lp], l[rp]

    l1 = l[:sorted_pointer]
    l2 = l[sorted_pointer:]

    return quick_sort(l1) + quick_sort(l2)


def sort_test(original_list: list, sorted_list: list):
    print('=' * len(str(num_list)))
    list1 = list(original_list)
    list1.sort()
    if list1 == sorted_list:
        print("Test success!")
    else:
        print("Test failed! :(")


sort_test(num_list, quick_sort(num_list))

print(quick_sort(num_list))
