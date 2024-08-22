import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to categorize BMI
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit interface
def main():
    st.title("BMI Tracker App")
    
    # Input fields
    weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
    height = st.number_input("Enter your height (m):", min_value=0.0, format="%.2f")
    
    # Calculate BMI
    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            
            st.write(f"Your BMI is: **{bmi:.2f}**")
            st.write(f"Category: **{category}**")
        else:
            st.write("Please enter a valid height.")

if __name__ == "__main__":
    main()


