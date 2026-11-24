def min_sum(number: int) -> int:
    if not 1000 <= number <= 9999:
        raise ValueError("Число должно быть в интервале [1000; 9999]")

    d = sorted(str(number))
    first_number = int(d[0] + d[2])
    second_number = int(d[1] + d[3])
    return  first_number + second_number


if __name__ == "__main__":
    user_number = input("Введите число в интервале [1000; 9999]: ")
    if not user_number.isdigit():
        print("Ошибка: нужно ввести целое число")
    else:
        try:
            print(f"Минимально возможная сумма пар цифр: {min_sum(int(user_number))}")
        except ValueError as error:
            print(f"Ошибка: {error}")
