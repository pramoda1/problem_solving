def contains_duplicate(arr):
    n = len(arr)
    for i in range(n):  
        for j in range(i + 1, n):  # Compare each element with all others
            if arr[i] == arr[j]:  # If a duplicate is found
                return True  # Return True immediately
    return False  # No duplicates found

# Example Test Cases
print(contains_duplicate([1, 2, 3, 1]))  # Expected Output: True
print(contains_duplicate([1, 2, 3, 4]))  # Expected Output: False
print(contains_duplicate([7, 7, 7, 7]))  # Expected Output: True
print(contains_duplicate([]))  # Expected Output: False
