from telebot import types
from database import bot, cursor, allowed_users, conn

def medicine_menu(message):
    if message.from_user.username in allowed_users:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Список лекарств"),
            types.KeyboardButton(text="Новое лекарство"),
            types.KeyboardButton(text="Уменьшить количество лекарства"),
            types.KeyboardButton(text="Увеличить количество лекарства"),
            types.KeyboardButton(text="Посоветовать лекарство"),
            types.KeyboardButton(text="Поддержка"),
            types.KeyboardButton(text="Назад в основное меню"),
        )
        cursor.execute('SELECT url FROM pic WHERE title = ?', "medicine")
        photo_url = cursor.fetchone()[0]  # url картинки
        bot.send_photo(message.chat.id, photo=photo_url, caption="Вы находитесь в разделе 'Аптечка'\n" "Чем я могу Вам помочь?", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")




# запрос в базу данных для получения списка лекарств
def medicine_list(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(
        types.KeyboardButton(text="Назад в основное меню"),
    )
    cursor.execute("SELECT * FROM medicine")
    drugs_data = cursor.fetchall()
    if drugs_data:
        response = "Аптечка:\n"
        for row in drugs_data:
            response += (
                f"Препарат: {row[1]}\nКоличество: {row[2]}\nНазначение: {row[3]}\n\n"
            )
        bot.send_message(message.chat.id, response, reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Нет информации о лекарствах")