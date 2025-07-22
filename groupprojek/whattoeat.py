import streamlit as st

# --- Title ---
st.title("🍽️ What Should I Eat?")
st.write("Tell me what you're craving, and I'll help you decide!")

# --- Sidebar: User Input ---
st.sidebar.header("Your Preferences")

location = st.sidebar.text_input("📍 Your Location", placeholder="e.g. Kuala Lumpur")
budget = st.sidebar.slider("💰 Your Budget (RM)", 5, 100, 20)
preference = st.sidebar.selectbox("🍲 Preference", ["Any", "Vegetarian", "Halal", "Vegan"])
craving = st.sidebar.selectbox("😋 What are you craving?", ["Any", "Spicy", "Sweet", "Savory", "Fried"])
calories = st.sidebar.slider("🔥 Max Calories", 100, 1500, 800)
nutrient = st.sidebar.multiselect("🥦 Nutrients to focus on", ["Protein", "Fiber", "Low Fat", "Low Carb", "Iron"])

# --- Recommend Button ---
if st.sidebar.button("🔍 Find My Meal"):
    # 🧠 Simulated results (you can later connect to real data)
    st.subheader("🍱 Suggested Meal:")
    st.write("**Meal:** Grilled Chicken Salad")
    st.write("**Price:** RM18")
    st.write("**Calories:** 450 kcal")
    st.write("**Rating:** ⭐ 4.5/5")
    st.write("**Nearest Store:** FitEats @ Pavilion, 1.2 km")

    # You can improve this by filtering data based on the input later!
