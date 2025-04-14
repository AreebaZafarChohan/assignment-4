# Data driven app

import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Shop Sales Analyzer",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sample datasets
@st.cache_data
def load_sample_data():
    datasets = {
        "Mobile Shop": {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Samsung': [50, 60, 55, 70, 90, 120],
            'Apple': [40, 45, 50, 60, 80, 100],
            'Oppo': [20, 25, 30, 20, 25, 30],
            'Vivo': [10, 15, 20, 10, 15, 20],
            'Total_Sales': [120, 145, 155, 160, 210, 270],
            'Avg_Price': [28000, 29000, 29500, 31000, 32000, 35000]
        },
        "Grocery Store": {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Vegetables': [150, 160, 155, 170, 190, 220],
            'Fruits': [140, 145, 150, 160, 180, 200],
            'Dairy': [120, 125, 130, 120, 125, 130],
            'Snacks': [110, 115, 120, 110, 115, 120],
            'Total_Sales': [520, 545, 555, 560, 610, 670],
            'Avg_Bill': [580, 590, 595, 610, 620, 650]
        },
        "Makeup Store": {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Lipstick': [35, 40, 45, 50, 55, 70],
            'Foundation': [30, 35, 40, 45, 50, 60],
            'Eyeshadow': [25, 30, 35, 40, 45, 50],
            'Mascara': [20, 25, 30, 35, 40, 45],
            'Total_Sales': [110, 130, 150, 170, 190, 225],
            'Avg_Price': [1800, 1900, 1950, 2100, 2200, 2500]
        },
        "Book Store": {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Fiction': [45, 50, 55, 60, 65, 80],
            'Non-Fiction': [40, 45, 50, 55, 60, 70],
            'Children': [35, 40, 45, 50, 55, 60],
            'Educational': [30, 35, 40, 45, 50, 55],
            'Total_Sales': [150, 170, 190, 210, 230, 265],
            'Avg_Price': [1200, 1250, 1300, 1350, 1400, 1500]
        }
    }
    return datasets

def get_default_df(shop_type):
    datasets = load_sample_data()
    return pd.DataFrame(datasets[shop_type])

# Main app
def main():
    st.sidebar.title("Shop Analytics")
    
    # Data selection
    data_source = st.sidebar.radio("Data Source", ["Sample Data", "Upload Your Own"])
    
    if data_source == "Sample Data":
        shop_type = st.sidebar.selectbox("Select Shop Type", 
                                        ["Mobile Shop", "Grocery Store", "Makeup Store", "Book Store"])
        df = get_default_df(shop_type)
    else:
        uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel", type=['csv', 'xlsx'])
        if uploaded_file:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
        else:
            st.info("Please upload your data file to begin analysis")
            st.stop()
    
    app_mode = st.sidebar.radio("Select Analysis Type", 
                               ["Sales Dashboard", "Brand/Category Performance", "Price Analysis", "About"])
    
    if app_mode == "Sales Dashboard":
        show_dashboard(df)
    elif app_mode == "Brand/Category Performance":
        show_brand_performance(df)
    elif app_mode == "Price Analysis":
        show_price_analysis(df)
    elif app_mode == "About":
        show_about()

def show_dashboard(df):
    st.title("📊 Sales Dashboard")
    
    # Key metrics
    st.subheader("Performance Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"{df['Total_Sales'].sum()} Units")
    col2.metric("Best Month", f"{df.loc[df['Total_Sales'].idxmax(), 'Month']} ({df['Total_Sales'].max()} Units)")
    
    price_col = 'Avg_Price' if 'Avg_Price' in df.columns else 'Avg_Bill'
    col3.metric(f"Average {price_col.split('_')[-1]}", f"PKR-{df[price_col].mean():,.0f}")
    
    # Monthly sales trend
    st.subheader("Monthly Sales Trend")
    fig = px.line(df, x='Month', y='Total_Sales', markers=True,
                 title="Total Sales Growth Over Months")
    st.plotly_chart(fig, use_container_width=True)
    
    # Brand/Category comparison
    st.subheader("Category-wise Monthly Sales")
    categories = [col for col in df.columns if col not in ['Month', 'Total_Sales', 'Avg_Price', 'Avg_Bill']]
    fig = px.bar(df, x='Month', y=categories, barmode='group',
                title="Sales by Category Each Month")
    st.plotly_chart(fig, use_container_width=True)

def show_brand_performance(df):
    st.title("📈 Category Performance Analysis")
    
    categories = [col for col in df.columns if col not in ['Month', 'Total_Sales', 'Avg_Price', 'Avg_Bill']]
    selected_category = st.selectbox("Select Category", categories)
    
    # Category metrics
    st.subheader(f"{selected_category} Performance")
    col1, col2 = st.columns(2)
    col1.metric("Total Sales", f"{df[selected_category].sum()} Units")
    col2.metric("Market Share", 
               f"{round(df[selected_category].sum()/df['Total_Sales'].sum()*100)}%")
    
    # Category trend
    fig = px.line(df, x='Month', y=selected_category, markers=True,
                 title=f"{selected_category} Monthly Sales Trend")
    st.plotly_chart(fig, use_container_width=True)
    
    # Category contribution to total sales
    st.subheader("Category Contribution to Total Sales")
    category_totals = df[categories].sum()
    fig = px.pie(values=category_totals, names=category_totals.index,
                title="Overall Market Share by Category")
    st.plotly_chart(fig, use_container_width=True)

def show_price_analysis(df):
    st.title("💰 Price Analysis")
    
    price_col = 'Avg_Price' if 'Avg_Price' in df.columns else 'Avg_Bill'
    
    # Price vs Sales
    st.subheader("Price vs Sales Relationship")
    fig = px.scatter(df, x=price_col, y='Total_Sales', trendline="ols",
                   title=f"How {price_col.replace('_', ' ')} Affects Total Sales")
    st.plotly_chart(fig, use_container_width=True)
    
    # Price distribution
    st.subheader("Price Range Analysis")
    fig = px.box(df, y=price_col, title=f"Average {price_col.replace('_', ' ')} Distribution")
    st.plotly_chart(fig, use_container_width=True)
    
    # Price trend
    st.subheader("Monthly Price Trend")
    fig = px.line(df, x='Month', y=price_col, markers=True,
                 title=f"Average {price_col.replace('_', ' ')} Trend")
    st.plotly_chart(fig, use_container_width=True)

def show_about():
    st.title("About This App")
    
    st.markdown("""
    ## Shop Sales Analyzer
    
    This application helps shop owners analyze their sales performance across different categories.
    
    ### Features:
    - **Sales Dashboard**: Overall sales trends and performance
    - **Category Performance**: Compare different categories' sales
    - **Price Analysis**: Understand how pricing affects sales
    
    ### Default Datasets Included:
    - Mobile Shop
    - Grocery Store
    - Makeup Store
    - Book Store
    
    ### How to Use:
    1. Choose between sample data or upload your own
    2. Select analysis type from sidebar
    3. Explore different visualizations
    4. Make data-driven business decisions
    
    *Sample data represents 6 months of sales*
    """)

if __name__ == "__main__":
    main()