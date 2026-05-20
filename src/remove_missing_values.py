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
