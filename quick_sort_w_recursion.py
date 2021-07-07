''' ------QUICK SORT RECURISVELY------
    In this program we demonstrate how to use Quick Sort recursively.
    Quick Sort is a divide and conquer algorithm. In this the heavy lifting is
    done during the divide operation
'''

import random

data = random.sample(range(0,100), 10)

def quick_sort(data):
    if len(data) < 2:
        return data
    pivot = random.choice(data)
    left_data = [x for x in data if x < pivot]
    right_data = [y for y in data if y > pivot]
    return (quick_sort(left_data) + [pivot] + quick_sort(right_data))
print('\n')
print("Array before sorting is {}".format(data))
print("\n")
print("Array after sorting is {}".format(quick_sort(data)))
print("\n")