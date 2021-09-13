import random


def bubble_sort(array):
    print('BUBBLE SORT\nInitial array:\n', array)

    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print('Sorted array:\n', array)
    return array


if __name__ == "__main__":
    array = [random.randint(1, 100) for _ in range(20)]
    bubble_sort(array)
