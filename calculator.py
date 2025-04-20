
# Calculator in pyrhon
# prompt: build a calculator which takes input from the user, beside basic functionality include modulus, floor division, Exponentiation

import streamlit as st

st.set_page_config(page_title="Python Calculator", page_icon="🧮")

st.title("🧮 Python Calculator")
st.markdown("This calculator supports `+`, `-`, `*`, `/`, `%`, `//`, `**` operations.")

# Input fields
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Operation selection
operation = st.selectbox("Choose an operation:", ['+', '-', '*', '/', '%', '//', '**'])

if st.button("Calculate"):
    result = None
    error = None

    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                error = "🚫 Error: Division by zero."
        elif operation == '%':
            result = num1 % num2
        elif operation == '**':
            result = num1 ** num2
        elif operation == '//':
            if num2 != 0:
                result = num1 // num2
            else:
                error = "🚫 Error: Division by zero."
    except:
        error = "⚠️ Unexpected error occurred."

    if error:
        st.error(error)
    else:
        st.success(f"✅ Result: {result}")



