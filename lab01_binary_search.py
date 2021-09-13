import random
from lab01_selection_sort import selection_sort


def binary_search(array, value):
    print(f'Searching for {value} in', array)

    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((high + low) / 2)
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
        else:
            return mid
    return 'hello'


if __name__ == "__main__":
    N = 10
    array = [random.randint(1, 100) for _ in range(N)]
    array = selection_sort(array)  # Sorting array w/ selection sort from prev task
    print('---')
    value = array[random.randint(0, N - 1)]
    index = binary_search(array, value)
    print(f'{value} is present at index {index} in {array}')
