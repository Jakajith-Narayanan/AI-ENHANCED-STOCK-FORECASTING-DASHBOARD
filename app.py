from flask import Flask, render_template, request, jsonify
#from forecasting import fetch_prices, arima_forecast
#from forecasting import fetch_prices, arima_forecast
from forecasting import fetch_prices, xgboost_forecast

from sentiment_analysis import extract_pdf_text, vader_sentiment, gpt_summary, extract_company_name
from decision import recommend
import tempfile, os, numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
  try: 
    # ------- 1. Receive inputs -------
    symbol = request.form['symbol'].upper()
    uploaded = request.files['pdf']

    # save uploaded PDF to a temp file & immediately release handle (Win⁖safe)
    tmp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    uploaded.save(tmp_pdf.name)
    tmp_pdf.close()

    # ------- 2. Fetch prices & forecast (ARIMA only) -------
    df = fetch_prices(symbol)
    # best_model, fcst_stat = arima_forecast(df)        # 7⁐day forecast
    best_model, fcst_stat = xgboost_forecast(df)       # 7⁐day forecast
    ensemble_fcst = fcst_stat['y'].values              # XGBoost predictions
    forecast_dates = fcst_stat['ds'].astype(str).tolist()

    # RMSE on the last 7 actual closes vs forecast
    actual_last7 = df['y'].iloc[-7:].values
    rmse = float(np.sqrt(np.mean((actual_last7 - ensemble_fcst) ** 2)))

    trend_dir = 'Up' if ensemble_fcst[-1] > df['y'].iloc[-1] else 'Down'

    # ------- 3. Sentiment & GPT summary -------
    pdf_text = extract_pdf_text(tmp_pdf.name)
    sentiment = vader_sentiment(pdf_text)
    summary = gpt_summary(pdf_text)
    company = extract_company_name(pdf_text)

    # ------- 4. Final recommendation -------
    decision, score = recommend(trend_dir, sentiment)

    # cleanup temp file
    os.unlink(tmp_pdf.name)

    # ------- 5. Return JSON -------
    return jsonify({
        'forecast_dates': forecast_dates,
        'forecast_values': ensemble_fcst.tolist(),
        'trend_dir': trend_dir,
        'best_model': best_model,
        'sentiment': sentiment,
        'gpt_summary': summary,
        'decision': decision,
        'score': round(score, 2),
        'rmse': round(rmse, 4),
        'company': company
    })

  except ValueError as e:
        return jsonify({"error": str(e)})
  except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"})    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
