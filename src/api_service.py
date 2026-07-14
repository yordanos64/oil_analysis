from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Permits cross-origin resource tracking from the React frontend

# Dynamic relative path checking to find your original data asset
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/BrentOilPrices.csv')

def load_processed_data():
    """Loads historical prices and filters down context for dashboard tracking."""
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame() # Return fallback empty structural context
    df = pd.read_csv(DATA_PATH)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')
    df = df.sort_values('Date').reset_index(drop=True)
    # Return last 500 trading sessions to optimize browser chart rendering speed
    return df.tail(500)

@app.route('/api/metrics', methods=['GET'])
def get_oil_metrics():
    """Serves time series pricing vectors and hardcoded mock change point markers."""
    df = load_processed_data()
    if df.empty:
        return jsonify({"error": "Data reference not available"}), 404
    
    # Format database rows into a clear JSON list of dictionaries
    chart_data = []
    for _, row in df.iterrows():
        chart_data.append({
            "date": row['Date'].strftime('%Y-%m-%d'),
            "price": float(row['Price'])
        })
        
    response_payload = {
        "series": chart_data,
        "structural_break_points": [
            {"date": "2020-03-11", "label": "COVID-19 Shock", "pre_mean": 62.0, "post_mean": 31.0},
            {"date": "2014-11-27", "label": "OPEC Supply Shift", "pre_mean": 102.0, "post_mean": 48.0}
        ]
    }
    return jsonify(response_payload)

if __name__ == '__main__':
    # Execute the localized runtime engine pipeline on micro port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
