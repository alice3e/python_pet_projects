import basic_sorts as bs
import advanced_sorts as ad_s
import testing_lib as tl


if __name__ == "__main__":
    # sorting_function signature: def some_sort(arr: list, size: int) -> list:
    # Example usage:
    sz = 10000
    max_abs = 1000
    times = tl.benchmark_all_list_types(ad_s.quick_sort, size=sz, max_abs_value=max_abs, negative_values=True,seed=42)
    list_types = ["random", "sorted", "reversed_sorted", "almost_sorted"]
    print(f'lists size in test is {sz}, max abs value of element in list is {max_abs}')
    for i in range(len(list_types)):
        print(f'list type: {list_types[i]}, time taken: {times[i]}')