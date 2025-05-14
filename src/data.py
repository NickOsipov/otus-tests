"""
Script: data.py
"""


def load_csv_data(filepath: str, header: bool=True) -> dict:
    """
    Загружает данные из CSV-файла.
    
    Parameters
    ----------
    filepath : str
        Путь к файлу CSV.
    header : bool, optional
        Флаг, указывающий, содержит ли файл заголовок, по умолчанию True.
    
    Returns
    -------
    list of list
        Данные из CSV в виде списка списков.
    list or None
        Список заголовков, если header=True, иначе None.
    """
    data = []
    header_data = None
    
    with open(filepath, 'r') as file:
        if header:
            header_line = file.readline().strip()
            header_data = header_line.split(',')
        
        for line in file:
            values = line.strip().split(',')
            # Преобразуем числовые значения из строк в числа
            processed_values = []
            for val in values:
                try:
                    # Пробуем преобразовать в число, если возможно
                    if '.' in val:
                        processed_values.append(float(val))
                    else:
                        processed_values.append(int(val))
                except ValueError:
                    # Если не число, оставляем как строку
                    processed_values.append(val)
            
            data.append(processed_values)
    
    return {"header": header_data, "data": data}


def split_data(data, split_ratio=0.8):
    """
    Разделяет данные на две части в соответствии с указанным соотношением.
    
    Parameters
    ----------
    data : list
        Список данных для разделения.
    split_ratio : float, optional
        Коэффициент разделения, определяющий размер первой части 
        (от 0 до 1), по умолчанию 0.8.
    
    Returns
    -------
    list
        Первая часть данных (размер = split_ratio * len(data)).
    list
        Вторая часть данных (оставшаяся часть).
    
    Raises
    ------
    ValueError
        Если split_ratio не в диапазоне (0, 1).
    """
    if split_ratio <= 0 or split_ratio >= 1:
        raise ValueError("split_ratio должен быть в диапазоне (0, 1)")
    
    # Определяем точку разделения
    split_point = int(len(data) * split_ratio)
    
    # Разделяем данные
    first_part = data[:split_point]
    second_part = data[split_point:]
    
    return first_part, second_part