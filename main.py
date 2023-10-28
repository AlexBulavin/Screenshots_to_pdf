__author__ = 'Alex Bulavin'
import os

from reportlab.platypus import Image, PageBreak
from PIL import Image as PILImage
from tqdm import tqdm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.fonts import addMapping


# Путь к папке со скриншотами. Указать свой.
screenshots_folder = '/Users/alex/Documents/Python_projects/screenshots_to_pdf/screenshots'

# Путь и имя выходного PDF файла
output_pdf = 'Your_file_name_here.pdf' #Изменить название файла на своё

# Получение списка файлов со скриншотами
screenshots = [f for f in os.listdir(screenshots_folder) if f.endswith('.png') or f.endswith('.jpg')]
#print(screenshots) #Лог, чтобы убедиться в корректности имени файла на старте

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

# Указание пути к файлу TTF-шрифта и его имени
font_path = 'Fonts/Arial/arialmt.ttf'
font_name = 'Arial'

# Устанавливаем шрифт с поддержкой кириллицы
pdfmetrics.registerFont(TTFont(font_name, font_path))

# Добавляем маппинг шрифта для кириллических символов
addMapping('Arial', 0, 0, 'Arial')

# Стиль для надписи с именем файла
styles = getSampleStyleSheet()
filename_style = Paragraph('filename_style')
filename_style = styles['Normal']
filename_style.fontName = font_name
filename_style.wordWrap = 'UTF8'

# Обработка каждого скриншота и добавление его в документ
for screenshot in tqdm(screenshots, desc='Creating PDF'):
    # Путь к текущему скриншоту
    screenshot_path = os.path.join(screenshots_folder, screenshot)

    # Открытие скриншота с помощью PIL
    img = PILImage.open(screenshot_path)

    # Масштабирование изображения, чтобы оно поместилось на страницу
    img.thumbnail((max_image_width, max_image_height))

    # Создание объекта изображения для скриншота
    reportlab_image = Image(screenshot_path, img.width, img.height)

    # Создание надписи с именем файла
    filename_paragraph = Paragraph(screenshot, filename_style, encoding='utf-8')
    print(filename_paragraph)
    # Добавление элементов в список элементов документа
    elements.append(filename_paragraph)
    elements.append(reportlab_image)
    elements.append(PageBreak())  # Переход на следующую страницу

# Сборка документа и запись в файл
doc.build(elements)

print('PDF файл успешно создан:', output_pdf)
