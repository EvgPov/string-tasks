def search_first_last_index(array: list[int], number: int) -> list[int]:
    if number not in array:
        return [-1, -1]

    first_index = array.index(number)
    last_index = first_index + array.count(number) - 1

    return [first_index, last_index]

if __name__ == "__main__":
    examples = [
        ([5, 7, 7, 8, 8, 8, 8, 10], 8, [3, 6]),
        ([5, 7, 7, 8, 8, 8, 8, 10], 3, [-1, -1]),
        ([], 5, [-1, -1]),
    ]

    for array, number, expected in examples:
        result = search_first_last_index(array, number)
        status = "OK" if result == expected else "ОШИБКА"
        print(f"Список: {array}, число: {number} → {result} (ожидалось {expected}) {status}")
