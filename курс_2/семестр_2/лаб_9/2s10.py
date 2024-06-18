word = input("Введите слово: ")

is_identifier = True

# Проверка первого символа
if not (word[0].isalpha() or word[0] == '_'):
    is_identifier = False

# Проверка остальных символов
for char in word[1:]:
    if not (char.isalnum() or char == '_'):
        is_identifier = False
        break  # Прерываем цикл, если найден некорректный символ

if is_identifier:
    print("Слово является идентификатором")
else:
    print("Слово не является идентификатором")
