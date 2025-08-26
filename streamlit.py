import streamlit as st
st.title("Hello GeeksForGeeks !!!")

st.header("This is a header") 
st.subheader("This is a subheader")

st.text("Hello GeeksForGeeks!!!")

st.markdown("### This is a markdown")

st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))

from PIL import Image  # Import Image from Pillow
img = Image.open("Streamlit-Output.png") # Open the image file
st.image(img, width=200) # Display the image with a specified width

# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    st.text("Showing the widget")
# When the checkbox is unchecked, nothing is displayed.

# Create a radio button to select gender
status = st.radio("Select Gender:", ['Male', 'Female'])

# Display the selected option using success message
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

# Create a dropdown menu for selecting a hobby
hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])

# Display the selected hobby
st.write("Your hobby is:", hobby)

# Create a multiselect box for choosing hobbies
hobbies = st.multiselect("Select Your Hobbies:", ['Dancing', 'Reading', 'Sports'])

# Display the number of selected hobbies
st.write("You selected", len(hobbies), "hobbies")

# A simple button that does nothing
st.button("Click Me")

# A button that displays text when clicked
if st.button("About"):
    st.text("Welcome to GeeksForGeeks!")

# Create a text input box with a default placeholder
name = st.text_input("Enter your name", "Type here...")

# Display the name after clicking the Submit button
if st.button("Submit"):
    result = name.title()  # Capitalize the first letter of each word
    st.success(result)

# Create a slider to select a level between 1 and 5
level = st.slider("Choose a level", min_value=1, max_value=5)

# Display the selected level
st.write(f"Selected level: {level}")

import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Input: Weight in kilograms
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")

# Input: Height format selection
height_unit = st.radio("Select your height unit:", ['Centimeters', 'Meters', 'Feet'])

# Input: Height value based on selected unit
height = st.number_input(f"Enter your height ({height_unit.lower()}):", min_value=0.0, format="%.2f")

# Calculate BMI when button is pressed
if st.button("Calculate BMI"):
    try:
        # Convert height to meters based on selected unit
        if height_unit == 'Centimeters':
            height_m = height / 100
        elif height_unit == 'Feet':
            height_m = height / 3.28
        else:
            height_m = height

        # Prevent division by zero
        if height_m <= 0:
            st.error("Height must be greater than zero.")
        else:
            bmi = weight / (height_m ** 2)
            st.success(f"Your BMI is {bmi:.2f}")

            # BMI interpretation
            if bmi < 16:
                st.error("You are Extremely Underweight")
            elif 16 <= bmi < 18.5:
                st.warning("You are Underweight")
            elif 18.5 <= bmi < 25:
                st.success("You are Healthy")
            elif 25 <= bmi < 30:
                st.warning("You are Overweight")
            else:
                st.error("You are Extremely Overweight")
    except:
        st.error("Please enter valid numeric values.")


st.write("Hello, **World!** :wave:")
st.write("# This is a header")

import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'column 1': [1, 2, 3, 4],
    'column 2': [10, 20, 30, 40]
})

st.write("Here is a DataFrame:", df)

import streamlit as st
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
st.write(fig)

st.write("My favorite equation is $$e^{i\pi} + 1 = 0$$")