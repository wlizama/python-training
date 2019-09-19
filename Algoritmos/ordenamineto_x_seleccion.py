ARRAY = [48, 84, 2, 12, 54, 62, 32, 44, 1, 78, 65, 15, 27, 81, 76, 62, 15]

def getNewMinIndex(arr, min_index):
    new_min_idx = min_index
    max_idx = len(arr)
    for idx in range(min_index, max_idx): # range ya genera hasta max_idx -1
        if arr[min_index] < arr[idx]:
            new_min_idx = idx
    
    return new_min_idx


def main():
    # print(ARRAY[0], len(ARRAY))
    # for val in ARRAY:
    #     print(val)
    print(getNewMinIndex(ARRAY, 0))

    


if __name__ == "__main__":
    main()