import streamlit as st
import urllib.parse
import os

# --- CONFIGURATION (EDIT YOUR WHATSAPP NUMBER) ---
# Format: Country code first, no spaces, no '+' sign (e.g., 91 for India + your 10 digits)
MY_WHATSAPP_NUMBER = "919876543210"  

# --- APP PAGE SETUP ---
st.set_page_config(page_title="The Salvi Farms", page_icon="🥭", layout="centered")

# Premium Custom Styling matching the Forest Green and Cream aesthetic
st.markdown("""
    <style>
    .main { background-color: #fbf9f4; }
    div.stButton > button:first-child {
        background-color: #2d5a27; color: white; border-radius: 8px;
        width: 100%; font-size: 18px; font-weight: bold; height: 50px;
        border: 2px solid #d4af37;
    }
    div.stButton > button:first-child:hover { background-color: #1e3d1a; color: white; }
    .footer { text-align: center; font-size: 12px; color: #777; margin-top: 30px; font-style: italic; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER (Loads logo.png from your local folder safely) ---
IMAGE_FILENAME = "logo.png"

if os.path.exists(IMAGE_FILENAME):
    st.image(IMAGE_FILENAME, use_column_width=True)
else:
    # Beautiful text backup so your app never crashes or shows an error if the file is missing
    st.markdown("<h1 style='color: #2d5a27; text-align: center; margin-bottom: 0;'>THE SALVI FARMS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #d4af37; text-align: center; font-style: italic; margin-top: 0; font-size: 18px;'>Pure Organic Alphonso Mangoes — From Tree to Home</p>", unsafe_allow_html=True)

# --- ORDER FORM ---
st.write("---")
with st.form("order_form", clear_on_submit=False):
    st.subheader("🛒 Place Your Alphonso Order")
    
    name = st.text_input("Your Full Name *", placeholder="Enter your name")
    phone = st.text_input("Your Contact/WhatsApp Number *", placeholder="e.g., 9876543210")
    
    mango_type = st.selectbox("Select Mango Box Type *", [
        "Premium Devgad Alphonso (1 Dozen)",
        "Premium Ratnagiri Alphonso (1 Dozen)",
        "Organic Alphonso Family Pack (5 Kg)"
    ])
    
    quantity = st.selectbox("Quantity (Number of Boxes) *", [1, 2, 3, 5, 10])
    address = st.text_area("Complete Delivery Address *", placeholder="Enter your complete home or office delivery address")
    
    submitted = st.form_submit_button("Generate WhatsApp Order")

# --- FORM SUBMISSION PROCESSING ---
if submitted:
    if not name or not phone or not address:
        st.error("⚠️ Please fill out all required fields before submitting.")
    else:
        # Build the beautifully formatted structured WhatsApp text message block
        order_details = (
            f"*NEW MANGO ORDER - THE SALVI FARMS*\n\n"
            f"*Customer Name:* {name}\n"
            f"*WhatsApp No:* {phone}\n"
            f"*Product:* {mango_type}\n"
            f"*Quantity:* {quantity} Box(es)\n"
            f"*Delivery Address:* {address}"
        )
        
        # Create Free Interactive WhatsApp Link Generator
        encoded_message = urllib.parse.quote(order_details)
        whatsapp_url = f"https://wa.me/{MY_WHATSAPP_NUMBER}?text={encoded_message}"
        
        # Display the big green button for the customer to tap and send to you
        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank">
                <div style="background-color: #25D366; color: white; text-align: center; 
                padding: 16px; border-radius: 8px; font-weight: bold; font-size: 18px; 
                margin-top: 15px; text-decoration: none; border: 1px solid #128C7E; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                    💬 Click Here to Share Order on WhatsApp
                </div>
            </a>
        """, unsafe_allow_html=True)

st.markdown("<p class='footer'>The Salvi Farms © 2026 | Pure Organic Harvest</p>", unsafe_allow_html=True)
