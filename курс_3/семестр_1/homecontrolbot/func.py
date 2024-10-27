from database import allowed_users

def menu(message):
    if message.text == "Назад в основное меню":
        return True
    
def allowed(message):
    if message.from_user.username in allowed_users:
        return True