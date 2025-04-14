import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import plotly.express as px
from PIL import Image
from io import BytesIO

# API Key (sign up at https://openweathermap.org/api)
API_KEY = "9a641e963d4d88b86f9f6e1e5e83d3c0"
BASE_URL = "https://api.openweathermap.org/data/2.5/"

# App configuration
st.set_page_config(page_title="Weather Forecast", page_icon="🌤️", layout="wide")

def get_wind_direction(degrees):
    """Convert wind degrees to compass direction""" # 16 possible directions
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return directions[int((degrees % 360) / 22.5)]

def display_current_weather(data, units):
    """Display current weather conditions"""
    current = data["current"]
    location = data["location"]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader(f"{location['name']}, {location.get('country', '')}")
        st.caption(datetime.fromtimestamp(current["dt"]).strftime("%A, %B %d, %Y %H:%M"))
        
        # Weather icon
        icon_code = current["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@4x.png"
        icon_response = requests.get(icon_url)
        icon_img = Image.open(BytesIO(icon_response.content))
        st.image(icon_img, width=150)
        
    with col2:
        st.metric("Temperature", f"{current['main']['temp']}°{'C' if units == 'metric' else 'F'}")
        st.caption(f"Feels like {current['main']['feels_like']}°")
        
        st.write(f"**Humidity:** {current['main']['humidity']}%")
        st.write(f"**Pressure:** {current['main']['pressure']} hPa")
        
    with col3:
        st.write(f"**Condition:** {current['weather'][0]['description'].title()}")
        st.write(f"**Wind:** {current['wind']['speed']} {'m/s' if units == 'metric' else 'mph'} {get_wind_direction(current['wind']['deg'])}")
        st.write(f"**Visibility:** {current.get('visibility', 'N/A')/1000 if current.get('visibility') else 'N/A'} km")
        
        sunrise = datetime.fromtimestamp(current["sys"]["sunrise"]).strftime("%H:%M")
        sunset = datetime.fromtimestamp(current["sys"]["sunset"]).strftime("%H:%M")
        st.write(f"**Sunrise:** {sunrise} | **Sunset:** {sunset}")

def display_forecast(data, units):
    """Display 5-day forecast with charts"""
    try:
        forecast_list = data["forecast"]["list"]
        
        # Process forecast data
        forecast_data = []
        for item in forecast_list:
            forecast_data.append({
                "datetime": datetime.fromtimestamp(item["dt"]),
                "date": datetime.fromtimestamp(item["dt"]).strftime("%a, %b %d"),
                "time": datetime.fromtimestamp(item["dt"]).strftime("%H:%M"),
                "temp": item["main"]["temp"],
                "feels_like": item["main"]["feels_like"],
                "humidity": item["main"]["humidity"],
                "pressure": item["main"]["pressure"],
                "wind_speed": item["wind"]["speed"],
                "weather": item["weather"][0]["main"],
                "description": item["weather"][0]["description"],
                "icon": item["weather"][0]["icon"],
                "pop": item.get("pop", 0) * 100  # Probability of precipitation
            })
        
        df = pd.DataFrame(forecast_data)
        
        # Daily forecast
        st.subheader("Forecast")
        
        # Group by day
        daily_df = df.copy()
        daily_df["date"] = pd.to_datetime(daily_df["datetime"]).dt.date
        daily_agg = daily_df.groupby("date").agg({
            "temp": ["min", "max"],
            "humidity": "mean",
            "weather": lambda x: x.mode()[0],
            "icon": lambda x: x.mode()[0],
            "pop": "max"
        }).reset_index()
        
        daily_agg.columns = ["Date", "Min Temp", "Max Temp", "Humidity", "Weather", "Icon", "Precipitation"]
        
        # Display forecast cards - now dynamic based on available data
        num_days = min(5, len(daily_agg))  # Ensure we don't exceed available data
        cols = st.columns(num_days)
        
        for i in range(num_days):
            row = daily_agg.iloc[i]
            with cols[i]:
                st.subheader(row["Date"].strftime("%a"))
                icon_url = f"http://openweathermap.org/img/wn/{row['Icon']}.png"
                st.image(icon_url, width=50)
                st.write(f"{row['Weather']}")
                st.write(f"↑ {row['Max Temp']}° | ↓ {row['Min Temp']}°")
                st.write(f"💧 {int(row['Humidity'])}%")
                st.write(f"🌧️ {int(row['Precipitation'])}%")
        
        # Temperature chart
        if len(df) > 0:
            st.subheader("Temperature Forecast")
            fig = px.line(df, x="datetime", y="temp", 
                        labels={"temp": f"Temperature (°{'C' if units == 'metric' else 'F'})", "datetime": "Time"},
                        title="Temperature Forecast")
            st.plotly_chart(fig, use_container_width=True)
            
            # Additional metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Highest Temperature", f"{df['temp'].max()}°")
            with col2:
                st.metric("Lowest Temperature", f"{df['temp'].min()}°")
            with col3:
                st.metric("Average Humidity", f"{df['humidity'].mean():.1f}%")
                
    except Exception as e:
        st.error(f"Error displaying forecast: {str(e)}")

def get_weather_data(location, units="metric"):
    """Fetch weather data from OpenWeatherMap API"""
    try:
        # Geocoding API to get coordinates
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={API_KEY}"
        geo_response = requests.get(geo_url).json()
        
        if not geo_response:
            st.error("Location not found. Please try another city.")
            return None
            
        lat = geo_response[0]["lat"]
        lon = geo_response[0]["lon"]
        
        # Current weather
        current_url = f"{BASE_URL}weather?lat={lat}&lon={lon}&units={units}&appid={API_KEY}"
        current_data = requests.get(current_url).json()
        
        # 5-day forecast
        forecast_url = f"{BASE_URL}forecast?lat={lat}&lon={lon}&units={units}&appid={API_KEY}"
        forecast_data = requests.get(forecast_url).json()
        
        return {
            "current": current_data,
            "forecast": forecast_data,
            "location": geo_response[0]
        }
    except Exception as e:
        st.error(f"Error fetching weather data: {str(e)}")
        return None

def main():
    st.title("🌦️ Advanced Weather Forecast")
    
    # Sidebar controls
    with st.sidebar:
        st.header("Settings")
        location = st.text_input("Enter city name", "London")
        units = st.radio("Units", ("metric", "imperial"), index=0, 
                        format_func=lambda x: "°C, m/s" if x == "metric" else "°F, mph")
        st.markdown(f"[Get API Key](https://home.openweathermap.org/users/sign_up)")
    
    if st.sidebar.button("Get Weather"):
        with st.spinner("Fetching weather data..."):
            weather_data = get_weather_data(location, units)
            
            if weather_data:
                display_current_weather(weather_data, units)
                st.divider() # make a horizontal line
                display_forecast(weather_data, units)

if __name__ == "__main__":
    main()