import random

def find_local_minimum(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if (mid == 0 or arr[mid] < arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] < arr[mid + 1]):
            return arr[mid]

        if mid > 0 and arr[mid - 1] < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return None

def brute_force_find_local_minimum(arr):
    for i in range(len(arr)):
        if i == 0 and arr[i] < arr[i + 1]:
            return arr[i]
        elif i == len(arr) - 1 and arr[i] < arr[i - 1]:
            return arr[i]
        elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            return arr[i]

    return None

# Test the algorithm using the comparator
def test_find_local_minimum():
    # Generate random test cases
    for _ in range(10):
        length = random.randint(1, 20)
        arr = random.sample(range(1, 100), length)
        arr.sort()

        # Add a local minimum at a random position
        local_min_index = random.randint(1, length - 2)
        local_min_value = random.randint(arr[local_min_index - 1] + 1, arr[local_min_index + 1] - 1)
        arr[local_min_index] = local_min_value

        # Test the algorithm against the brute-force approach
        result1 = find_local_minimum(arr)
        result2 = brute_force_find_local_minimum(arr)

        # Compare the results
        if result1 != result2:
            print("Test failed")
            print("Array:", arr)
            print("Algorithm result:", result1)
            print("Brute-force result:", result2)
            return

    print("All tests passed!")

# Run the tests
test_find_local_minimum()
