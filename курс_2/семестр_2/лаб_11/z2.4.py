x = [int(input()) for _ in range(15)]

max_element = x[0]
max_index = 0
for i in range(1, len(x)):
    if x[i] > max_element:
        max_element = x[i]
        max_index = i

print("Наибольший элемент:", max_element)
print("Порядковый номер наибольшего элемента:", max_index + 1)