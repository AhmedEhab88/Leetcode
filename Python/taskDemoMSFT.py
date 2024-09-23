def smallest_missing_positive_integer(A):
    n = len(A)

    print("Original Array:", A)

    # Mark negative and out-of-range elements as n+1
    for i in range(n):
        if A[i] <= 0 or A[i] > n:
            A[i] = n + 1
    print("After Marking Negative/Out-of-Range:", A)

    # Place each element at its correct position (if possible)
    for i in range(n):
        while 1 <= A[i] <= n and A[A[i] - 1] != A[i]:
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
            print("Array after swapping:", A)

    # Find the first index where the element is not in its correct position
    for i in range(n):
        if A[i] != i + 1:
            return i + 1

    # If all elements are in their correct positions, return n+1
    return n + 1


# Example usage:
A = [3, 4, -1, 1]

result = smallest_missing_positive_integer(A)
print("Smallest Missing Positive Integer:", result)
