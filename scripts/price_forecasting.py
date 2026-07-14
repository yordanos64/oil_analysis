import pandas as pd
import numpy as np
import os
from statsmodels.tsa.arima.model import ARIMA

def generate_oil_forecasts():
    """Builds a predictive forecasting pipeline for Brent oil future trends."""
    data_path = os.path.join(os.path.dirname(__file__), '../data/BrentOilPrices.csv')
    
    if not os.path.exists(data_path):
        print("Data file reference not found.")
        return
        
    # Load and clean baseline data
    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')
    df = df.sort_values('Date').reset_index(drop=True)
    
    # Use recent historical data post-COVID change point to train the model
    recent_data = df[df['Date'].dt.year >= 2020]['Price'].values
    
    # Initialize and fit a baseline ARIMA model (order parameters p,d,q)
    # p=1 (autoregressive), d=1 (differencing for stationarity), q=1 (moving average)
    model = ARIMA(recent_data, order=(1, 1, 1))
    model_fit = model.fit()
    
    # Forecast the next 30 operational trading days
    forecast_steps = 30
    forecast_output = model_fit.forecast(steps=forecast_steps)
    
    print("\n--- Birhan Energies: 30-Day Brent Oil Price Forecast ---")
    for day, price in enumerate(forecast_output, 1):
        print(f"Day {day:02d} Projected Price: ${price:.2f} USD/Barrel")

if __name__ == '__main__':
    generate_oil_forecasts()
