# 🧠 Python Strategy Debugger & Mini Backtester  

Project developed by **Luciana Sosa (2025)** as a technical demo to showcase how I structure a **Python + N8n** workflow focused on **debugging, validation, and backtesting** of trading or logic-based strategies.  

Designed for **portfolio and professional practice purposes**, inspired by real-world **automation and AI-assisted workflow** projects.  

---

## 🚀 Overview

This mini-framework allows you to:
- Validate financial (OHLC) datasets.  
- Execute Python-based strategies and capture errors or traces.  
- Perform a basic backtest (cumulative return, drawdown, ratio).  
- Automatically generate both **JSON** and **human-readable** reports.  

The workflow is structured to be easily **integrated into N8n** or any orchestration tool (Make, Airflow, etc.), dividing the process into modular steps or nodes.

---

## 🧩 Workflow (N8n-friendly)

```
Input (CSV/JSON)
   └── validators.py (structure and NaN checks)
       └── strategy_debugger.py (error handling & execution)
           └── backtester.py (metrics calculation)
               └── ai_summary_stub.py (human-readable summary)
                   └── report.json + summary.txt (final outputs)
```

> In an N8n flow, each part of this process would represent a **node**.  
> This repository provides the **building blocks** for automation pipelines and validation workflows.

---

## 🧰 Project Structure

```
python-strategy-debugger/
├── ai_summary_stub.py
├── backtester.py
├── strategy_debugger.py
├── validators.py
├── example_strategy.py
├── requirements.txt
├── data/
│   └── sample_prices.csv
├── results/          # output files
├── scripts/
│   └── run_all.sh
└── tests/
    └── test_strategy_debugger.py
```

---

## ▶️ Quickstart

```bash
# Clone and enter the project folder
git clone https://github.com/lucianagsosa41/python-strategy-debugger.git
cd python-strategy-debugger

# (Optional) Create a virtual environment
python -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the complete pipeline
python strategy_debugger.py --strategy example_strategy:my_strategy --data data/sample_prices.csv --report results/report.json --summary results/summary.txt
```

📁 **Generated outputs:**
- `results/report.json` → structured report (machine-readable)  
- `results/summary.txt` → readable summary report  

---

## 🧪 Sample Data

The project includes a small synthetic dataset (`data/sample_prices.csv`) with simulated OHLC values.  
This allows testing the pipeline **fully offline** without any external dependencies or APIs.

---

## 📊 Metrics Included
- **Cumulative Return**
- **Maximum Drawdown**
- **Return / Drawdown Ratio**
- **Sharpe-like Ratio (optional for future upgrades)**

---

## 🔧 N8n Integration Example

Example of how this can be mapped inside **N8n**:

1. **Node 1:** Read Binary File (CSV)  
2. **Node 2:** Run Python (validators.py)  
3. **Node 3:** Run Python (strategy_debugger.py)  
4. **Node 4:** Run Python (backtester.py)  
5. **Node 5:** Run Python (AI summary or LLM API)  
6. **Node 6:** Write Binary File (report.json / summary.txt)  
7. **Node 7:** Send results via Email, Telegram or Slack → Human validation  

> This setup allows a complete **validation → execution → analysis → human approval** workflow, which can be automated or extended with AI integration.

---

## 🧾 License
MIT License — free for educational and professional use.  
© **Luciana Sosa**, 2025  

---

## 📫 Contact
📧 [lucianagsosa41@gmail.com](mailto:lucianagsosa41@gmail.com)  
🌐 [GitHub](https://github.com/lucianagsosa41)  
📍 Mendoza, Argentina 🇦🇷
