import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import expon

chat_id = 282219367 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    a = ((x+0.5)*2)/35**2
    alpha = 1 - p
    return a.mean() - np.sqrt(np.var(a)) * expon.ppf(1 - alpha / 2) / np.sqrt(len(a)), \
           a.mean() - np.sqrt(np.var(a)) * expon.ppf(alpha / 2) / np.sqrt(len(a))
