# AutoTrader Web Python Library: Broker-Independent Trading API for 40+ Indian Brokers

> Place, modify, cancel and track orders across **40+ Indian brokers** from your own **Python** code. Write your logic once, trade on any broker, and never change a line of code to switch. Part of **[AutoTrader Web](https://stocksdeveloper.in/)** by **Stocks Developer**.

[![PyPI](https://img.shields.io/badge/pip-AutoTrader--Web--API--Stocks--Developer-3776ab)](https://pypi.org/project/AutoTrader-Web-API-Stocks-Developer/)
[![Brokers supported](https://img.shields.io/badge/brokers-40%2B-2ea44f)](https://stocksdeveloper.in/#supported-brokers)
[![Free trial](https://img.shields.io/badge/free%20trial-1%20month-blue)](https://webx.stocksdeveloper.in/register)
[![Uptime](https://img.shields.io/badge/uptime-99.98%25-brightgreen)](https://stocksdeveloper.in/features/)
[![API docs](https://img.shields.io/badge/docs-API%20reference-8a2be2)](https://stocksdeveloper.in/documentation/api/)

---

## What is this library?

The **AutoTrader Web Python library** is a broker-independent trading client. You write your strategy once in Python and run it against any broker that AutoTrader Web supports. The same function calls work on every broker, so changing broker does not mean rewriting your code.

- **Broker independent.** One codebase works across 40+ Indian brokers. The system handles each broker's API and trading-symbol format for you.
- **Full order control.** Regular, bracket, cover and advanced orders, plus modify, cancel and square-off.
- **Read your portfolio.** Live orders, positions, holdings and margins from your code.
- **Multi-account.** Place into one account or many at once.
- **Direct connection.** Your code talks to AutoTrader Web over a secure web connection. Nothing extra to install.

## What is AutoTrader Web?

**[AutoTrader Web](https://stocksdeveloper.in/)** by **Stocks Developer** is copy trading and multi-account software for Indian brokers. Monitor every broker account on one screen and act across all of them at once.

- **All your accounts, one screen.** Live, consolidated P&L, holdings, positions, orders and margins across every account and broker.
- **Copy trading, two ways.** PMS copy from our terminal, and master-child copy in the background, across brokers, with per-account sizing. [Copy trading software](https://stocksdeveloper.in/copy-trading-software/)
- **Bulk orders.** Place, modify, cancel and square-off across many accounts in one action.
- **GTT, bracket and cover orders**, order slicing and market price protection.
- **TradingView automation.** Turn your own chart alerts into real orders.
- **APIs and SDKs.** Python, Java, C# and Excel, plus AmiBroker, MetaTrader and HTTP REST / CSV.
- **8+ years in operation. 99.98% uptime. 40+ brokers. Under 100 ms data latency.**

## Why traders and developers choose us

- 🆓 **Free static IP included** with every account. Saves up to **₹500 per broker account per month** that other tools charge extra for.
- 💸 **One of the lowest prices in the category.** **₹295 to ₹495 per account per month**, all taxes and the static IP included. No setup fee, no hidden charges.
- ☁️ **Nothing to install for the platform.** Monitor and trade from your browser on PC or mobile, from anywhere. (Developer libraries connect directly to our servers.)
- 🔗 **40+ Indian brokers on one platform.** One of the widest broker coverages available.
- 🔁 **Two ways to copy trade**, PMS and master-child, both included.
- 🔒 **Security you control.** API credentials encrypted and stored in India, broker OAuth login and two-factor authentication, portfolio data never stored, plus a Kill Switch and a full activity log.
- 🎁 **Free 1-month trial** on supported brokers.

## Supported brokers

AutoTrader Web works with **40+ Indian brokers**:

5paisa · AC Agarwal · Aetram Trades · Alice Blue · Ambalal Shares · Anand Rathi · Angel One · Arham Share · ATS · AxisDirect · Choice · DBOnline · Dhan · Eureka Share · Finvasia · Flattrade · FYERS · Groww · IIFL Securities · Jainam (Prop & Retail) · Kotak Securities · Mastertrust · Mirae Asset Sharekhan · MLB Stock Broking · Motilal Oswal · Nuvama · PL Capital (PLIndia) · Profitmart · Pune E-Stock Broking (PESB) · Raghunandan Money · Religare · Share India (Prop & Retail) · SMC India · Stocko · SW Capital · Tradejini · Tradeswift · Upstox · Wisdom Capital · Zebu · Zerodha

*Plus any broker that supports the Symphony XTS API.* See the [full, always-current broker list](https://stocksdeveloper.in/#supported-brokers) and the [broker setup guides](https://stocksdeveloper.in/documentation/supported-brokers/).

## Quick start

Install the library with pip (it also pulls its one dependency, `requests`):

```shell
python -m pip install AutoTrader-Web-API-Stocks-Developer
```

Create one instance with your API key and place an order. The same call works on every supported broker:

```python
from com.dakshata.autotrader.api.AutoTrader import AutoTrader

autotrader = AutoTrader.create_instance('<your-api-key>', AutoTrader.SERVER_URL)

# Place a regular limit order
response = autotrader.place_regular_order(
    'ABC123',        # your account
    '<exchange>',    # your exchange segment code
    'SBIN',          # trading symbol
    'BUY', 'LIMIT', 'INTRADAY',
    1, 330.35, 0.0)

print(response)
```

The same instance also handles bracket and cover orders, modify, cancel, square-off, and reading orders, positions, holdings and margins.

Full step-by-step guide: **[Python library setup](https://stocksdeveloper.in/documentation/client-setup/python-library/)**. Get your API key from your [account settings](https://webx.stocksdeveloper.in/register).

## Pricing and free trial

- **Free 1-month trial** on supported brokers, with every feature included.
- Then **₹295 to ₹495 per account per month**. All taxes and a free static IP are included. No setup fee, no hidden charges.
- [See full pricing](https://stocksdeveloper.in/pricing/) · [Start free](https://webx.stocksdeveloper.in/register)

## Documentation and links

| Resource | Link |
|---|---|
| 🌐 Website | https://stocksdeveloper.in/ |
| ✨ Features | https://stocksdeveloper.in/features/ |
| 💰 Pricing | https://stocksdeveloper.in/pricing/ |
| 🔁 Copy trading software | https://stocksdeveloper.in/copy-trading-software/ |
| 🏦 Supported brokers | https://stocksdeveloper.in/#supported-brokers |
| 🔒 Security and data handling | https://stocksdeveloper.in/security/ |
| 📘 Documentation | https://stocksdeveloper.in/documentation/getting-started/ |
| 🧩 API reference | https://stocksdeveloper.in/documentation/api/ |
| ⚙️ Python library setup | https://stocksdeveloper.in/documentation/client-setup/python-library/ |
| 📦 PyPI package | https://pypi.org/project/AutoTrader-Web-API-Stocks-Developer/ |
| 🆓 Start free (1-month trial) | https://webx.stocksdeveloper.in/register |
| ✉️ Contact us | https://stocksdeveloper.in/contact/ |

## About Stocks Developer

Stocks Developer is a technology company building software tools for Indian markets, shaped by 8+ years of trader feedback. Our software runs on Google Cloud in its Mumbai, India region for fast, low-latency performance, with strong security and high reliability.

Stocks Developer provides software tools only. It gives no investment advice, tips, recommendations, or trading strategies, and it makes no trading decisions for you. All trading and investment decisions remain solely your responsibility. You set up and control every activity, and you can stop it at any time.
