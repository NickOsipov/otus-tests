"""
Script: models.py
"""

class MeanPredictor:
    """
    Простейшая 'модель', которая предсказывает среднее значение из обучающей выборки.
    """
    
    def __init__(self):
        """Инициализация модели."""
        self.mean = None
        self.is_fitted = False
    
    def fit(self, X, y):
        """
        'Обучает' модель, вычисляя среднее значение y.
        
        Parameters
        ----------
        X : list
            Признаки (не используются в этой модели).
        y : list
            Целевые значения.
            
        Returns
        -------
        self
            Объект модели.
        """
        if not y:
            raise ValueError("y не может быть пустым")
            
        self.mean = sum(y) / len(y)
        self.is_fitted = True
        return self

    def predict(self, X):
        """
        Предсказывает одно и то же значение (среднее) для всех примеров.
        
        Parameters
        ----------
        X : list
            Признаки (не используются).
            
        Returns
        -------
        list
            Предсказания - среднее значение для каждого примера.
        """
        if not self.is_fitted:
            raise ValueError("Модель не обучена. Сначала вызовите fit().")
            
        return [self.mean] * len(X)
