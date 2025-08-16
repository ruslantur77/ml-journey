from fastapi import FastAPI, HTTPException
from prophet import Prophet
import joblib, datetime

app = FastAPI()
model = joblib.load('week1-day6-prophet.pkl')

@app.get('/predict')
def predict(days: int =30):
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    return forecast[['ds','yhat']].tail(days).to_dict(orient='records')

@app.get('/health')
def health():
    return {'status': 'ok'}