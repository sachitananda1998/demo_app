import streamlit as st
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('cencus_data.db')
cursor = conn.cursor()

# Define Streamlit app
def main():
    st.title("Census Data Analysis")

    # Define query options
    query_options = [
        "Total population of each district",
        "Literate males and females in each district",
        "Percentage of workers in each district",
        "Households with access to LPG or PNG in each district",
        "Religious composition of each district",
        "Households with internet access in each district",
        "Educational attainment distribution in each district",
        "Households with access to transportation modes in each district",
        "Condition of occupied census houses in each district",
        "Household size distribution in each district",
        "Total number of households in each state",
        "Households with latrine facility within the premises in each state",
        "Average household size in each state",
        "Distribution of latrine facilities in each state",
        "Households with access to drinking water sources near the premises in each state",
        "Average household income distribution in each state",
        "Percentage of married couples with different household sizes in each state",
        "Households below the poverty line in each state",
        "Overall literacy rate in each state"
    ]

    # Select query
    query = st.selectbox("Select Query", query_options)

    # Run selected query and display results
    if query == "Total population of each district":
        # Run query and display results
        result = cursor.execute("SELECT District, SUM(Population) FROM census_data GROUP BY District").fetchall()
        st.write(result)

    # Add other queries here...

# Run Streamlit app
if __name__ == "__main__":
    main()

# Close database connection
conn.close()