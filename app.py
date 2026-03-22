import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

# Set page config
st.set_page_config(page_title="Weather Data Analysis", layout="wide")

st.title("🌤️ Weather Data Analysis Dashboard")
st.write("Welcome to the Weather Data Analysis app. This dashboard allows you to explore weather trends and predict future temperatures.")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("weather_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    # Optional clean-up
    df = df.dropna()
    df['DayOfYear'] = df['Date'].dt.dayofyear
    df['Month'] = df['Date'].dt.month
    return df

try:
    data = load_data()
except FileNotFoundError:
    st.error("Error: `weather_data.csv` could not be found.")
    st.stop()

# Display raw data
with st.expander("View Raw Data"):
    st.write(data)

# Insights
st.header("📊 Key Insights")
col1, col2, col3 = st.columns(3)

max_temp = data['Temperature'].max()
avg_rain = data['Rainfall'].mean()
high_humidity = data['Humidity'].max()

col1.metric("Maximum Temperature", f"{max_temp} °C")
col2.metric("Average Rainfall", f"{avg_rain:.2f} mm")
col3.metric("Highest Humidity", f"{high_humidity} %")

st.divider()

# Visualizations
st.header("📈 Weather Trends")

tab1, tab2, tab3 = st.tabs(["Temperature", "Rainfall", "Humidity"])

with tab1:
    fig_temp = px.line(data, x='Date', y='Temperature', title="Temperature Over Time", markers=True)
    st.plotly_chart(fig_temp, use_container_width=True)

with tab2:
    fig_rain = px.line(data, x='Date', y='Rainfall', title="Rainfall Over Time", markers=True)
    st.plotly_chart(fig_rain, use_container_width=True)

with tab3:
    fig_hum = px.line(data, x='Date', y='Humidity', title="Humidity Over Time", markers=True)
    st.plotly_chart(fig_hum, use_container_width=True)

st.divider()

# Prediction Model
st.header("🤖 Temperature Prediction")
st.write("Using a simple Linear Regression model trained on historical data to predict the next day's temperature.")

# Prepare data for model
# We'll use DayOfYear as the feature to predict Temperature
X = data[['DayOfYear']]
y = data['Temperature']

model = LinearRegression()
model.fit(X, y)

# Predict next day
last_date = data['Date'].max()
next_date = last_date + pd.Timedelta(days=1)
next_day_of_year = next_date.dayofyear

# Need a 2D array for the prediction if X was a DataFrame. X is DataFrame since we used [['DayOfYear']]
next_temp_pred = model.predict(pd.DataFrame({'DayOfYear': [next_day_of_year]}))[0]

st.success(f"Predicted Temperature for {next_date.strftime('%Y-%m-%d')} is **{next_temp_pred:.2f} °C**")
