ARRAY = [48, 84, 2, 12, 54, 10, 32, 44, 1, 78, 65, 8, 27, 81, 76, 62, 15]

def swapArray(arr, idx_ant, idx_new):
    val_ant = arr[idx_ant]
    arr[idx_ant] = arr[idx_new]
    arr[idx_new] = val_ant
    return arr


def selectionSort(arr):
    idx_ini = 0
    max_idx = len(arr)
    for idx_pos_sort in range(idx_ini, max_idx):
        idx_min = idx_pos_sort
        for idx_iter in range(idx_pos_sort + 1 , max_idx):
            if arr[idx_iter] < arr[idx_min]:
                idx_min = idx_iter

        arr = swapArray(arr, idx_pos_sort, idx_min)
        print(arr)
    
    return arr

def main():
    
    print("Array original:", ARRAY)
    print("Longitud:", len(ARRAY))
    print("Max. Index:", len(ARRAY) - 1)

    arr_sorted = selectionSort(ARRAY)
    print("Sorted:", arr_sorted)


if __name__ == "__main__":
    main()
