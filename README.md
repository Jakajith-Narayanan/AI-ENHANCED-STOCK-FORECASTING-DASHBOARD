# AI-Enhanced Stock Forecasting Dashboard

This project is an intelligent stock market dashboard that:

- 📈 Forecasts the next 7 days of stock prices using machine learning (XGBoost)
- 📄 Analyzes uploaded financial PDF documents using NLP
- 🤖 Summarizes company reports using GPT (via OpenAI API)
- 💬 Provides sentiment analysis using VADER
- ✅ Gives final BUY / HOLD / SELL recommendations

---

## 🚀 Features

- 📈 **Stock Forecasting** (7-day forecast using historical closing prices)
- 📄 **PDF Upload** (e.g., reports from Apple, Infosys, TCS, etc.)
- 💬 **Sentiment Analysis** using VADER
- 🧠 **Report Summarization** using GPT-4 (OpenAI API)
- ✅ **Final Investment Recommendation** (BUY / HOLD / SELL)

---

## ⚙️ Setup Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-ENHANCED-STOCK-FORECASTING-DASHBOARD.git
cd AI-ENHANCED-STOCK-FORECASTING-DASHBOARD
```

2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required libraries such as:

1)Flask

2)yfinance

3)pandas

4)xgboost

5)nltk

6)openai

7)PyMuPDF (for reading PDF)


➤ Add it to your .env file
Create a .env file in the root folder and add:
```env
OPENAI_API_KEY=your_api_key_here
```

▶️ How to Run the App
Once everything is installed and the .env file is configured:

```bash
python app.py
```

🔗 Access it at:

```
http://localhost:5000
```


📂 Project Structure

.
├── app.py                  # Main Flask app

├── forecasting.py          # XGBoost stock prediction logic

├── sentiment_analysis.py   # PDF reading, sentiment & GPT summary

├── decision.py             # Recommendation logic

├── templates/

│   └── index.html          # Frontend HTML

├── static/

│   └── dashboard.js        # Frontend JS logic

├── .env.example            # Sample .env file

├── requirements.txt        # Python dependencies

├── runtime.txt             # Python version for Render (optional)

🇮🇳 Top 20 Indian Stock Symbols (NSE):-

| Company Name              | Symbol     | Sector              |

| ------------------------- | ---------- | ------------------- |

| Reliance Industries       | RELIANCE   | Energy/Conglomerate |

| Tata Consultancy Services | TCS        | IT Services         |

| Infosys Ltd               | INFY       | IT Services         |

| HDFC Bank Ltd             | HDFCBANK   | Banking             |

| ICICI Bank Ltd            | ICICIBANK  | Banking             |

| State Bank of India       | SBIN       | Banking (PSU)       |

| HCL Technologies          | HCLTECH    | IT Services         |

| Wipro Ltd                 | WIPRO      | IT Services         |

| Larsen & Toubro           | LT         | Infrastructure      |

| Hindustan Unilever Ltd    | HINDUNILVR | FMCG                |

| ITC Ltd                   | ITC        | FMCG                |

| Bharti Airtel             | BHARTIARTL | Telecom             |

| Bajaj Finance             | BAJFINANCE | NBFC                |

| Kotak Mahindra Bank       | KOTAKBANK  | Banking             |

| Maruti Suzuki India       | MARUTI     | Auto                |

| Tata Motors               | TATAMOTORS | Auto                |

| NTPC Ltd                  | NTPC       | Power               |

| Power Grid Corporation    | POWERGRID  | Power               |

| Sun Pharmaceutical        | SUNPHARMA  | Pharma              |

| Adani Enterprises         | ADANIENT   | Conglomerate        |





🌍 Top 20 Global Stock Symbols (NASDAQ/NYSE/ADR)

| Company Name             | Symbol    | Exchange    | Sector            |

| ------------------------ | --------- | ----------- | ----------------- |

| Apple Inc.               | AAPL      | NASDAQ      | Technology        |

| Microsoft Corp.          | MSFT      | NASDAQ      | Technology        |

| Amazon.com Inc.          | AMZN      | NASDAQ      | E-commerce/Cloud  |

| Alphabet Inc. (Google)   | GOOGL     | NASDAQ      | Technology        |

| Meta Platforms Inc.      | META      | NASDAQ      | Social Media      |

| Tesla Inc.               | TSLA      | NASDAQ      | EV/Auto           |

| NVIDIA Corp.             | NVDA      | NASDAQ      | Semiconductors    |

| Berkshire Hathaway Inc.  | BRK.B     | NYSE        | Conglomerate      |

| Johnson & Johnson        | JNJ       | NYSE        | Pharma/Healthcare |

| JPMorgan Chase & Co.     | JPM       | NYSE        | Banking           |

| Visa Inc.                | V         | NYSE        | FinTech           |

| Procter & Gamble         | PG        | NYSE        | FMCG              |

| Netflix Inc.             | NFLX      | NASDAQ      | Streaming         |

| Intel Corp.              | INTC      | NASDAQ      | Semiconductors    |

| The Coca-Cola Company    | KO        | NYSE        | Beverages         |

| PepsiCo Inc.             | PEP       | NASDAQ      | Beverages/Food    |

| Toyota Motor Corp. (ADR) | TM        | NYSE ADR    | Auto              |

| Alibaba Group (ADR)      | BABA      | NYSE ADR    | E-commerce        |

| Samsung Electronics Co.  | 005930.KS | KRX (Korea) | Electronics       |

| Nestlé SA                | NSRGY     | OTC ADR     | FMCG/Food         |




Notes:-
Works best with PDF reports that contain financial narratives.
You can switch between XGBoost and ARIMA inside app.py.
Modify forecasting.py if you want to try different ML models.



Future Improvements:-
FinBERT sentiment instead of VADER
Live stock ticker integration
User authentication
Database for saving uploaded files and reports


   

