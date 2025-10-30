import json, os, subprocess, sys

def test_pipeline_runs():
    cmd = [sys.executable, "strategy_debugger.py", "--strategy", "example_strategy:my_strategy", "--data", "data/sample_prices.csv", "--report", "results/report.json", "--summary", "results/summary.txt"]
    subprocess.check_call(cmd, cwd=".")
    assert os.path.exists("results/report.json")
    assert os.path.exists("results/summary.txt")
    data = json.load(open("results/report.json"))
    assert "validation" in data and "debug" in data and "backtest" in data
