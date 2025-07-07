import yfinance as yf
import pandas as pd
import numpy as np
from xgboost import XGBRegressor

HORIZON = 7  # forecast 7 days ahead


# ---------- 1. download & tidy data ----------
def fetch_prices(symbol: str) -> pd.DataFrame:
    """
    Download the past 400 days of daily closing prices from Yahoo Finance
    and return a tidy DataFrame with columns: ds (date) and y (close).
    Raises ValueError if no data is found.
    """
    df_raw = yf.download(symbol, period="400d")
    if df_raw.empty:
        raise ValueError(f"No price data found for symbol '{symbol}'.")
    close_series = df_raw["Close"].squeeze()          # ensure 1‑D Series
    df = (
        pd.DataFrame({"ds": df_raw.index, "y": close_series})
        .dropna()
        .reset_index(drop=True)
    )
    return df


# ---------- 2. XGBoost forecasting ----------
def xgboost_forecast(df: pd.DataFrame):
    """
    Fit an XGBoost regressor on lag features and
    forecast the next 7 daily prices.
    Returns tuple: ('XGBoost', forecast_dataframe)
    """
    df = df.copy()

    # create 7 lag features
    for lag in range(1, 8):
        df[f"lag_{lag}"] = df["y"].shift(lag)

    df.dropna(inplace=True)

    X = df[[f"lag_{i}" for i in range(1, 8)]]
    y = df["y"]

    # train‑test split: keep last 7 rows for validation/prediction seed
    split = len(X) - HORIZON
    model = XGBRegressor(n_estimators=100, max_depth=3, objective="reg:squarederror")
    model.fit(X.iloc[:split], y.iloc[:split])

    # rolling prediction for HORIZON days
    last_row = X.iloc[-1].values.reshape(1, -1)
    preds = []
    for _ in range(HORIZON):
        next_pred = model.predict(last_row)[0]
        preds.append(next_pred)
        # roll lags and insert new prediction at the end
        last_row = np.roll(last_row, -1)
        last_row[0, -1] = next_pred

    future_dates = pd.date_range(
        df["ds"].iloc[-1] + pd.Timedelta(days=1), periods=HORIZON
    )
    fcst = pd.DataFrame({"ds": future_dates, "y": preds})

    return "XGBoost", fcst
