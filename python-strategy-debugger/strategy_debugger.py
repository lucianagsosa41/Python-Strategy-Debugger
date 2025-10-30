import importlib, argparse, json, traceback, pandas as pd
from validators import validate_price_df
from backtester import simple_backtest
from ai_summary_stub import build_summary

def load_strategy(dotted: str):
    """
    Carga dinámica de estrategia: 'module:function', p.ej. 'example_strategy:my_strategy'
    """
    if ":" not in dotted:
        raise ValueError("Formato inválido. Usa 'module:function', p.ej. example_strategy:my_strategy")
    mod_name, fn_name = dotted.split(":")
    mod = importlib.import_module(mod_name)
    fn = getattr(mod, fn_name, None)
    if fn is None:
        raise AttributeError(f"No se encontró la función '{fn_name}' en el módulo '{mod_name}'")
    return fn

def main():
    ap = argparse.ArgumentParser(description="Strategy Debugger & Mini Backtester")
    ap.add_argument("--strategy", required=True, help="Formato 'module:function'. Ej: example_strategy:my_strategy")
    ap.add_argument("--data", required=True, help="Ruta a CSV con columnas: timestamp, open, high, low, close")
    ap.add_argument("--report", default="results/report.json", help="Salida JSON")
    ap.add_argument("--summary", default="results/summary.txt", help="Salida resumen legible")
    args = ap.parse_args()

    df = pd.read_csv(args.data)
    val = validate_price_df(df)

    debug = {}
    signals = None
    try:
        strategy_fn = load_strategy(args.strategy)
        signals = strategy_fn(df)
        debug = {"status": "success", "error": None}
    except Exception as e:
        debug = {"status": "error", "error": str(e), "trace": traceback.format_exc()}

    backtest = {}
    if debug["status"] == "success":
        try:
            backtest = simple_backtest(df, signals)
        except Exception as e:
            backtest = {"error": str(e), "trace": traceback.format_exc()}

    context = {
        "meta": {
            "strategy": args.strategy,
            "data_path": args.data,
            "rows": int(len(df))
        },
        "validation": val,
        "debug": debug,
        "backtest": backtest,
    }

    # Guardar JSON
    with open(args.report, "w") as f:
        json.dump(context, f, indent=2, ensure_ascii=False)

    # Guardar resumen
    with open(args.summary, "w") as f:
        f.write(build_summary(context))

    print(f"✅ Reporte: {args.report}")
    print(f"✅ Resumen: {args.summary}")

if __name__ == "__main__":
    main()
