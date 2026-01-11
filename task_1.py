def find_item_index(items, target):
    """Находит индекс первого вхождения товара в списке.

    Args:
        items (list): Список товаров.
        target (str): Товар, который нужно найти.

    Returns:
        int or None: Индекс первого вхождения товара или None, если товар не найден.
    """
    try:
        # Пытаемся получить индекс первого вхождения товара
        return items.index(target)
    except ValueError:
        # Если товар не найден, возвращаем None
        return None


# Список товаров на складе
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Товары для поиска
search_items = ['банан', 'груша', 'персик']

# Проходимся по каждому товару для поиска его индекса
for find_item in search_items:
    # Вызываем функцию, чтобы получить индекс товара
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")