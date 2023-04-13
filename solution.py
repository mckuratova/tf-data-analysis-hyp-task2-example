import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 906914964  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    pv = ks_2samp(x, y).pvalue
    res = False
    if pv < 0.02:
      res = True
    return res # Ваш ответ, True или False
