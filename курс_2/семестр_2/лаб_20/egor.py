from PIL import Image, ImageDraw
import random

def randomColor(): # генерация цветов
        # 0 - черный цвет -> исключаем из диапазона для randint
        colorR = random.randint(1, 255)
        colorG = random.randint(1, 255)
        colorB = random.randint(1, 255)
        return(colorR, colorG, colorB) # возвращаем кортеж из цветов

def picture():
    image = Image.new("RGB", (1160, 500))
    drawer = ImageDraw.Draw(image)

    # Прямая линия из кругов (Е)
    for y in range(0, 5):
        # Иксы углов остаются неизменными, меняем только y
        drawer.ellipse(
            (
                (0, 0 + y * 100), 
                (100, 100 + y * 100)
            ), randomColor())

    # Дополнительные линии из кругов (Е)
    for i in range(0, 3):
        for j in range(0, 2):
            # Нужно менять и x, и y
            drawer.ellipse(
                (
                    (100 + j * 100, 0 + i * 200), 
                    (200 + j * 100, 100 + i * 200)
                ), randomColor())

    # Буква 'Г'
    drawer.rectangle(((310, 0), (410, 500)), randomColor())
    drawer.rectangle(((410, 0), (600, 100)), randomColor())

    # Буква 'О'
    drawer.ellipse([(590, 0), (890, 495)], randomColor())
    drawer.arc([(610, 10), (870, 485)], 0, 360)

    # Буква 'Р'
    drawer.polygon(
        (
            (900, 0), 
            (900, 500),
            (1000, 500),
            (1000, 250),
            (1100, 250),
            (1150, 230),
            (1150, 30),
            (1100, 0)
        ),
        randomColor()
    )
    image.show()
    image.save("egor.png") # сохранение изображения
    
picture()