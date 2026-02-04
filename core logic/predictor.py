from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import datetime

app = Flask(__name__, static_folder="frontend", static_url_path="")
CORS(app)  # 🔥 VERY IMPORTANT

USD_TO_INR = 83  # approx

# ------------------------
# Frontend route
# ------------------------
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


# ------------------------
# Prediction API
# ------------------------
@app.route("/api/predict", methods=["GET"])
def predict():
    try:
        # frontend se USD price bhej sakta hai
        usd_price = request.args.get("price", type=float)

        # fallback (Tesla current approx)
        if not usd_price:
            usd_price = 421.84

        change_percent = 0.34 / 100  # 0.34%
        predicted_usd = usd_price * (1 + change_percent)

        response = {
            "base_usd": round(usd_price, 2),
            "base_inr": round(usd_price * USD_TO_INR, 2),
            "predicted_usd": round(predicted_usd, 2),
            "predicted_inr": round(predicted_usd * USD_TO_INR, 2),
            "change_percent": 0.34,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M IST")
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "error": "Prediction failed",
            "details": str(e)
        }), 500


# ------------------------
# Run server
# ------------------------
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
