import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the app
st.title("Business Analysis App 📊")

# Sidebar for template selection
st.sidebar.header("Choose Analysis Template")
template = st.sidebar.selectbox(
    "Select the type of business analysis",
    ("Sales Analysis", "Customer Analysis", "Financial Analysis", "Marketing Analysis", "Operational Analysis")
)

# Generate random data for the sake of this example
def generate_data(template):
    if template == "Sales Analysis":
        data = {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            'Sales': np.random.randint(1000, 5000, 12)
        }
    elif template == "Customer Analysis":
        data = {
            'Customer ID': range(1, 101),
            'Age': np.random.randint(18, 70, 100),
            'Annual Spend': np.random.randint(500, 10000, 100)
        }
    elif template == "Financial Analysis":
        data = {
            'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
            'Revenue': np.random.randint(10000, 50000, 4),
            'Expenses': np.random.randint(5000, 30000, 4),
            'Profit': np.random.randint(1000, 20000, 4)
        }
    elif template == "Marketing Analysis":
        data = {
            'Campaign': [f'Campaign {i}' for i in range(1, 11)],
            'Clicks': np.random.randint(1000, 10000, 10),
            'Conversions': np.random.randint(100, 1000, 10)
        }
    else:
        data = {
            'Department': ['Sales', 'HR', 'Finance', 'Marketing', 'Operations'],
            'Efficiency': np.random.randint(60, 100, 5),
            'Cost': np.random.randint(1000, 10000, 5)
        }
    return pd.DataFrame(data)

# Display the data
data = generate_data(template)
st.header(f"{template} 📈")
st.write(data)

# Visualize the data based on the template selected
if template == "Sales Analysis":
    st.line_chart(data.set_index('Month'))
elif template == "Customer Analysis":
    fig, ax = plt.subplots()
    ax.scatter(data['Age'], data['Annual Spend'])
    plt.xlabel('Age')
    plt.ylabel('Annual Spend')
    st.pyplot(fig)
elif template == "Financial Analysis":
    data.plot(x='Quarter', y=['Revenue', 'Expenses', 'Profit'], kind='bar')
    st.pyplot(plt)
elif template == "Marketing Analysis":
    data.plot(x='Campaign', y=['Clicks', 'Conversions'], kind='bar')
    st.pyplot(plt)
else:
    data.plot(x='Department', y=['Efficiency', 'Cost'], kind='bar')
    st.pyplot(plt)
