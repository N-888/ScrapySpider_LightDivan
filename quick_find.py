from bs4 import BeautifulSoup

with open('debug_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Ищем все div с data-testid, начинающимся с "product-card"
cards = soup.select('div[data-testid^="product-card"]')
print(f"Найдено карточек: {len(cards)}")

if cards:
    first_card = cards[0]
    print("Первый элемент:")
    print("Классы:", first_card.get('class'))
    print("Data-testid:", first_card.get('data-testid'))
    print("Текст внутри:", first_card.get_text(strip=True)[:200])

    # Ищем внутри название
    title = first_card.select('[data-testid="product-title"]')
    if title:
        print("Найден product-title:", title[0].get_text(strip=True))
    else:
        print("Не найден product-title")

    # Ищем цену
    price = first_card.select('[data-testid="product-price"]')
    if price:
        print("Найден product-price:", price[0].get_text(strip=True))
    else:
        print("Не найден product-price")

    # Ищем ссылку
    link = first_card.find('a')
    if link:
        print("Ссылка:", link.get('href'))