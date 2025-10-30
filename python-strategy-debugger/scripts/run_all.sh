#!/usr/bin/env bash
set -e
python strategy_debugger.py --strategy example_strategy:my_strategy --data data/sample_prices.csv --report results/report.json --summary results/summary.txt
