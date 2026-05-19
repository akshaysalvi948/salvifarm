import streamlit as st
import urllib.parse
import os

# --- CONFIGURATION (YOUR NUMBER UPDATED) ---
MY_WHATSAPP_NUMBER = "917208974398"  

# --- APP PAGE SETUP ---
st.set_page_config(page_title="The Salvi Farms", page_icon="🥭", layout="centered")

# --- TRENDY LUXURY UI CUSTOM STYLING ---
st.markdown("""
    <style>
    /* Background overall styling */
    .main { 
        background: radial-gradient(circle, #fcfbf7 0%, #f4f0e6 100%);
    }
    
    /* Modern Glassmorphic Container */
    .app-card {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 12px 40px 0 rgba(45, 90, 39, 0.08);
        margin-bottom: 25px;
    }
    
    /* Elegant typography */
    .brand-title {
        font-family: 'Playfair Display', 'Georgia', serif;
        color: #1e3d1a;
        text-align: center;
        font-size: 32px;
        font-weight: 700;
        letter-spacing: 1.5px;
        margin-bottom: 5px;
    }
    .brand-tagline {
        color: #bfa15f;
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
        margin-bottom: 25px;
    }
    
    /* Dedicated Product Badge Style */
    .product-badge {
        background-color: #2d5a27;
        color: #fbf9f4;
        padding: 15px 20px;
        border-radius: 14px;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
        border: 1px solid #d4af37;
        margin-bottom: 15px;
    }
    
    /* Trendy Glass Form Inputs */
    div.stTextInput > div > div > input, 
    div.stSelectbox > div > div > div, 
    div.stTextArea > div > div > textarea {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        padding: 12px !important;
        font-size: 16px !important;
        color: #2d5a27 !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    /* Glowing active states for form fields */
    div.stTextInput > div > div > input:focus, 
    div.stSelectbox > div > div > div:focus, 
    div.stTextArea > div > div > textarea:focus {
        border-color: #2d5a27 !important;
        box-shadow: 0 0 0 3px rgba(45, 90, 39, 0.15) !important;
    }

    /* Premium Button Style with subtle gradient and lift effect */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #2d5a27 0%, #1e3d1a 100%);
        color: white;
        border-radius: 14px;
        width: 100%;
        font-size: 18px;
        font-weight: 600;
        height: 54px;
        border: none;
        letter-spacing: 0.5px;
        transition: all 0.3s transform ease;
        box-shadow: 0 8px 20px rgba(45, 90, 39, 0.25);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 24px rgba(45, 90, 39, 0.35);
        background: linear-gradient(135deg, #35692e 0%, #24471f 100%);
    }
    
    /* Clean Footer */
    .footer { 
        text-align: center; 
        font-size: 12px; 
        color: #8a9489; 
        margin-top: 50px; 
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP LAYOUT CONTAINER ---
st.markdown('<div class="app-card">', unsafe_allow_html=True)

# 1. Core Branding Logo Header
if os.path.exists("logo.png"):
    st.image("logo.png", use_column_width=True)
else:
    st.markdown('<div class="brand-title">THE SALVI FARMS</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-tagline">Pure Organic Alphonso Mangoes</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 2. Modern Product Card Showcase Block
st.markdown('<div class="app-card">', unsafe_allow_html=True)
st.markdown("<h4 style='color: #1e3d1a; margin-top:0; font-weight:600; font-size:18px;'>✨ Live Digital Storefront</h4>", unsafe_allow_html=True)

if os.path.exists("app_mockup.png"):
    st.image("app_mockup.png", use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 3. Interactive Luxury Checkout Form Block
st.markdown('<div class="app-card">', unsafe_allow_html=True)
with st.form("luxury_order_form", clear_on_submit=False):
    st.markdown("<h3 style='color: #1e3d1a; margin-top:0; font-size:22px; font-weight:600;'>🛒 Quick Checkout</h3>", unsafe_allow_html=True)
    
    # Prominent display of your single premium product selection
    st.markdown('<div class="product-badge">🥭 Selected Item: Organic Alphonso Mango (1 Dozen Premium)</div>', unsafe_allow_html=True)
    PRODUCT_NAME = "The Salvi Farms Organic Alphonso Mango (1 Dozen Premium)"
    
    # Input alignment grid
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Full Name", placeholder="e.g. Rahul Salvi")
    with col2:
        phone = st.text_input("WhatsApp Number", placeholder="e.g. 9876543210")
        
    quantity = st.selectbox("Select Quantity (Number of Dozens)", [1, 2, 3, 5, 10, 20])
    address = st.text_area("Delivery Drop Location", placeholder="Enter full home/office address details...")
    
    submitted = st.form_submit_button("PLACE ORDER & SHARE")

# --- TRENDING WHATSAPP REDIRECTION TRIGGER ---
if submitted:
    if not name or not phone or not address:
        st.error("⚠️ Please fill out all required details to finalize your request.")
    else:
        # Structured business layout text block sent directly to your WhatsApp chat
        order_details = (
            f"📦 *THE SALVI FARMS — NEW MANGO ORDER*\n"
            f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
            f"👤 *Client Name:* {name}\n"
            f"📱 *WhatsApp:* {phone}\n\n"
            f"🥭 *Item Selected:* {PRODUCT_NAME}\n"
            f"🔢 *Total Quantity:* {quantity} Dozen(s)\n\n"
            f"📍 *Delivery Location:*\n{address}\n"
            f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
            f"✨ _Order submitted via Instant Store App_"
        )
        
        encoded_message = urllib.parse.quote(order_details)
        whatsapp_url = f"https://wa.me/{MY_WHATSAPP_NUMBER}?text={encoded_message}"
        
        # Tap-to-send action block
        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
                <div style="background: linear-gradient(135deg, #25D366 0%, #1cbd55 100%); 
                color: white; text-align: center; padding: 16px; border-radius: 14px; 
                font-weight: 600; font-size: 18px; margin-top: 20px;
                box-shadow: 0 10px 25px rgba(37, 211, 102, 0.4); transition: transform 0.2s;">
                    💬 Launch WhatsApp to Confirm Order Delivery
                </div>
            </a>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Clean branding footer
st.markdown("<div class='footer'>THE SALVI FARMS • EST. 2026 • ORGANIC LUXURY</div>", unsafe_allow_html=True)
