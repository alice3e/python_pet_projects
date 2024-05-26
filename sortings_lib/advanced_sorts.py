import random

import random

def quick_sort(arr: list, size : int) -> list:
    """Quick sort using list comprehension

    Args:
        arr (list): unsorted list
        size (int): size of a list

    Returns:
        list: sorted_list
    
    Result:
        lists size in test is 10000, max abs value of element in list is 1000
        list type: random, time taken: 0.010195255279541016
        list type: sorted, time taken: 0.009316682815551758
        list type: reversed_sorted, time taken: 0.0092620849609375
        list type: almost_sorted, time taken: 0.00958108901977539
    """
    if size <= 1:
        return arr
    else:
        pivot_index = random.randint(0, size - 1)  # Random pivot selection
        pivot = arr[pivot_index]
        less = [x for x in arr[:pivot_index] + arr[pivot_index + 1:] if x < pivot]
        greater = [x for x in arr[:pivot_index] + arr[pivot_index + 1:] if x > pivot]
        equal = [x for x in arr if x == pivot]
        return quick_sort(less, size=len(less)) + equal + quick_sort(greater, size=len(greater))