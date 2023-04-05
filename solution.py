import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import expon

chat_id = 282219367 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = 1
    scale = 1
    return (x.mean() - 1/2 + expon.ppf(1 - alpha, loc=loc, scale=scale))/35**2, \
            (x.mean() - 1/2 - expon.ppf(alpha, loc=loc, scale=scale))/35**2
