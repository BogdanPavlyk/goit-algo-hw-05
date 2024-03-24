def binary_search(arr, target):
    iterations = 0
    low, high = 0, len(arr) - 1
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        iterations += 1

        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            upper_bound = mid_value
            high = mid - 1
        else:
            upper_bound = mid_value
            break

    return iterations, upper_bound

sorted_array = [1.2, 2.3, 3.4, 5.5, 8.8, 11.11, 13.13, 17.17, 19.19, 21.21]
target_value = 20.1

iterations, upper_bound = binary_search(sorted_array, target_value)

if upper_bound is not None:
    print(f"Елемент {target_value} знайдено за {iterations} ітерацій. Верхня межа: {upper_bound}")
else:
    print(f"Елемент {target_value} не знайдено у масиві за {iterations} ітерацій.")