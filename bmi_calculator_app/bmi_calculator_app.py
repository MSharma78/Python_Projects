import streamlit as st

"""
BMI Calculator App using Streamlit
Developed by Meghna
Takes user weight and height, calculates BMI, categorizes it, and gives advice.
"""


name = st.text_input("Whats your good name?")
st.write(f"Welcome {name}...Let's check if you have a healthy weight!")

st.title("BMI Calculator ⚖️")
st.write("Enter your weight in kgs and height in feet and inches:")

# User input
weight_input = st.text_input("Your weight (kg)")
feet_input = st.text_input("Height (feet)")
inches_input = st.text_input("Height (inches)")

if weight_input and feet_input and inches_input:
    try:
        weight = float(weight_input)
        feet = float(feet_input)
        inches = float(inches_input)

        # Validate non-zero positive values
        if weight <= 0 or feet < 0 or (feet == 0 and inches == 0):
            st.error("Please enter valid non-zero weight and height.")
        else:
            # Add a Calculate BMI button inside this block
            if st.button("Calculate BMI"):
                total_inches = (feet * 12) + inches
                heightInMeters = total_inches * 0.0254
                BMI = weight / (heightInMeters ** 2)
                BMI = round(BMI, 2)

                st.write(f"Your BMI is: **{BMI}**")

                # Category logic
                if BMI <= 18.5:
                    st.warning("Category: Underweight")
                    st.info("📝Advice: Its good to consult a dietician!")
                    st.markdown("[Find a dietician near you](https://www.google.com/maps/search/dietician+near+me)", unsafe_allow_html = True)
                elif BMI <= 25:
                    st.success("Category: Normal weight")
                    st.info("✅Keep Going! You're doing great!")
                elif BMI <= 30:
                    st.warning("Category: Overweight")
                    st.info("📝Advice: 🏃‍➡️Regular exercise and mindful eating will help getting a healthy weight")
                else:
                    st.error("Category: Obese")
                    st.info("⚠️Advice: Its not a bad idea to consult a doctor or nutritionist for personalized health plans")
                    st.markdown("[Find a nutritionist near you](https://www.google.com/maps/search/weight+management+clinic+near+me)", unsafe_allow_html=True)

    except ValueError:
        st.error("Please enter valid numbers only.")
