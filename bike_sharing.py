import streamlit as st
import pandas as pd

# Load the data
df_day = pd.read_csv("/content/day.csv")

# Add a title to your dashboard
st.title("Bike Sharing Data Analysis Dashboard")

# Add a subtitle
st.subheader("Exploratory Data Analysis")

# Display the first few rows of the dataset
st.write("Displaying the first few rows of the dataset:")
st.write(df_day.head())

# Add a section for data visualization
st.subheader("Data Visualization")

# Add a histogram for the 'temp' column
st.write("Histogram of Temperature (temp):")
st.bar_chart(df_day['temp'])

# Add a scatter plot for 'temp' vs 'cnt'
st.write("Scatter Plot of Temperature (temp) vs Count (cnt):")
st.write(df_day[['temp', 'cnt']])

# Add a plot for 'weathersit' distribution
st.write("Bar Plot of Weather Situation (weathersit) Distribution:")
st.bar_chart(df_day['weathersit'].value_counts())

# Add a section for insights
st.subheader("Insights")

# Add text insights based on the analysis
st.write("Based on the analysis, we can see that temperature has a positive correlation with the count of registered users. Additionally, the weather situation (weathersit) has a significant impact on the number of bike rentals during the autumn season (season 3).")

# Add a section for conclusions
st.subheader("Conclusions")

# Add text for the conclusions drawn from the analysis
st.write("In conclusion, the weather, season, and day of the week all have significant effects on bike rental trends. Businesses can leverage this information to optimize their operations and marketing strategies.")

# Display the dashboard
st.show()
