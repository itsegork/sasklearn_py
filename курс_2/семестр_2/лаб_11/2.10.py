grades = [int(input()) for _ in range(25)]

fail_count = 0
for grade in grades:
    if grade == 2:
        fail_count += 1

print("Количество человек, не допущенных ко второму экзамену:", fail_count)