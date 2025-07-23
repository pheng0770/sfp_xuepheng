import streamlit as st
import requests
import random

# ===== API Key =====
SPOONACULAR_API_KEY = st.secrets["api"]["spoonacular_key"]

# ===== Macaron Gradient Background =====
def set_background_macaron_gradient():
    style = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffe4e1, #e6e6fa, #d6f0ff, #d0f0c0, #ffdab9);
        background-size: 300% 300%;
        animation: gradientFlow 15s ease infinite;
    }

    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .text-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 1em;
        border-radius: 15px;
        margin-bottom: 1em;
        color: black !important;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
    }

    .result-title {
        font-size: 22px;
        font-weight: bold;
        color: black;
        margin-bottom: 0.5em;
    }

    h1 {
        color: black;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

# ===== Spoonacular API =====
def get_food_ideas(craving, max_calories):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": craving,
        "maxCalories": max_calories,
        "number": 5,
        "addRecipeInformation": True,
        "apiKey": SPOONACULAR_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        st.error(f"API error: {response.status_code}")
        return []

# ===== Dummy Restaurant Data =====
def get_dummy_restaurants(craving, location):
    dummy_data = {
        "pizza": [
            {"name": "Joe's Pizza", "address": f"Main Street, {location}", "rating": 4.5},
            {"name": "Crusty Heaven", "address": f"2nd Ave, {location}", "rating": 4.2},
        ],
        "sushi": [
            {"name": "Sushi World", "address": f"Market Road, {location}", "rating": 4.7},
        ],
        "burger": [
            {"name": "Burger Town", "address": f"Downtown {location}", "rating": 4.3},
        ]
    }
    for key in dummy_data:
        if key in craving.lower():
            return dummy_data[key]
    return [{"name": "Local Bites", "address": f"Center St, {location}", "rating": 4.0}]

# ===== Page Setup =====
st.set_page_config(page_title="What To Eat App", page_icon="🍽", layout="centered")
set_background_macaron_gradient()

# ===== Header =====
st.markdown("""
    <div class='text-box'>
        <h1 style='text-align: center;'>🍽 What Should I Eat?</h1>
        <p style='text-align: center;'>Find meals and restaurant ideas based on your cravings and budget.</p>
    </div>
""", unsafe_allow_html=True)

# ===== Craving Options =====
craving_options = ["Pizza", "Sushi", "Burger", "Pasta", "Salad", "Ramen", "Tacos", "Fried Chicken", "Dumplings", "Noodles"]

# ===== Initialize session_state craving input =====
if "craving_input" not in st.session_state:
    st.session_state.craving_input = ""

# ===== Input Form =====
st.markdown("<div class='text-box'><h2>🔎 Enter Your Details</h2>", unsafe_allow_html=True)
with st.form("user_inputs", clear_on_submit=False):
    location = st.text_input("📍 Your Location")
    budget = st.number_input("💰 Your Budget", min_value=1)
    currency = st.text_input("💱 Your Currency Symbol (e.g., $, €, ₹, RM)", value="$")
    
    # Craving Input with Random Button
    col1, col2 = st.columns([4, 1])
    with col1:
        craving = st.text_input("😋 What are you craving?", value=st.session_state.craving_input)
    with col2:
        random_clicked = st.form_submit_button("🎲 Random")
        if random_clicked:
            st.session_state.craving_input = random.choice(craving_options)
            craving = st.session_state.craving_input  # update field value
    
    calories = st.number_input("🔥 Max Calories", min_value=100, max_value=2000, step=50)
    submitted = st.form_submit_button("🔍 Find Foods")
st.markdown("</div>", unsafe_allow_html=True)

# ===== Search Result Handling =====
if submitted:
    st.markdown("<div class='text-box'>", unsafe_allow_html=True)
    st.info("🔎 Searching for food options...")

    # ===== Recipes =====
    food_results = get_food_ideas(craving, calories)
    if food_results:
        st.markdown("### 🧑‍🍳 Recipe Suggestions")
        found = False
        for food in food_results:
            estimated_price = 10.00  # You can add price logic later
            if estimated_price <= budget:
                found = True
                st.markdown("<div class='text-box'>", unsafe_allow_html=True)
                st.markdown(f"<div class='result-title'>🍽 {food['title']}</div>", unsafe_allow_html=True)
                st.image(food["image"], use_column_width=True)
                st.write(f"📍 Location: {location}")
                st.write(f"💸 Estimated Price: {currency}{estimated_price}")
                st.write(f"🔥 Calories: {calories} kcal")
                st.write(f"🕐 Ready in {food['readyInMinutes']} minutes")
                st.write(f"🍽 Servings: {food['servings']}")
                st.markdown(f"[🔗 View Recipe]({food['sourceUrl']})")
                st.markdown("</div>", unsafe_allow_html=True)
        if not found:
            st.warning("🚫 No foods found within your budget.")
    else:
        st.warning("🔍 No recipes found.")

    # ===== Restaurant Suggestions =====
    st.markdown("### 🏪 Nearby Restaurant Suggestions")
    restaurants = get_dummy_restaurants(craving, location)
    for r in restaurants:
        st.markdown("<div class='text-box'>", unsafe_allow_html=True)
        st.markdown(f"<div class='result-title'>🏪 {r['name']}</div>", unsafe_allow_html=True)
        st.write(f"📍 {r['address']}")
        st.write(f"⭐ Rating: {r['rating']}")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)