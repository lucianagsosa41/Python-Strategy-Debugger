def build_summary(context: dict) -> str:
    """
    Crea un resumen legible sin depender de modelos externos.
    En producción, este módulo se reemplaza por un llamado a un LLM vía n8n.
    """
    parts = []
    parts.append("### Resumen del pipeline\n")
    meta = context.get("meta", {})
    if meta:
        parts.append(f"- Estrategia: {meta.get('strategy', 'N/A')}")
        parts.append(f"- Archivo de datos: {meta.get('data_path', 'N/A')}")
        parts.append(f"- Filas: {meta.get('rows', 'N/A')}")
    val = context.get("validation", {})
    parts.append("\n### Validación")
    parts.append(f"- OK: {val.get('ok', False)}")
    if not val.get('ok', True):
        issues = val.get("issues", [])
        for it in issues:
            parts.append(f"  - ⚠️ {it}")
    dbg = context.get("debug", {})
    parts.append("\n### Debug")
    parts.append(f"- Status: {dbg.get('status','N/A')}")
    if dbg.get("status") == "error":
        parts.append(f"- Error: {dbg.get('error','')}")
    bt = context.get("backtest", {})
    parts.append("\n### Backtest (mini)")
    if bt:
        parts.append(f"- Retorno acumulado: {bt.get('cum_return', 0.0):.4f}")
        parts.append(f"- Máx. drawdown: {bt.get('max_drawdown', 0.0):.4f}")
        parts.append(f"- Return/DD: {bt.get('return_over_dd', 0.0):.4f}")
    else:
        parts.append("- No se pudo calcular (error en estrategia).")
    parts.append("\nSiguiente paso sugerido: aprobación humana antes de aplicar cambios.")
    return "\n".join(parts) + "\n"
