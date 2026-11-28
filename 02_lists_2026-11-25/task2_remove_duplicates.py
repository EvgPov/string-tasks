def remove_duplicates(array: list[int]) -> tuple[int, list[int]]:
    modify_array = []
    count = 0
    for i in range(len(array)):
        if i == 0 or array[i] != array[i - 1]:
            modify_array.append(array[i])
            count += 1

    for i in range(len(array) - count):
        modify_array.append(None)

    return count, modify_array

if __name__ == "__main__":
    examples = [
        ([1, 1, 2], 2, [1, 2, None]),
        ([0, 0, 1, 1, 2, 2, 3], 4, [0, 1, 2, 3, None, None, None]),
    ]

    for items, expected_count, expected_array in examples:
        count, result = remove_duplicates(items)
        status = "OK" if (count, result) == (expected_count, expected_array) else "ОШИБКА"
        print(f"Список: {items}")
        print(f"  Уникальных: {count} (ожидалось {expected_count})")
        print(f"  Результат:  {result} (ожидалось {expected_array}) {status}")
