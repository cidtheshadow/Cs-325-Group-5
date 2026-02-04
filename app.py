from flask import Flask, render_template, jsonify
from datetime import datetime
import yfinance as yf
import numpy as np

app = Flask(__name__)

USD_TO_INR = 83.0  # demo-safe rate

# ================== MODEL ==================
class TeslaPredictor:
    def __init__(self):
        self.ticker = "TSLA"

    def get_stock_data(self, period="6mo"):
        try:
            stock = yf.Ticker(self.ticker)
            data = stock.history(period=period)

            # 🔥 SAFETY CHECK
            if data is None or data.empty:
                return None

            return data["Close"]

        except Exception as e:
            print("yfinance error:", e)
            return None

    def calculate_features(self, prices):
        prices_list = prices.values

        sma_20 = [
            np.mean(prices_list[i - 20 : i])
            for i in range(20, len(prices_list))
        ]

        sma_50 = prices.rolling(window=50).mean()
        sma_50 = sma_50.tail(len(sma_20)).values

        return np.array(sma_20), np.array(sma_50)

    def predict_price(self):
        prices = self.get_stock_data()

        # 🚨 fallback so frontend never breaks
        if prices is None or len(prices) < 60:
            return {
                "current_price": 0,
                "predicted_price": 0,
                "usd_price": 0,
                "predicted_usd_price": 0,
                "change_percent": 0,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M IST"),
            }

        sma_20, sma_50 = self.calculate_features(prices)

        last_price = prices.iloc[-1]
        last_sma20 = sma_20[-1]
        last_sma50 = sma_50[-1]

        trend_direction = 1 if last_sma20 > last_sma50 else -1
        trend_strength = min(abs(last_sma20 - last_sma50) / last_sma50, 0.01)

        daily_volatility = np.std(
            prices.pct_change().dropna().tail(20)
        )

        predicted_change = (
            trend_direction * trend_strength * 0.6
            + daily_volatility * 0.4
        )

        predicted_change = np.clip(predicted_change, -0.025, 0.025)
        predicted_price = last_price * (1 + predicted_change)

        return {
            # 🔑 frontend-safe keys
            "current_price": round(last_price * USD_TO_INR, 2),
            "predicted_price": round(predicted_price * USD_TO_INR, 2),

            "usd_price": round(float(last_price), 2),
            "predicted_usd_price": round(float(predicted_price), 2),

            "change_percent": round(predicted_change * 100, 2),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M IST"),
        }

# ================== ROUTES ==================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/api/predict")
def api_predict():
    predictor = TeslaPredictor()
    return jsonify(predictor.predict_price())

# ================== RUN ==================
if __name__ == "__main__":
    app.run(debug=True)
