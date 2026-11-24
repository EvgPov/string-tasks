def reverse_vowels(line: str) -> str:
    vowels = "aeiouyAEIOUY"
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

text = input("Введите строку: ")
print(reverse_vowels(text))
