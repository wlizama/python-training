ARRAY = [5, 3, 9, 1, 4, 13, 18, 10, 6, 15, 20, 19, 18, 11, 12]


def insercionSort(arr):
    idx_ini_iter = 1
    idx_end_iter = len(arr)
    for idx_iter in range(idx_ini_iter, idx_end_iter):
        for idx_revs in reversed(range(idx_iter)):
            if arr[idx_iter] < arr[idx_revs]:
                arr[idx_revs] = arr[idx_iter]
    
    return arr


def main():
    
    print("Array original:", ARRAY)
    print("Longitud:", len(ARRAY))
    print("Max. Index:", len(ARRAY) - 1)

    arr_sorted = insercionSort(ARRAY)
    print("Sorted:", arr_sorted)


if __name__ == '__main__':
    main()
    