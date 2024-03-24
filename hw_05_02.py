def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    if upper_bound is None:
        return iterations, None  # Target is greater than any array element
    else:
        return iterations, upper_bound

sorted_array = [1.2, 2.3, 3.4, 5.5, 8.8, 11.11, 13.13, 17.17, 19.19, 21.21]
target_value = 20.1

iterations, upper_bound = binary_search_with_upper_bound(sorted_array, target_value)

if upper_bound is not None:
    print(f"Елемент {target_value} знайдено за {iterations} ітерацій. Верхня межа: {upper_bound}")
else:
    print(f"Елемент {target_value} не знайдено у масиві за {iterations} ітерацій.")