def is_sorted_brute_force(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                return False
    return True

t = [1, 3, 2, 4]
a = is_sorted_brute_force(t)
print(a)