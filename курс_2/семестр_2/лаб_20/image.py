from PIL import Image, ImageDraw

def picture():
    image = Image.new("RGB", (500, 500), "#AED8E6")
    drawer = ImageDraw.Draw(image)

    # Основа дома
    drawer.rectangle(((20, 200), (270, 500)), "#008001")

    # Лестница
    drawer.polygon(
        (
            (270, 350),
            (360, 350),
            (360, 425),
            (450, 425),
            (450, 500),
            (270, 500),
        ),
        "#FE0000"
    )

    # Крыша
    drawer.polygon(
        (
            (20, 200),
            (145, 80),
            (270, 200),
        ),
        "#0000FE"
    )

    # Полумесяц
    drawer.arc([(40, 80), (100, 140)],  -30, 150, "#55414E")

    # Антена
    drawer.line(((270, 200), (270, 90)), "#34505C", 2)
    drawer.line(((270, 90), (240, 45)), "#34505C", 2)
    drawer.line(((270, 90), (300, 45)), "#34505C", 2)

    # Солнце
    drawer.ellipse([(400, 20), (500, 120)], "#FFFF01")
   
    image.show()
    image.save("house.png")
picture()