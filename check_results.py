# check_results.py
import json


def check_results():
    try:
        with open('lighting_results.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"Всего собрано товаров: {len(data)}")
        print("\nПервые 10 товаров:")
        print("-" * 50)

        for i, item in enumerate(data[:10]):
            print(f"{i + 1}. {item['name']}")
            print(f"   Цена: {item['price']}")
            print(f"   Ссылка: {item['url']}")
            print()

    except FileNotFoundError:
        print("Файл lighting_results.json не найден. Сначала запустите паука.")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    check_results()