import random

nums = []
length = int(input('How long should the list be: '))
lim_min = int(input('Enter down limit of available nums: '))
lim_max = int(input('Enter up limit of available nums: '))

for i in range(length):
    nums.append(str(random.randint(lim_min, lim_max)))

nums_string = ':'.join(nums)

file = open('Algorithms/nums.txt', 'w')
file.write(nums_string)
file.close()

file = open('nums.txt', 'w')
file.write(nums_string)
file.close()

file = open('Algorithms/nums.txt', 'r')
print('File nums.txt now contain this:\n' + file.read())
file.close()
