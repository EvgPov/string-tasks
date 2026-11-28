MONTHS = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]


def day_month(date: str) -> str:
    _, month, day = date.split("-")
    return f"{int(day)} {MONTHS[int(month) - 1]}"


if __name__ == "__main__":
    user_date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    print(f"День месяца: {day_month(user_date)}")
