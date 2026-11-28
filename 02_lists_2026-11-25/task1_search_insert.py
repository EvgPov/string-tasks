def search_insert(array: list[int], number: int) -> int:
    for index in range(len(array)):
        if array[index] >= number:
            return index
    return len(array)

if __name__ == "__main__":
    examples = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ]

    for items, value, expected in examples:
        result =  search_insert(items, value)
        status = "OK" if result == expected else "ОШИБКА"
        print(f"Список: {items}, число: {value} → {result} (ожидалось {expected}) {status}")
