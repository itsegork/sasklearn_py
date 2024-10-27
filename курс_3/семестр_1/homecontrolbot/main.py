from telebot import telebot, types
from medicine import medicine_menu, medicine_list
import os
from mimetypes import guess_extension
import time
from docx import Document
from database import bot, cursor, conn
from func import menu, allowed


# добавление кнопок для выбора пункта меню
@bot.message_handler(
    func=lambda message: message.text == "Назад в основное меню"
    or message.text == "/start"
)
def start_message(message):
    if allowed(message):
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Аптечка"),
            types.KeyboardButton(text="Список покупок"),
            types.KeyboardButton(text="Факс"),
            types.KeyboardButton(text="Поддержка"),
            types.KeyboardButton(text="Печать (stable release - HomeBot 4)")
        )
        cursor.execute('SELECT url FROM pic WHERE title = ?', "menu")
        photo_url = cursor.fetchone()[0]  # url картинки
        bot.send_photo(message.chat.id, photo=photo_url, caption="Привет! Я твой домашний помощник\n"
            "Я знаю, что находится в твоей аптечке и могу посоветовать препарат, исходя из симптомов\n"
            "Не забуду о предстоящих покупках\n"
            "Управлять мной можно кнопками ниже", reply_markup=keyboard)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(types.KeyboardButton(text="Факс"), types.KeyboardButton(text="Поддержка"))
        bot.send_message(
            message.chat.id,
            "Привет! Тут ты можешь отправить факс\n",
            reply_markup=keyboard,
        )

# поддержка
@bot.message_handler(func=lambda message: message.text == "Поддержка")
def help_message(message):
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(types.KeyboardButton(text="Назад в основное меню"))
        response = (
            "Бот для управления домом v.0.1\n\n"
            "by @egorkurochkin with ❤️ for SASK\n\n"
        )
        cursor.execute('SELECT url FROM pic WHERE title = ?', "logo")
        photo_url = cursor.fetchone()[0]  # url картинки
        bot.send_photo(message.chat.id, photo=photo_url, caption=response, reply_markup=keyboard)


# -------------------------------АПТЕЧКА-----------------------------------#


# добавление кнопок для аптечки
@bot.message_handler(func=lambda message: message.text == "Аптечка")
def start_med(message):
    if allowed(message):
        medicine_menu(message)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")


# получение списка лекарств
@bot.message_handler(func=lambda message: message.text == "Список лекарств")
def start_medlist(message):
    if allowed(message):
        medicine_list(message)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")


# добавление нового лекарства
@bot.message_handler(func=lambda message: message.text == "Новое лекарство")
# проверка доступа
def new_medicine_access(message):
    if allowed(message):
        new_medicine_name(message)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")
# получение имени лекарства
def new_medicine_name(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(
        types.KeyboardButton(text="Назад в основное меню")
    )
    bot.send_message(message.chat.id, "Введите название лекарства:", reply_markup=keyboard)
    bot.register_next_step_handler(message, new_medicine_quant)
# получение количества лекарства
def new_medicine_quant(message):
    if menu(message):
        start_message(message)
    else:
        global name
        name = message.text
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Назад в основное меню")
        )
        bot.send_message(message.chat.id, "Введите количество лекарства:", reply_markup=keyboard)
        bot.register_next_step_handler(message, new_medicine_prescript)
# получение назначения лекарства
def new_medicine_prescript(message):
    if menu(message):
        start_message(message)
    else:
        global quantity
        quantity = message.text
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Назад в основное меню")
        )
        bot.send_message(message.chat.id, "Введите назначение лекарства:", reply_markup=keyboard)
        bot.register_next_step_handler(message, new_medicine_prescript_two)
# получение второго назначения лекарства
def new_medicine_prescript_two(message):
    if menu(message):
        start_message(message)
    else:
        global prescription
        prescription = message.text
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Назад в основное меню"),
            types.KeyboardButton(text="Пропустить")
        )
        bot.send_message(message.chat.id, "Введите второе назначение лекарства при наличии:", reply_markup=keyboard)
        bot.register_next_step_handler(message, new_medicine_commit)
# запись полученной информации в базу данных
def new_medicine_commit(message):
    if menu(message):
        start_message(message)
    else:
        try:
            global prescription2
            if message.text == "Пропустить":
                prescription2 = None
            else:
                prescription2 = message.text
            cursor.execute(
                "INSERT INTO medicine (title, quantity, prescription, prescription_two) VALUES (?, ?, ?, ?)",
                name,
                quantity,
                prescription,
                prescription2,
                    )
            conn.commit()
            bot.send_message(
                message.from_user.id,
                f"Лекарство '{name}' в количестве '{quantity}' успешно добавлено!",
                            )
            medicine_menu(message)
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")
            medicine_menu(message)


