y = [int(input()) for _ in range(15)]

min_element = y[0]
min_index = 0
for i in range(1, len(y)):
    if y[i] < min_element:
        min_element = y[i]
        min_index = i

print("Наименьший элемент:", min_element)
print("Порядковый номер наименьшего элемента:", min_index + 1)