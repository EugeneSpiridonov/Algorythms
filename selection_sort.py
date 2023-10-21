def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Начинаем с предположения, что первый элемент в подмассиве - минимальный
        min_index = i
        
        # Поиск минимального элемента в оставшейся части списка
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Обмен минимального элемента с элементом на текущей позиции
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Пример использования
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Отсортированный массив:", arr)