# увелчение количества лекарства
@bot.message_handler(func=lambda message: message.text == "Увеличить количество лекарства")
# проверка доступа
def add_medicine_access(message):
    if allowed(message):
        add_medicine_name(message)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")
# получение названия лекарства
def add_medicine_name(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(
        types.KeyboardButton(text="Назад в основное меню")
    )
    bot.send_message(message.chat.id, "Введите название лекарства:", reply_markup=keyboard)
    bot.register_next_step_handler(message, add_medicine_quant)
# получение количества лекарства
def add_medicine_quant(message):
    if menu(message):
        start_message(message)
    else:
        global name
        name = message.text
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Назад в основное меню")
        )
        bot.send_message(message.chat.id, "Введите число, на которое надо увеличить количество лекарства:", reply_markup=keyboard)
        bot.register_next_step_handler(message, add_medicine_commit)
# запись полученной информации в базу данных
def add_medicine_commit(message):
    if menu(message):
        start_message(message)
    else:
        try:
            global quantity
            quantity = message.text
            cursor.execute("SELECT quantity FROM medicine WHERE title=?", name)
            current_quantity = cursor.fetchone()
            if current_quantity:
                current_quantity = current_quantity[0]
                new_quantity = int(current_quantity) + int(quantity)
                cursor.execute(
                    "UPDATE medicine SET quantity=? WHERE title=?", (new_quantity, name)
                )
                conn.commit()
                bot.send_message(
                    message.from_user.id,
                    f"Лекарство '{name}' в количестве '{quantity}' успешно добавлено",
                )
                medicine_menu(message)
            else:
                bot.send_message(message.from_user.id, f"В инвентаре нет '{name}'")
                medicine_menu(message)
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")
            medicine_menu(message)


# удаление лекарства
@bot.message_handler(func=lambda message: message.text == "Уменьшить количество лекарства")
# проверка доступа
def del_medicine_access(message):
    if allowed(message):
        del_medicine_name(message)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")
# получение названия лекарства
def del_medicine_name(message):
    global name
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(
        types.KeyboardButton(text="Назад в основное меню")
    )
    bot.send_message(message.chat.id, "Введите название лекарства:", reply_markup=keyboard)
    bot.register_next_step_handler(message, del_medicine_quant)
# получение количества лекарства
def del_medicine_quant(message):
    if menu(message):
        start_message(message)
    else:
        global name
        name = message.text
        global quantity
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Назад в основное меню")
        )
        bot.send_message(message.chat.id, "Введите число, на которое необходимо увеличить количество лекарства:", reply_markup=keyboard)
        bot.register_next_step_handler(message, del_medicine_commit)
# запрос в базу данных для удаления лекарства
def del_medicine_commit(message):
    if menu(message):
        start_message(message)
    else:
        try:
            quantity = message.text
            cursor.execute("SELECT quantity FROM medicine WHERE title=?", name)
            current_quantity = cursor.fetchone()
            if current_quantity:
                current_quantity = current_quantity[0]
                new_quantity = int(current_quantity) - int(quantity)
                if new_quantity > 0:
                    cursor.execute(
                        "UPDATE medicine SET quantity=? WHERE title=?",
                        (new_quantity, name),
                    )
                    conn.commit()
                    bot.send_message(
                        message.from_user.id,
                        f"Лекарство {name} в количестве {quantity} успешно удалено",
                    )
                    medicine_menu(message)
                else:
                    cursor.execute("DELETE FROM medicine WHERE title=?", (name,))
                    conn.commit()
                    bot.send_message(message.from_user.id, f"Лекарство {name} удалено")
                    medicine_menu(message)
            else:
                bot.send_message(message.from_user.id, f"В инвентаре нет {name}")
                medicine_menu(message)
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")
            medicine_menu(message)


# получение совета по симптомам
@bot.message_handler(func=lambda message: message.text == "Посоветовать лекарство")
# проверка доступа
def advice_medicine_access(message):
    if allowed(message):
        advice_medicine_menu(message)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")
