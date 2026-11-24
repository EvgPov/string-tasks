def find_target (line: str, target_value: str) -> int:
    targets = set(target_value)
    count = 0
    for char in line:
        if char in targets:
            count += 1
    return count


if __name__ == "__main__":
    user_line = input("Введите строку: ")
    user_target_value = input("Введите целевую последовательность символов: ")
    print(f"Количество вхождений: {find_target(user_line, user_target_value)}")
