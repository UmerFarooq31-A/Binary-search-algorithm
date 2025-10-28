# Binary Search Program (Improved Version)

def binary_search(arr, target):
    """
    Performs binary search on a sorted list `arr` to find `target`.
    Returns the index if found, otherwise returns -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # use integer division
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Main program
numbers = [20, 30, 40, 50, 60, 70, 80, 90, 100]

try:
    search_value = int(input("Enter a number to search for: "))
    result = binary_search(numbers, search_value)

    if result != -1:
        print(f"✅ Found {search_value} at index {result}.")
    else:
        print("❌ Not found in the list.")
except ValueError:
    print("⚠️ Please enter a valid integer.")
