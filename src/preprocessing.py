"""
Script: preprocessing.py
"""

def min_max_normalize(data):
    """
    Нормализует данные в диапазон [0, 1] по формуле:
    x_normalized = (x - min(data)) / (max(data) - min(data))
    
    Parameters
    ----------
    data : list
        Список чисел для нормализации
        
    Returns
    -------
    list : Нормализованные данные
    """
    if not data:
        return []
        
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val
    
    if min_val == max_val:
        return [0.5] * len(data)  # Особый случай, когда все значения одинаковые
        
    return [(x - min_val) / range_val for x in data]


if __name__ == "__main__":
    # Пример использования функции
    data = [10, 20, 30, 40, 50]
    normalized_data = min_max_normalize(data)
    print(normalized_data)
