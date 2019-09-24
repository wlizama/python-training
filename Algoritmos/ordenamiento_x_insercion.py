ARRAY = [5, 3, 9, 1, 4, 13, 18, 10, 6, 15, 20, 19, 18, 11, 12]


def insertionSort(arr):
    for i in range(1, len(arr)):
        # elemento a comprar
        current = arr[i]

        # comparar el elemento actual con la parte ordenada e intercambiar
        while i > 0 and arr[i-1] > current:
            arr[i] = arr[i-1]
            i = i-1
            arr[i] = current

    return arr


def main():
    
    print("Array original:", ARRAY)
    print("Longitud:", len(ARRAY))
    print("Max. Index:", len(ARRAY) - 1)

    arr_sorted = insertionSort(ARRAY)
    print("Sorted:", arr_sorted)


if __name__ == '__main__':
    main()
    