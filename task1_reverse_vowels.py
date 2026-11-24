def reverse_vowels(line: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""
    vowels_list = []
    for char in line:
        if char in vowels:
            vowels_list.append(char)

    for index in range(len(line)):
        if line[index] in vowels:
            result += vowels_list.pop()
        else:
            result += line[index]
    return result

if __name__ == "__main__":
    text = input("Введите строку: ")
    print(f"Результат: {reverse_vowels(text)}")
