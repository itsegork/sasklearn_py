n = int(input())
phonebook = {}

for _ in range(n):
  name, number = input().split()
  phonebook[name] = number

query = input()

if query in phonebook:
  print(phonebook[query])
else:
  print("Нет в телефонной книге")