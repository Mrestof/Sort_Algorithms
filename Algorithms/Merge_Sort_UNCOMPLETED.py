file = open('nums.txt', 'r')
file_list = file.read().split(':')
file.close()

num_list = []

for i in file_list:
    num_list.append(int(i))

print('Have the list:\n' + str(num_list) + '\n==============================')


def merge_sort(l):
    if len(l) == 1:
        return l[0]
    r = len(l)
    m = (0 + r) // 2
    list1 = l[:m]
    list2 = l[m:]

    merge_sort(list1)
    merge_sort(list2)

    print('==============================================')
    print(list1)
    print(list2)


merge_sort(num_list)

# CAN NOT UNDERSTAND RECURSION!(
