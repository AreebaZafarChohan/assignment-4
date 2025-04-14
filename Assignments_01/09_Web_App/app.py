# Web App - Country Information Cards

import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        response = requests.get(url, timeout=5)  # timeout added for safety
        if response.status_code == 200:
            data = response.json()
            country_data = data[0]
            name = country_data["name"]["common"]
            capital = country_data["capital"][0]
            population = country_data["population"]
            area = country_data["area"]
            currency = list(country_data["currencies"].keys())[0]
            region = country_data["region"]
            return name, capital, population, area, currency, region
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def main():
    st.title("🌍 Country Information App")
    
    country_name = st.text_input("Enter a country name:")
    
    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency, region = country_info
            st.subheader("Country Information")
            st.write(f"**Name:** {name}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**Population:** {population:,}")
            st.write(f"**Area:** {area:,} sq.km")
            st.write(f"**Currency:** {currency}")
            st.write(f"**Region:** {region}")
        else:
            st.error("❌ Error: Could not fetch country data. Please try another name.")

if __name__ == "__main__":
    main()
