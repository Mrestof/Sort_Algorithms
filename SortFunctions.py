import time


class Sort:

    def __init__(self, arr: list):
        """
        This class contain sort functions

        :param list arr: list to sort
        """
        self.arr = arr

    def bubble_sort(self):
        """
        This function implements 'Bubble Sort' algorithm.

        :return: sorted list and execution time
        """
        int_list = list(self.arr)

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

    def quick_sort(self):
        """
        This function implements 'Quick Sort' algorithm.

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
        int_list = list(self.arr)

        start_time = time.time()
        sorted_list = q_s(int_list)
        finish_time = time.time()

        return {'list': sorted_list, 'time': finish_time - start_time}

    def merge_sort(self):
        """
        This function is in development

        :return: sorted list and execution time
        """
        int_list = list(self.arr)

        return {'list': int_list, 'time': 0}

    def selection_sort(self):
        """
        This function implements 'Selection Sort' algorithm.

        :return: sorted list and execution time
        """
        int_list = list(self.arr)

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

    def insertion_sort(self):
        """
        This function implements 'Insertion Sort' algorithm.

        :return: sorted list and execution time
        """
        int_list = list(self.arr)

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

    def heap_sort(self):
        """
        This function implements 'Heap Sort' algorithm.

        :return: sorted list and execution time
        """
        int_list = list(self.arr)

        start_time = time.time()

        num_heap = [int_list[0]]
        counter = [1, 1]

        while counter[1] < len(int_list):

            num_heap.append(int_list[counter[0]])
            current_pos = len(num_heap) - 1
            parent_pos = int((current_pos + current_pos % 2 - 2) / 2)

            while current_pos != 0 and num_heap[current_pos] < num_heap[parent_pos]:

                num_heap[current_pos], num_heap[parent_pos] = num_heap[parent_pos], num_heap[current_pos]
                current_pos = parent_pos

                parent_pos = int((current_pos + current_pos % 2 - 2) / 2)

            counter[0] += 1
            counter[1] += 1

        final_list = []

        while len(num_heap) != 0:

            num_heap[0], num_heap[len(num_heap) - 1] = num_heap[len(num_heap) - 1], num_heap[0]
            final_list.append(num_heap[len(num_heap) - 1])
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

        finish_time = time.time()

        return {'list': final_list, 'time': finish_time - start_time}

    def builtin_sort(self):
        """
        This function sort list with builtin method

        :return: sorted list
        """
        int_list = list(self.arr)

        start_time = time.time()
        int_list.sort()
        finish_time = time.time()

        return {'list': int_list, 'time': finish_time - start_time}
