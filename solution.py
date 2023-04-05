import pandas as pd
import numpy as np
from math import log

from scipy.stats import norm
from scipy.stats import expon


chat_id = 282219367 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    return (loc - 1/2 - log(1-alpha))*2/(35**2), \
           (loc - 1/2 - log(alpha))*2/(35**2)
