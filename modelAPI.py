from fastapi import FastAPI, HTTPException
from prophet import Prophet
import joblib
from datetime import datetime, timedelta
import pandas as pd

app = FastAPI()

# Load the Prophet model
model = joblib.load("./models/prophet_model.joblib")

@app.post("/predict/")
async def predict_co2_emission(start_date: str, end_date: str):
    try:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")

        date_range = pd.date_range(start=start_dt, end=end_dt, freq='H')
        future = pd.DataFrame(date_range, columns=['ds'])
        forecast = model.predict(future)

        # print(forecast)

        results = forecast[['ds', 'yhat']]
        results.rename(columns={'ds': 'Date', 'yhat': 'Predicted CO2 Emission'}, inplace=True)

        return results.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
