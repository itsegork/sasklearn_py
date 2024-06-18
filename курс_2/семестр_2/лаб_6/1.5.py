U = 40
total_pages = U

for i in range(2, 11):
    daily_pages = U * (1 + 0.05 * (i - 1))
    total_pages += daily_pages

print(f"Общее количество страниц в книге: {total_pages} страниц.")