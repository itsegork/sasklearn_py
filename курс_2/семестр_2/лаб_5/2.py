pages_per_day = 40  # количество страниц, прочитанных в первый день
days = 10  # количество дней за которое студент прочитал книгу
total_pages = 0
day = 1
while day <= days:
    total_pages += pages_per_day
    pages_per_day *= 1.05  # увеличение дневной нормы на 5%
    day += 1

print("Количество страниц в книге:", total_pages)
