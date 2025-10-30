import pandas as pd

REQUIRED_COLS = ["timestamp", "open", "high", "low", "close"]

def validate_price_df(df: pd.DataFrame) -> dict:
    issues = []

    # columnas mínimas
    for c in REQUIRED_COLS:
        if c not in df.columns:
            issues.append(f"Falta columna requerida: {c}")

    # tipos y orden
    if "timestamp" in df.columns:
        try:
            ts = pd.to_datetime(df["timestamp"])
        except Exception:
            issues.append("timestamp no es convertible a datetime")
            ts = None
        if ts is not None:
            if not ts.is_monotonic_increasing:
                issues.append("timestamp no está en orden creciente")
            if ts.duplicated().any():
                issues.append("timestamp tiene duplicados")

    # NaNs críticos
    for c in ["open", "high", "low", "close"]:
        if c in df.columns and df[c].isna().any():
            issues.append(f"Columna {c} contiene NaNs")

    return {
        "ok": len(issues) == 0,
        "issues": issues,
        "rows": len(df),
        "cols": list(df.columns),
    }
