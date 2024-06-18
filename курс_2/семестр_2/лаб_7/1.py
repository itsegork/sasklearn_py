table = []
for i in range(1, 10):
    row = []
    for j in range(1, 10):
        row.append(i * j)
    table.append(row)
for row in table:
    print(*row)