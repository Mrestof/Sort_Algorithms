import SortFunctions as SFunc

file = open('nums.txt', 'r')
file_list = file.read().split(':')
file.close()

num_list = []

for i in file_list:
    num_list.append(int(i))


def test_sort_functions(functions: list):

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

    print(f'Have this list:\n {num_list} \n' + '===' * 30 + '\nStart tests...\n' + '===' * 30)

    for func in functions:
        sort_result = func()
        print(f'\n{func.__name__}:')
        print(f'Sorted in {round(sort_result["time"], 8)} seconds\n' +
              'Test success!' if sort_test(num_list, sort_result['list']) else "Test failed!")

    print('\nAll tests completed')


sorter = SFunc.Sort(num_list)

functions_to_test = [sorter.bubble_sort, sorter.selection_sort, sorter.insertion_sort,
                     sorter.heap_sort, sorter.merge_sort, sorter.quick_sort, sorter.builtin_sort]

test_sort_functions(functions_to_test)
