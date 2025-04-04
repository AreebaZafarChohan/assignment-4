import streamlit as st
import pandas as pd

# Function to calculate BMI
def calculate_bmi(weight, height):
    """BMI calculation formula"""
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Function to determine BMI category
def bmi_category(bmi):
    """Returns category & color based on BMI value"""
    if bmi < 18.5:
        return "Underweight 😔", "blue"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight 😊", "green"
    elif 25 <= bmi < 29.9:
        return "Overweight 😟", "orange"
    else:
        return "Obese 😢", "red"

# Ideal Weight Chart
ideal_weight_data = {
    "Height (cm)": [140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200],
    "Min Weight (kg)": [36, 39, 42, 45, 47, 50, 53, 56, 59, 62, 65, 69, 72],
    "Max Weight (kg)": [49, 53, 56, 60, 64, 68, 72, 76, 81, 85, 90, 95, 100]
}
ideal_weight_df = pd.DataFrame(ideal_weight_data)

# Streamlit App
def main():
    st.title("🩺 BMI Calculator with Ideal Weight Chart")
    st.write("Enter your height and weight to calculate your BMI.")

    # User Input
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, max_value=300.0, step=0.1)
    height = st.number_input("Enter your height (cm):", min_value=50.0, max_value=250.0, step=0.1)

    # Load previous data
    if "bmi_data" not in st.session_state:
        st.session_state.bmi_data = pd.DataFrame(columns=["Weight (kg)", "Height (cm)", "BMI", "Category"])

    if st.button("Calculate BMI"):
        if height > 0 and weight > 0:
            bmi = calculate_bmi(weight, height)
            category, color = bmi_category(bmi)

            # Display results
            st.success(f"**Your BMI:** {bmi} ({category})")
            st.markdown(f"<h3 style='color:{color};'>You are {category}</h3>", unsafe_allow_html=True)

            # Progress Bar
            st.progress(min(bmi / 40, 1.0))  # Normalize BMI on a scale of 0-40

            # Save data to session state (temporary storage)
            new_entry = pd.DataFrame([[weight, height, bmi, category]], columns=["Weight (kg)", "Height (cm)", "BMI", "Category"])
            st.session_state.bmi_data = pd.concat([st.session_state.bmi_data, new_entry], ignore_index=True)

        else:
            st.error("Please enter valid weight and height.")

    # Show BMI history
    if not st.session_state.bmi_data.empty:
        st.subheader("📊 BMI History")
        st.dataframe(st.session_state.bmi_data)

    # Show Ideal Weight Chart
    st.subheader("📏 Ideal Weight Chart (Based on Height)")
    st.table(ideal_weight_df)

if __name__ == "__main__":
    main()
