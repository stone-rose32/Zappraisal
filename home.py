import streamlit as st
import pandas as pd

# Create a dictionary to store restaurant rankings
restaurant_rankings = {
    "Restaurant A": {"Food": 4, "Service": 3, "Ambience": 5},
    "Restaurant B": {"Food": 5, "Service": 4, "Ambience": 4},
    # Add more restaurants and their rankings here
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(restaurant_rankings).T

# Calculate the overall ranking for each restaurant
df["Overall"] = df.mean(axis=1)

# Streamlit app
st.title("Restaurant Rankings")
st.write("Rate restaurants based on food, service, and ambience.")

# User input
restaurant_name = st.text_input("Enter restaurant name:")
food_rating = st.slider("Food rating (1-5)", 1, 5)
service_rating = st.slider("Service rating (1-5)", 1, 5)
ambience_rating = st.slider("Ambience rating (1-5)", 1, 5)

# Update rankings
if st.button("Submit"):
    restaurant_rankings[restaurant_name] = {
        "Food": food_rating,
        "Service": service_rating,
        "Ambience": ambience_rating,
    }
    df = pd.DataFrame(restaurant_rankings).T
    df["Overall"] = df.mean(axis=1)
    st.success(f"Rankings updated for {restaurant_name}!")

# Display current rankings
st.write("Current Rankings:")
st.dataframe(df)

# Display overall rankings
st.write("Overall Rankings:")
st.dataframe(df.sort_values(by="Overall", ascending=False))
