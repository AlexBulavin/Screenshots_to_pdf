__author__ = 'Alex Bulavin'
import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image as PILImage

# Путь к папке со скриншотами
screenshots_folder = '/Users/alex/Documents/Python_projects/screenshots_to_pdf/screenshots'

# Путь и имя выходного PDF файла
output_pdf = 'homework2.pdf'

# Получение списка файлов со скриншотами
screenshots = [f for f in os.listdir(screenshots_folder) if f.endswith('.png') or f.endswith('.jpg')]

# Сортировка скриншотов по имени файла (хронологический порядок)
screenshots.sort()

# Создание PDF документа
doc = SimpleDocTemplate(output_pdf, pagesize=A4)

# Список элементов документа
elements = []

# Размеры страницы PDF
page_width, page_height = A4

# Максимальный размер изображения на странице
max_image_width = page_width * 0.8
max_image_height = page_height * 0.8

# Стиль для надписи с именем файла
styles = getSampleStyleSheet()
filename_style = styles['Normal']

# Обработка каждого скриншота и добавление его в документ
for screenshot in screenshots:
    # Путь к текущему скриншоту
    screenshot_path = os.path.join(screenshots_folder, screenshot)

    # Открытие скриншота с помощью PIL
    img = PILImage.open(screenshot_path)

    # Масштабирование изображения, чтобы оно поместилось на страницу
    img.thumbnail((max_image_width, max_image_height))

    # Создание объекта изображения для скриншота
    reportlab_image = Image(img.filename, img.width, img.height)

    # Создание надписи с именем файла
    filename_paragraph = Paragraph(screenshot, filename_style)

    # Добавление элементов в список элементов документа
    elements.append(filename_paragraph)
    elements.append(reportlab_image)

# Сборка документа и запись в файл
doc.build(elements)

print('PDF файл успешно создан:', output_pdf)
