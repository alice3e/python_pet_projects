import random
import matplotlib.pyplot as plt
import time
def generate_random_list(size=10,max_abs_value=20,negative_values=True,type="random",seed: int=42) -> list:
    """generates list with random values
    
    Args:
        size (int, optional): size of a list. Defaults to 10.
        max_abs_value (int, optional): maximum value of an element in list. Defaults to 20.
        negative_values (bool, optional): True - some values can be negative, False - only positive values. Defaults to True.
        type (str, optional): types: random, reversed_sorted, sorted, almost_sorted. Defaults to "random".
    """
    if(max_abs_value <= 0): raise Exception("wrong max_abs_value in generate_random_list")
    if(size < 0): raise Exception("wrong size in generate_random_list")
    random.seed(seed)
    
    if(negative_values):
        out = [random.randint(-1*max_abs_value, max_abs_value) for _ in range(size)]
    else:
        out = [random.randint(0, max_abs_value) for _ in range(size)]
    
    if type=="random":
        return out
    elif type=="sorted":
        out.sort()
        return out
    elif type=="reversed_sorted":
        out.sort()
        out.reverse()
        return out
    elif type=="almost_sorted":
        out.sort()
        k = 0.05
        n_mix = round(size * k)
        for i in range(n_mix):
            ind_1 ,ind_2 = random.randint(0, size-1), random.randint(0, size-1)
            out[ind_1], out[ind_2] = out[ind_2], out[ind_1]
        return out
    else:
        raise Exception("wrong type in generate_random_list")
    

def benchmark_all_list_types(sorting_function, size, max_abs_value, negative_values, seed):
    """Benchmarks the given sorting function on different list types,
    raising an exception if the output is not truly sorted.

    Args:
        sorting_function (function): The sorting function to benchmark (e.g., sorted, list.sort).
        size (int): The desired size of the lists.
        max_abs_value (int): The maximum absolute value of elements in the lists.
        negative_values (bool): Whether to include negative values in the lists.
        seed (int): Seed for random number generation.

    Returns:
        list: A list of times (in seconds) taken to sort each list type.
    """
    times = []
    for list_type in ["random", "sorted", "reversed_sorted", "almost_sorted"]:
        start_time = time.time()
        input_list = generate_random_list(size, max_abs_value, negative_values, type=list_type, seed=seed)
        # Make a copy of the input list
        test_list = input_list.copy()
        sorting_function(test_list)
        end_time = time.time()
        times.append(end_time - start_time)

        # Check if the list is truly sorted
        if not all(test_list[i] <= test_list[i + 1] for i in range(len(test_list) - 1)):
            raise Exception(f"Sorting function failed to sort correctly for list type: {list_type}")

    return times

