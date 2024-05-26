def bubble_sort(arr: list, size: int) -> list:
    """Bubble sort
    
    Args:
        arr (list): unsorted list

    Returns:
        list: sorted list
        
    Results:
        lists size in test is 10000, max abs value of element in list is 1000
        list type: random, time taken: 2.2590579986572266
        list type: sorted, time taken: 1.1731250286102295
        list type: reversed_sorted, time taken: 2.562087059020996
        list type: almost_sorted, time taken: 1.2984519004821777
    """
    n = size
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
