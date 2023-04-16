import streamlit as st
import pandas as pd

# Define the layout of your app
st.title("Budget App")

# Create input forms
col1, col2 = st.columns(2)
monthly_income = col1.number_input("Monthly Income", min_value=0, step=50)
expenses = col2.number_input("Monthly Expenses", min_value=0, step=50)

# Add data processing functionality
savings = monthly_income - expenses
if savings < 0:
    st.warning("Your expenses are greater than your income. You need to cut back on expenses.")
else:
    st.success("You are saving ${} every month.".format(savings))

# Create output visuals
st.header("Monthly Expenses")

# Get user input for expense names and amounts
num_expenses = st.number_input("How many expenses do you have?", min_value=0, step=1)
expense_names = []
expense_amounts = []
for i in range(num_expenses):
    expense_names.append(st.text_input(f"Expense {i+1} name"))
    expense_amounts.append(st.number_input(f"Expense {i+1} amount", min_value=0, step=50))

# Create a DataFrame from the expense data
expense_data = pd.DataFrame({'Expense Name': expense_names, 'Amount': expense_amounts}, index=range(1, num_expenses+1))

# Calculate the total of all expenses
total_expenses = pd.DataFrame({'Expense Name': 'Total', 'Amount': expense_data['Amount'].sum()}, index=[0])

# Concatenate the total row with the original DataFrame
expense_data = pd.concat([expense_data, total_expenses], ignore_index=True)

# Display the expense data in a table
st.table(expense_data)


# Deploy your app
# Use the command `streamlit run app.py` to run your app locally
# You can also deploy your app to hosting services like Heroku or Streamlit Sharing


#Todo:
"""Get the table to start from '1' instead of '0' """