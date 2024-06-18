rubles = int(input("Рубли: "))
kopeiki = int(input("Копейки: "))
quantity = int(input("Сколько пирожков: "))

total_rubles = rubles * quantity
total_kopeiki = kopeiki * quantity

if total_kopeiki >= 100:
    total_rubles += total_kopeiki // 100
    total_kopeiki %= 100

print(f"К оплате: {total_rubles} руб. {total_kopeiki} коп.")