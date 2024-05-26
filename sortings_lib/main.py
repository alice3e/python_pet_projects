import sorts
import testing_lib as tl


if __name__ == "__main__":
    # Example usage:
    times = tl.benchmark_all_list_types(sorted, size=1000000, max_abs_value=1000, negative_values=True,seed=42)
    list_types = ["random", "sorted", "reversed_sorted", "almost_sorted"]
    for i in range(len(list_types)):
        print(f'list type: {list_types[i]}, time taken: {times[i]}')