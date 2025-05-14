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
    
    if min_val == max_val:
        return [0.5] * len(data)  # Особый случай, когда все значения одинаковые
        
    return [(x - min_val) / (max_val - min_val) for x in data]


def remove_missing_values(data):
    """
    Удаляет пропущенные значения (None) из списка.
    
    Parameters
    ----------
    data : list
        Список, который может содержать None.
        
    Returns
    -------
    list
        Список без None значений.
    """
    return [x for x in data if x is not None]