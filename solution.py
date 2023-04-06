import pandas as pd
import numpy as np
from math import log

from scipy.stats import norm
from scipy.stats import expon


chat_id = 282219367 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = p
    time = 35
    return (2 * np.mean(x) / time ** 2 -  norm.ppf(1 - alpha / 2, scale=2) / time ** 2, 2 * np.mean(x) / time ** 2 - norm.ppf(alpha / 2, scale=2) / time ** 2)
