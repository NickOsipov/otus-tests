def mean_value(data):
    """Возвращает среднее значение списка."""
    if not data:
        return 0
    return sum(data) / len(data)
