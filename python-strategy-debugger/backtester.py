import pandas as pd
import numpy as np

def simple_backtest(df: pd.DataFrame, signals: pd.Series) -> dict:
    """
    Ejecuta un backtest **muy** simple:
    - signals: Serie {+1: long, 0: flat, -1: short} alineada con df.index
    - Retorno diario = señal de ayer * retorno de hoy (retorno logarítmico)
    """
    df = df.copy()
    df["ret"] = np.log(df["close"]).diff().fillna(0.0)
    sig = signals.reindex(df.index).fillna(0.0)
    df["strat_ret"] = sig.shift(1).fillna(0.0) * df["ret"]
    cumret = float(np.exp(df["strat_ret"].sum()) - 1.0)

    # drawdown
    equity = (df["strat_ret"].cumsum()).apply(np.exp)
    peak = equity.cummax()
    dd = (equity - peak) / peak
    max_dd = float(dd.min())

    ratio = float(cumret / abs(max_dd)) if max_dd != 0 else float("inf")
    return {
        "cum_return": cumret,
        "max_drawdown": max_dd,
        "return_over_dd": ratio,
        "n_obs": int(len(df)),
    }
