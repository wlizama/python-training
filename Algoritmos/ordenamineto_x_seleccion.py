ARRAY = [48, 84, 2, 12, 54, 62, 32, 44, 1, 78, 65, 15, 27, 81, 76, 62, 15]

def getNewMinIndex(arr, idx_min, idx_last_minor_found):
    new_min_idx = idx_last_minor_found
    max_idx = len(arr)
    for idx in range(idx_last_minor_found + 1, max_idx): # range ya genera hasta max_idx -1
        if arr[idx] < arr[idx_min]:
            new_min_idx = idx
            break
    
    return new_min_idx


def swapArray(arr, idx_ant, idx_new):
    val_ant = arr[idx_ant]
    arr[idx_ant] = arr[idx_new]
    arr[idx_new] = val_ant
    return arr


def selectionSort(arr):
    idx_ini = 0
    max_idx = len(arr)
    idx_min = 0
    for idx_iter in range(idx_ini, max_idx):
        # idx_last_minor_found = idx_iter
        # idx_last_minor_found_new = getNewMinIndex(arr, idx_iter, idx_last_minor_found)
        # swapped_arr = swapArray(arr, idx_ant, idx_last_minor_found)
        # for idx in range(idx_iter + 1, max_idx): # range ya genera hasta max_idx -1
        
        if arr[idx_iter] < arr[idx_min]:
            idx_min = idx_iter
            print(idx_min)

   
    
    # print(idx_last_minor_found, swapped_arr)

def main():
    # print(ARRAY[0], len(ARRAY))
    # for val in ARRAY:
    #     print(val)
    print("Array original:", ARRAY)
    print("Longitud:", len(ARRAY))
    print("Max. Index:", len(ARRAY) - 1)

    selectionSort(ARRAY)


if __name__ == "__main__":
    main()

"""
tener 3 variables
    indice_donde_se_encontro_el_ultimo_menor        : indice marcador de ubicacion de ultimo menor ubicado en recorrido
    indice_del_numero_menor                         : indice de numero menor ubicado despues del ultimo menor
    indice_de_recorrido_hasta_final_longitud_array  : aumenta en 1 hasta longitud de array
"""