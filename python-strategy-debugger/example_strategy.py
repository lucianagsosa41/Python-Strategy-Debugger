import pandas as pd

def my_strategy(df: pd.DataFrame):
    """
    Ejemplo minimalista de estrategia:
    - Señal +1 si close > open, -1 si close < open, 0 si igual.
    - Retorna un pd.Series alineado con df.index
    """
    s = (df["close"] > df["open"]).astype(int) - (df["close"] < df["open"]).astype(int)
    s.name = "signal"
    return s
