word = input("Введите слово: ")

letter_counts = {}
for letter in word:
  if letter in letter_counts:
    letter_counts[letter] += 1
  else:
    letter_counts[letter] = 1

print(letter_counts)