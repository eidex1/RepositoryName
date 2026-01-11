
def find_common_participants(group1, group2, separator=','):
    """Находит общих участников из двух групп участников.

    Args:
        group1 (str): Участники первой группы, перечисленные через указанный разделитель.
        group2 (str): Участники второй группы, перечисленные через указанный разделитель.
        separator (str): Разделитель, по умолчанию запятая.

    Returns:
        list: Список общих участников, отсортированный в алфавитном порядке.
    """
    # Разделяем строки на участники
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим общие элементы
    common_participants = participants1.intersection(participants2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)


# Примеры участника из двух групп
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем работу функции с заданным разделителем
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')

print("Общие участники:", common_participants)
