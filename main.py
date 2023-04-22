import streamlit as st
import pandas as pd
import os.path

# Define the layout of your app
st.title("Budget App")

# Create input forms
col1, col2 = st.columns(2)
monthly_income = col1.number_input("Monthly Income", min_value=0, step=50, key="monthly_income")
expenses = col2.number_input("Monthly Expenses", min_value=0, step=50, key="expenses")


# Add data processing functionality
if expenses > monthly_income:
    st.warning("Your expenses are greater than your income. You need to cut back on expenses.")
else:
    st.success("You are saving ${} every month.".format(monthly_income - expenses))

# Create output visuals
st.header("Monthly Expenses")

# Get user input for expense names and amounts
num_expenses = st.number_input("How many expenses do you have?", min_value=0, step=1, key="num_expenses")
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

# Check if any expenses are over budget
if total_expenses["Amount"][0] > expenses:
    st.warning("Your expenses are over budget.")
else:
    st.success("Your expenses are within budget.")

# Check if the file containing the previous budget data exists
if os.path.isfile("budget_data.csv"):
    budget_data = pd.read_csv("budget_data.csv")
else:
    budget_data = pd.DataFrame(columns=["Monthly Income", "Expenses", "Savings"])

# Add current budget data to DataFrame
current_budget_data = pd.DataFrame({"Monthly Income": monthly_income, "Expenses": expenses, "Savings": monthly_income - expenses}, index=[0])
budget_data = budget_data.append(current_budget_data, ignore_index=True)

# Save budget data to file
budget_data.to_csv("budget_data.csv", index=False)

# Display previous budget data in a table
st.header("Previous Budget Data")
st.table(budget_data)

# Check if the file containing the previous expense data exists
if os.path.isfile("expense_data.csv"):
    prev_expense_data = pd.read_csv("expense_data.csv")
else:
    prev_expense_data = pd.DataFrame(columns=["Expense Name", "Amount"])

# Append current expense data to DataFrame
current_expense_data = pd.DataFrame({"Expense Name": expense_names, "Amount": expense_amounts})
expense_data = pd.concat([prev_expense_data, current_expense_data], ignore_index=True)

# Save expense data to file
expense_data.to_csv("expense_data.csv", index=False)


# Deploy your app
# Use the command `streamlit run app.py` to run your app locally
# You can also deploy your app to hosting services like Heroku or Streamlit Sharing