# добавление кнопок
def advice_medicine_menu(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(text="Раны", callback_data="Раны"),
        types.InlineKeyboardButton(text="Горло", callback_data="Горло"),
        types.InlineKeyboardButton(text="Голова", callback_data="Голова"),
        types.InlineKeyboardButton(text="Пищеварение", callback_data="Пищеварение"),
        types.InlineKeyboardButton(text="Нос", callback_data="Нос"),
        types.InlineKeyboardButton(text="Антибиотики", callback_data="Антибиотики"),
        types.InlineKeyboardButton(text="Аллергия", callback_data="Аллергия"),
        types.InlineKeyboardButton(text="ВПЧ", callback_data="ВПЧ"),
        types.InlineKeyboardButton(text="Давление", callback_data="Давление"),
        types.InlineKeyboardButton(text="Сердце", callback_data="Сердце"),
        types.InlineKeyboardButton(text="Отравление", callback_data="Отравление"),
        types.InlineKeyboardButton(text="Инструменты", callback_data="Инструменты"),
        types.InlineKeyboardButton(text="Боль", callback_data="Боль"),
        types.InlineKeyboardButton(text="Очищение", callback_data="Очищение"),
        types.InlineKeyboardButton(text="Кашель", callback_data="Кашель"),
        types.InlineKeyboardButton(text="Нервная система", callback_data="Нервная система"),
    )
    bot.send_message(
        message.chat.id,
        "Давай я помогу подобрать лекарство! Что у тебя случилось?",
        reply_markup=keyboard,
    )
# обработчик нажатия кнопок для симптомов, запрос в бд
@bot.callback_query_handler(func=lambda call: True)
def advice_medicine(call):
    try:
        symptom = call.data
        cursor.execute(
            "SELECT title, quantity FROM medicine WHERE prescription=? OR prescription_two=?",
            (symptom, symptom),
        )
        drugs_data = cursor.fetchall()
        if drugs_data:
            response = "\n"
            for row in drugs_data:
                response += f"Препарат: {row[0]}\nКоличество: {row[1]}\n\n"
            bot.send_message(
                call.message.chat.id,
                f"Рекомендации при симптоме '{symptom}':\n{response}",
            )
        else:
            bot.send_message(
                call.message.chat.id, f"Нет рекомендаций при симптоме {symptom}"
            )
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Произошла ошибка: {str(e)}")


# -------------------------------СПИСОК ПОКУПОК-----------------------------------#


# вывод кнопок для покупок
@bot.message_handler(
    func=lambda message: message.text == "Список покупок"
)
def start_shop(message):
    if allowed(message):
        shop_menu(message)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")
    
def shop_menu(message):
    if allowed(message):
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Показать список"),
            types.KeyboardButton(text="Добавить в список"),
            types.KeyboardButton(text="Убрать из списка"),
            types.KeyboardButton(text="Поддержка"),
            types.KeyboardButton(text="Назад в основное меню"),
        )
        cursor.execute('SELECT url FROM pic WHERE title = ?', "shop")
        photo_url = cursor.fetchone()[0]  # url картинки
        bot.send_photo(message.chat.id, photo=photo_url, caption="Вы находитесь в разделе 'Список покупок'\n" "Чем я могу Вам помочь?", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")
# получение списка покупок
@bot.message_handler(func=lambda message: message.text == "Показать список")
# проверка доступа
def acesss_shoplist(message):
    if allowed(message):
        shoplist(message)
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Назад в основное меню"),
        )
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")
# запрос в базу данных для получения списка покупок
def shoplist(message):
    cursor.execute("SELECT * FROM shop")
    drugs_data = cursor.fetchall()
    if drugs_data:
        response = "Список покупок:\n"
        for row in drugs_data:
            response += f"Продукт: {row[1]}\nКоличество: {row[2]}\nЗаметка: {row[3]}\n\n"
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Нет информации о предстоящих покупках")


# добавление в список позиций
@bot.message_handler(func=lambda message: message.text == "Добавить в список")
# проверка доступа
def access_add_shoplist(message):
    if allowed(message):
        new_shoplist_name(message)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")
# получение названия
def new_shoplist_name(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(
        types.KeyboardButton(text="Назад в основное меню")
    )
    bot.send_message(message.chat.id, "Введите название товара:", reply_markup=keyboard)
    bot.register_next_step_handler(message, new_shoplist_quant)
# получение количества
def new_shoplist_quant(message):
    if menu(message):
        start_message(message)
    else:
        global name
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Назад в основное меню")
        )
        bot.send_message(message.chat.id, "Введите количество товара:", reply_markup=keyboard)
        if menu(message):
            start_message(message)
        else:
            name = message.text
            bot.register_next_step_handler(message, new_shoplist_prescript)
# получение заметки
def new_shoplist_prescript(message):
    if menu(message):
        start_message(message)
    else:
        global quantity
        quantity = message.text
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Назад в основное меню"),
            types.KeyboardButton(text="Пропустить")
        )
        bot.send_message(message.chat.id, "Введите заметку:", reply_markup=keyboard)
        bot.register_next_step_handler(message, new_shoplist_commit)
