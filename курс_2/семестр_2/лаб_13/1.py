def create_sentence(numbers_str, words_str):

  numbers = [int(x) for x in numbers_str.split()]
  words = words_str.split()
  sentence = ' '.join([words[i - 1] for i in numbers])
  return sentence.capitalize()

numbers_str = "1 3 2"
words_str = "Это просто тест строки"
new_sentence = create_sentence(numbers_str, words_str)
print(new_sentence)