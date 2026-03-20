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
    list
        Список заголовков, если header=True, иначе пустой список.
    """
    data = []
    header_data = []
    
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

if __name__ == "__main__":
    filepath = "test.csv"
    result = load_csv_data(filepath)
    print(result)
