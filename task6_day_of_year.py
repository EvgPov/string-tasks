from datetime import date


def day_of_year(date_str: str) -> int:
    end_date = date.fromisoformat(date_str)
    start_date = date(end_date.year, 1, 1)
    return (end_date - start_date).days + 1


if __name__ == "__main__":
    user_date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    try:
        print(f"Дней с начала {user_date[:4]} года: {day_of_year(user_date)}")
    except ValueError:
        print("Неверный формат даты. Пример: 2020-01-05")
