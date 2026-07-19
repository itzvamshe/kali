def binary_search(numbers, target):

    start = 0                    # First index
    end = len(numbers) - 1        # Last index

    while start <= end:

        middle = (start + end) // 2

        if numbers[middle] == target:
            return middle         # Target found

        elif numbers[middle] < target:
            start = middle + 1    # Search the right half

        else:
            end = middle - 1      # Search the left half

    return -1                     # Target not found


# Example
numbers = [2, 3, 4, 10, 40]
target = int(input('enter the number: '))

answer = binary_search(numbers, target)

if answer == -1:
    print("Number not found")
else:
    print("Number found at index", answer)

