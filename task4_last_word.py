def last_word_length(line: str) -> int:
    PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    words = line.split()
    return len(words[-1].strip(PUNCTUATION)) if words else 0


if __name__ == "__main__":
    user_line = input("Введите строку: ")
    print(f"Длина последнего слова: {last_word_length(user_line)}")
