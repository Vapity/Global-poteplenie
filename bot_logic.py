

import requests
from bs4 import BeautifulSoup

# Получаем страницу
url = "https://ru.m.wikipedia.org/wiki/%D0%93%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D0%BF%D0%BE%D1%82%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Функция для получения информации из нужного раздела
def get_section_info(section_name):
    # Шаг 1: Найти нужный заголовок
    for heading in soup.find_all(['h2', 'h3']):
        if section_name in heading.text:
            print(f"Нашли раздел: {section_name}")
            
            # Шаг 2: Собираем параграфы после заголовка
            paragraphs = []
            next_element = heading.find_next()
            
            # Шаг 3: Продолжаем, пока не встретим другой заголовок
            while next_element and not next_element.name in ['h2', 'h3']:
                if next_element.name == 'p':
                    paragraphs.append(next_element.text)
                next_element = next_element.find_next()
            
            return ' '.join(paragraphs)
    
    return ["Раздел не найден"]

# Пример использования



