

def partition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            # if i!= j:
            #   print(A)
    A[i + 1], A[high] = A[high], A[i + 1]
    # if i+1 != high:
    # print(A)
    return i + 1


def quick_sort(A, low, high):
    if low < high:
        m = partition(A, low, high)
        # print('m = ',m)
        quick_sort(A, low, m - 1)
        quick_sort(A, m + 1, high)
