import random


def selection_sort(array):
    print('SELECTION SORT\nInitial array:\n', array)

    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]

    print('Sorted array:\n', array)
    return array


if __name__ == "__main__":
    array = [random.randint(1, 100) for _ in range(20)]
    selection_sort(array)
