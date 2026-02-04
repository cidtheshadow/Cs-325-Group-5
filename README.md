🚀 Tesla Stock Price Prediction System

A clean, minimal, and data-driven web application that predicts short-term Tesla stock price movement using real-time market data and statistical indicators.

Built with ❤️ using Python, Flask, and live financial APIs.

✨ What This Project Does

Fetches real-time Tesla (TSLA) stock data

Analyzes historical trends using moving averages & volatility

Predicts expected price movement

Displays results through a simple web interface

Generates data suitable for academic reports & demos

This project is designed for learning, experimentation, and academic presentation.

🧠 How It Works

Live stock data is fetched from Yahoo Finance

Key indicators are calculated:

20-day Simple Moving Average (SMA)

50-day Simple Moving Average (SMA)

Recent volatility

A lightweight prediction logic estimates:

Expected percentage change

Predicted price

Results are returned via a Flask API and rendered on the frontend

⚠️ Note: This is not financial advice — it’s an educational project.

🛠 Core Technologies Used

Python 3

Flask – backend & API

yfinance – stock market data

NumPy – numerical analysis

HTML, CSS, JavaScript – frontend

REST API architecture

📁 Project Structure
project/
│
├── app.py                  # Main Flask application
├── templates/
│   ├── index.html          # Main UI
│   └── faq.html            # FAQ & team details
├── myenv/                  # Virtual environment
└── README.md               # You are here 👀

⚙️ How To Run Locally
# Activate virtual environment
source myenv/bin/activate

# Install dependencies
pip install flask flask-cors yfinance numpy

# Run the app
python app.py


Then open 👉 http://127.0.0.1:5000

📊 Sample Output (API)
{
  "base_price_usd": 414.32,
  "current_price_inr": 34388.56,
  "predicted_price_inr": 34474.53,
  "expected_change_percent": 0.25,
  "time": "2026-02-04 21:09 IST"
}

📌 Key Learnings

Real-time API integration

Backend-frontend communication

Handling live data failures gracefully

Applying financial concepts programmatically

Debugging real production-style errors

🔮 Future Scope

Machine Learning based prediction models

Support for multiple stocks

Interactive charts & dashboards

Improved prediction accuracy

Cloud deployment

👤 Author

Tanush Singla (Team Franx)
Diploma Student | Tech & AI Enthusiast
Built as part of academic & self-learning journey 🚀

📎 Disclaimer

This project is for educational purposes only.
It does not provide investment advice or guarantee accuracy.
