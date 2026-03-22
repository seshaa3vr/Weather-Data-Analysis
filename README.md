# 🌤️ Weather Data Analysis Dashboard

A simple, interactive web application built with [Streamlit](https://streamlit.io/) for exploring weather datasets, visualizing trends, and predicting future temperatures using a Linear Regression model.

## 🚀 Features

- **Data Exploration**: View the raw weather dataset directly within the app.
- **Key Insights**: Automatically calculates Maximum Temperature, Average Rainfall, and Highest Humidity.
- **Interactive Visualizations**: Includes interactive line charts for Temperature, Rainfall, and Humidity trends using `plotly.express`.
- **Temperature Prediction**: Uses a Scikit-Learn `LinearRegression` model trained on historical data to predict the next day's temperature.

## 📋 Prerequisites

Ensure you have Python 3.7+ installed on your system.

## 🛠️ Installation

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd "d:\projects\Weather Data Analysis"
   ```
3. Install the required Python packages:
   ```bash
   pip install streamlit pandas plotly scikit-learn
   ```

## 💻 Usage

To run the application locally:

1. Execute the following command in your terminal:
   ```bash
   streamlit run app.py
   ```
2. The application will start and automatically open in your default web browser at `http://localhost:8501`.

## 📁 Project Structure

- `app.py`: The main Streamlit application containing the UI, data processing, and prediction logic.
- `weather_data.csv`: The dataset containing historical weather records (Date, Temperature, Rainfall, Humidity). If you want to use your own data, simply replace this file with your own dataset keeping the same column headers.

## 🧠 Machine Learning Model

The app uses a simple `LinearRegression` model from `scikit-learn` to predict the next day's temperature. It trains on the historical relationship between the day of the year and the temperature.
