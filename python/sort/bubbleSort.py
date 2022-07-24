def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        # check if the elements are already sorted
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 32, 34, 10]

    bubble_sort(elements)
    print(elements)
