# analyze_card.py
from bs4 import BeautifulSoup


def analyze_card():
    with open('debug_page.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    print("=== АНАЛИЗ ОДНОЙ КАРТОЧКИ ===")

    # Найдем первую карточку
    card = soup.find('div', attrs={"data-testid": "product-card"})
    if not card:
        print("Не найдена карточка с data-testid='product-card'")
        return

    print("Найдена карточка")

    # Найдем все дочерние элементы с data-testid
    all_data_testids = card.find_all(attrs={"data-testid": True})
    print("\nВсе data-testid в карточке:")
    for elem in all_data_testids:
        testid = elem.get('data-testid')
        text = elem.get_text(strip=True)
        print(f"  {testid}: '{text}'")

    # Найдем все ссылки
    links = card.find_all('a', href=True)
    print("\nСсылки в карточке:")
    for link in links:
        print(f"  {link.get('href')}")

    # Найдем все элементы с текстом, содержащим рубль
    price_indicators = card.find_all(text=lambda t: '₽' in t or 'руб' in t)
    print("\nТексты с ценами:")
    for text in price_indicators:
        print(f"  '{text}'")


if __name__ == "__main__":
    analyze_card()