import streamlit as st

# Unit conversion factors
conversion_factors = {
    "Metre": {"Centimetre": 100, "Kilometre": 0.001, "Inch": 39.37, "Foot": 3.281},
    "Centimetre": {"Metre": 0.01, "Kilometre": 0.00001, "Inch": 0.3937, "Foot": 0.03281},
    "Kilometre": {"Metre": 1000, "Centimetre": 100000, "Inch": 39370, "Foot": 3281},
    "Inch": {"Metre": 0.0254, "Centimetre": 2.54, "Kilometre": 0.0000254, "Foot": 0.0833},
    "Foot": {"Metre": 0.3048, "Centimetre": 30.48, "Kilometre": 0.0003048, "Inch": 12},
}

# Streamlit UI
st.title("⌛Unit Converter")
st.write("⌘Convert between different length units using Python and Streamlit.")

# Dropdowns for unit selection
unit_type = st.selectbox("Select Measurement Type", ["Length" ,"Weight" , "Height"])
from_unit = st.selectbox("From Unit", list(conversion_factors.keys()))
to_unit = st.selectbox("To Unit", list(conversion_factors[from_unit].keys()))

# Input value
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Conversion Calculation
if from_unit and to_unit:
    result = value * conversion_factors[from_unit][to_unit]
    st.write(f"### {value} {from_unit} = {result:.2f} {to_unit}")

    # Show conversion formula
    st.info(f"Formula: Multiply the {from_unit} value by {conversion_factors[from_unit][to_unit]}")

st.markdown("<div class= 'footer'>🙌created by Umm-E-Habiba ✌</div>", unsafe_allow_html=True)