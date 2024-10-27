import pyodbc
import telebot
import os

# подключение к базе данных
db_name = "botdatabase.accdb" # относительный путь
db_path = os.path.join(os.path.dirname(__file__), db_name) # получение абсолютного пути
conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=" + db_path  
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# токен
bot = telebot.TeleBot("ВСТАВИТЬ ТОКЕН СЮДА")

# разрешенные пользователи
cursor.execute('SELECT allowed FROM allowed')
allowed_users = [row[0] for row in cursor.fetchall()]
