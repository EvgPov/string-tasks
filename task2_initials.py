def initials(full_name: str) -> str:
    words = full_name.split()
    return "".join(f"{word[0].upper()}." for word in words)


if __name__ == "__main__":
    person_full_name = input("Введите ФИО: ")
    print(f"Инициалы: {initials(person_full_name)}")
