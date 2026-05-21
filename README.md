# Crypto Analyst — 4-Agent Real-Time Market Analysis System

> 4 AI agents collaborate to produce analyst-grade Buy / Hold / Sell reports for any cryptocurrency, grounded in live market data and current news.

---

## What it does

Give it any cryptocurrency ticker (BTC, ETH, SOL, etc.). The system:

1. Gathers the latest news on the asset
2. Analyzes market sentiment from coverage
3. Pulls live price plus 7-day trend data
4. Synthesizes a final analyst report with Buy / Hold / Sell recommendation

Tested on Bitcoin, Ethereum, and Solana — each returned distinct, data-grounded recommendations driven by different signals.

## How it works

| Agent | Role |
|---|---|
| **News Researcher** | Searches the web for the latest news on the asset; summarizes key events |
| **Sentiment Analyst** | Evaluates tone and sentiment of the news coverage |
| **Market Tracker** | Fetches live price + 7-day historical trend |
| **Report Writer** | Synthesizes all inputs into a final analyst report with a recommendation |

All four agents are orchestrated through CrewAI's sequential workflow.

## Tech stack

- **Language:** Python
- **Agent framework:** CrewAI
- **LLM:** OpenAI API
- **Data:** Open news APIs, market data APIs, web scraping

## Run it locally

```bash
git clone https://github.com/kvssyugal/crypto-analyst.git
cd crypto-analyst
pip install -r requirements.txt
cp .env.example .env   # add your API keys
python main.py
```

## Sample output

The system produces structured reports per asset that include: latest news summary, sentiment score, current price + 7-day change, and a final recommendation with reasoning.

## Why I built this

Most "crypto AI" tools are single-prompt wrappers that confidently make recommendations without grounding. I wanted to test whether splitting research, sentiment, market data, and synthesis into specialized agents would produce more honest, evidence-backed outputs. The results were noticeably more nuanced than single-prompt baselines.

## About me

Built by **[Yugal Kanukolanu](https://linkedin.com/in/yugalkvss)** — AI/ML Engineer, M.S. CS @ University of Louisville. Open to AI Engineer roles. [More projects](https://github.com/kvssyugal).

## License

MIT
