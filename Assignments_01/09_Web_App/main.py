# Another country info app with more styling and a little bit complex code

import streamlit as st
import requests

# Set page config
st.set_page_config(
    page_title="Country Information Cards",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to fetch country data
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_country_data():
    try:
        response = requests.get("https://restcountries.com/v3.1/all")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

# Function to display country card
def display_country_card(country):
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if 'flags' in country and 'png' in country['flags']:
            st.image(country['flags']['png'], width=200)
        else:
            st.warning("No flag available")
    
    with col2:
        st.subheader(country.get('name', {}).get('common', 'Unknown Country'))
        
        # Basic info
        if 'capital' in country:
            st.markdown(f"**Capital:** {', '.join(country['capital'])}")
        if 'region' in country:
            st.markdown(f"**Region:** {country['region']}")
        if 'subregion' in country:
            st.markdown(f"**Subregion:** {country['subregion']}")
        
        # Population with formatting
        if 'population' in country:
            population = "{:,}".format(country['population'])
            st.markdown(f"**Population:** {population}")
        
        # Languages
        if 'languages' in country:
            languages = ', '.join(country['languages'].values())
            st.markdown(f"**Languages:** {languages}")
        
        # Currency
        if 'currencies' in country:
            currencies = []
            for code, info in country['currencies'].items():
                currencies.append(f"{info['name']} ({info['symbol'] if 'symbol' in info else '?'})")
            st.markdown(f"**Currencies:** {', '.join(currencies)}")

# Main app
def main():
    st.title("🌍 Country Information Cards")
    st.markdown("Fetching live data from [REST Countries API](https://restcountries.com/)")
    
    # Get country data
    countries = get_country_data()
    
    if countries:
        # Create search and filter options
        st.sidebar.header("Filters")
        
        # Search by name
        search_query = st.sidebar.text_input("Search by country name")
        
        # Filter by region
        regions = sorted(set([country.get('region', 'Unknown') for country in countries]))
        selected_region = st.sidebar.selectbox("Filter by region", ["All"] + regions)
        
        # Filter by population
        min_population = st.sidebar.slider(
            "Minimum population (millions)",
            min_value=0,
            max_value=1500,
            value=0
        ) * 1000000
        
        # Apply filters
        filtered_countries = []
        for country in countries:
            name = country.get('name', {}).get('common', '').lower()
            region = country.get('region', '')
            population = country.get('population', 0)
            
            name_match = not search_query or search_query.lower() in name
            region_match = selected_region == "All" or region == selected_region
            population_match = population >= min_population
            
            if name_match and region_match and population_match:
                filtered_countries.append(country)
        
        st.sidebar.markdown(f"**{len(filtered_countries)}** countries match your filters")
        
        # Display country cards
        if filtered_countries:
            # Sort options
            sort_option = st.selectbox(
                "Sort by",
                ["Name (A-Z)", "Name (Z-A)", "Population (High-Low)", "Population (Low-High)"]
            )
            
            # Apply sorting
            if sort_option == "Name (A-Z)":
                filtered_countries.sort(key=lambda x: x.get('name', {}).get('common', ''))
            elif sort_option == "Name (Z-A)":
                filtered_countries.sort(key=lambda x: x.get('name', {}).get('common', ''), reverse=True)
            elif sort_option == "Population (High-Low)":
                filtered_countries.sort(key=lambda x: x.get('population', 0), reverse=True)
            elif sort_option == "Population (Low-High)":
                filtered_countries.sort(key=lambda x: x.get('population', 0))
            
            # Pagination
            items_per_page = 10
            page = st.number_input("Page", min_value=1, max_value=(len(filtered_countries) // items_per_page) + 1, value=1)
            
            start_idx = (page - 1) * items_per_page
            end_idx = start_idx + items_per_page
            
            for country in filtered_countries[start_idx:end_idx]:
                with st.expander(f"{country.get('name', {}).get('common', 'Unknown Country')}", expanded=True):
                    display_country_card(country)
                st.markdown("---")
        else:
            st.warning("No countries match your filters")
    else:
        st.error("Failed to load country data. Please try again later.")
    st.sidebar.markdown("---")    
    st.sidebar.markdown("""
    <style>
    .glow {
    font-size: 16px;
    color: #fff;
    text-align: center;
    animation: glow 1.5s ease-in-out infinite alternate;
    }

    @keyframes glow {
    from {
        text-shadow: 0 0 10px #e91e63, 0 0 20px #e91e63;
    }
    to {
        text-shadow: 0 0 20px #673ab7, 0 0 30px #673ab7;
    }
    }
    </style>

    <div class="glow"> Made with ❤️ by Areeba Zafar</div>
    """, unsafe_allow_html=True)
 

if __name__ == "__main__":
    main()