# запись полученнной информации в базу данных
def new_shoplist_commit(message):
    if menu(message):
        start_message(message)
    else:
        try:
            global note
            if message.text == "Пропустить":
                note = None
            else:
                note = message.text
            cursor.execute(
                "INSERT INTO shop (title, quantity, [note]) VALUES (?, ?, ?)",
                (name, quantity, note)
            )
            conn.commit()
            bot.send_message(
                message.from_user.id,
                f"Продукт '{name}' в количестве '{quantity}' успешно добавлен в список покупок!",
            )
            shop_menu(message)
            
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")
            shop_menu(message)


# удаление позиции из списка покупок
@bot.message_handler(func=lambda message: message.text == "Убрать из списка")
# проверка доступа
def del_shoplist_access(message):
    if allowed(message):
        del_shoplist_menu(message)
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к боту")
# варианты для удаления
def del_shoplist_menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(
        types.KeyboardButton(text="Удалить список покупок полностью"),
        types.KeyboardButton(text="Удалить одну позицию из списка покупок"),
        types.KeyboardButton(text="Назад в основное меню"),
    )
    bot.send_message(
        message.from_user.id, "Что вы хотите сделать?", reply_markup=keyboard
    )
# удаление списка
@bot.message_handler(
    func=lambda message: message.text == "Удалить список покупок полностью"
)
def del_shoplist_full(message):
    cursor.execute("DELETE FROM shop")
    conn.commit()
    bot.send_message(message.from_user.id, "Список покупок был успешно удален!")
# удаление позиции
@bot.message_handler(
    func=lambda message: message.text == "Удалить одну позицию из списка покупок"
)
# получение названия позиции
def del_shoplist_name(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(
        types.KeyboardButton(text="Назад в основное меню")
    )
    bot.send_message(message.chat.id, "Введите название товара:", reply_markup=keyboard)
    bot.register_next_step_handler(message, del_shoplist)
# удаление лекарства из базы данных
def del_shoplist(message):
    if menu(message):
        start_message(message)
    else:
        try:
            global name
            name = message.text
            cursor.execute("DELETE FROM shop WHERE title=?", (name,))
            conn.commit()
            bot.send_message(message.from_user.id, f"Продукт '{name}' был удален из списка!")
            shop_menu(message)
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")
            shop_menu(message)


# -------------------------------ФАКС-----------------------------------#


@bot.message_handler(func=lambda message: message.text == "Факс")
# прием сообщения
def fax_name(message):
    global fax
    fax = f"Факс от пользователя {message.chat.username}:\n"
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(
        types.KeyboardButton(text="egorkurochkin") # тут требуется ввести ник
    )
    bot.send_message(message.chat.id, "Выберите, кому адресовано сообщение:", reply_markup=keyboard)
    bot.register_next_step_handler(message, fax_message)
def fax_message(message):
    if menu(message):
        start_message(message)
    else:
        global fax
        fax += f"Кому: {message.text}\n\n"
        global name
        name = message.text
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(
            types.KeyboardButton(text="Назад в основное меню")
        )
        bot.send_message(message.chat.id, "Напишите сообщение", reply_markup=keyboard)
        bot.register_next_step_handler(message, fax_print)
# печать
def fax_print(message):
    if menu(message):
        start_message(message)
    else:
        try:
            doc = Document()
            global fax
            fax += f"Сообщение:\n"
            fax += message.text
            doc.add_paragraph(fax)
            doc.save("fax.docx")
            os.startfile("fax.docx", "print")
            bot.send_message(message.chat.id, "Факс успешно отправлен!")
            bot.send_message(786411454, fax) #необходимо ввести свой ID (НЕ ник) для получени сообщений об отправленном факсе
            start_message(message)
            time.sleep(10)
            os.remove("fax.docx")
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")


#-------------------------------------------------PRINT------------------------------------------------#

@bot.message_handler(func=lambda message: message.text == "Печать" or message.text == "Печать")
def send_doc(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(
            types.KeyboardButton(text="Назад в основное меню")
                )
    bot.send_message(message.chat.id, "Отправьте файл для печати", reply_markup=keyboard)
    bot.register_next_step_handler(message, printing)

def printing(message):
    if menu(message):
        start_message(message)
    else:
        try:
            FILE_PATH = 'print'
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            # Определение расширения файла
            file_extension = guess_extension(message.document.mime_type)
            if file_extension is None:
                bot.reply_to(message, "Неподдерживаемый тип файла.")
                return

            # Сохранение файла с соответствующим расширением
            full_file_path = f"{FILE_PATH}{file_extension}"
            with open(full_file_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, f"Отправляю на печать...")
            os.startfile(full_file_path, "print")
            bot.reply_to(message, "Файл отправлен на печать.")
            time.sleep(10)
            os.remove(full_file_path)
        except Exception as e:
            bot.reply_to(message, f"Произошла ошибка: {e}")
            os.remove(full_file_path)


# запуск бота
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)