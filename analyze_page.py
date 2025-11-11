import requests
from bs4 import BeautifulSoup


def analyze_page():
    url = "https://www.divan.ru/category/svet"

    # Добавляем заголовки, чтобы сайт не блокировал нас
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем, что запрос прошел успешно

        soup = BeautifulSoup(response.text, 'html.parser')

        print("=== АНАЛИЗ СТРАНИЦЫ ДИВАН.РУ - ИСТОЧНИКИ ОСВЕЩЕНИЯ ===\n")

        # 1. Найдем все div элементы с классами, содержащими "product" или "card"
        product_divs = soup.find_all('div', class_=lambda x: x and any(
            word in str(x).lower() for word in ['product', 'card', 'item', 'goods', 'tovar']))

        print(f"Найдено потенциальных карточек товаров: {len(product_divs)}\n")

        # 2. Покажем подробную информацию о первых 3 карточках
        for i, div in enumerate(product_divs[:3]):
            print(f"--- Карточка товара {i + 1} ---")
            print("Классы:", div.get('class', []))

            # Найдем все текстовые элементы
            texts = [text.strip() for text in div.stripped_strings if text.strip() and len(text.strip()) > 2]
            print("Текстовые элементы:", texts[:8])  # Первые 8 текстовых элементов

            # Найдем все ссылки
            links = div.find_all('a', href=True)
            for link in links[:2]:  # Первые 2 ссылки
                href = link.get('href', '')
                if href:
                    print("Ссылка:", href)

            # Найдем элементы с ценами
            prices = div.find_all(text=lambda text: '₽' in text or 'руб' in text.lower())
            if prices:
                print("Цены:", prices)

            print()

        # 3. Поищем специфические элементы по data-атрибутам
        print("=== Поиск по data-атрибутам ===")
        data_product_cards = soup.find_all(attrs={"data-testid": True})
        data_product_count = len(
            [elem for elem in data_product_cards if 'product' in str(elem.get('data-testid', '')).lower()])
        print(f"Элементов с data-testid: {len(data_product_cards)}")
        print(f"Из них связанных с продуктами: {data_product_count}")

        # 4. Покажем уникальные data-testid
        unique_testids = set()
        for elem in data_product_cards:
            testid = elem.get('data-testid')
            if testid:
                unique_testids.add(testid)
        print("Уникальные data-testid:", list(unique_testids)[:10])

        # 5. Сохраним HTML для ручного анализа
        with open('debug_page.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        print("\nHTML страницы сохранен в файл: debug_page.html")

    except Exception as e:
        print(f"Ошибка при анализе страницы: {e}")


if __name__ == "__main__":
    analyze_page()