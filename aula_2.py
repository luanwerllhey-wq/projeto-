def insertion_sort(arr):
    for i in range(1, len(arr)):          # Passo 1
        key = arr[i]                     # Passo 2
        j = i - 1                       # Passo 3

        while j >= 0 and arr[j] > key:  # Passo 4
            arr[j + 1] = arr[j]         # Passo 5
            j -= 1                      # Passo 6

        arr[j + 1] = key                # Passo 7
