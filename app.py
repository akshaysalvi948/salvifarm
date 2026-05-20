import streamlit as st
import urllib.parse
import os

# --- CONFIGURATION ---
MY_WHATSAPP_NUMBER = "917208974398"  

# --- APP PAGE SETUP ---
st.set_page_config(page_title="The Salvi Farms", page_icon="🥭", layout="centered")

# --- TRENDY LUXURY UI CUSTOM STYLING ---
st.markdown("""
    <style>
    .main { 
        background: radial-gradient(circle, #fcfbf7 0%, #f4f0e6 100%);
    }
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
    .brand-title {
        font-family: 'Playfair Display', 'Georgia', serif;
        color: #1e3d1a; text-align: center; font-size: 32px; font-weight: 700; letter-spacing: 1.5px; margin-bottom: 5px;
    }
    .brand-tagline {
        color: #bfa15f; text-align: center; font-family: 'Inter', sans-serif; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; font-weight: 600; margin-bottom: 25px;
    }
    .product-badge {
        background-color: #2d5a27; color: #fbf9f4; padding: 15px 20px; border-radius: 14px; font-size: 18px; font-weight: 600; text-align: center; border: 1px solid #d4af37; margin-bottom: 15px;
    }
    div.stTextInput > div > div > input, 
    div.stSelectbox > div > div > div, 
    div.stTextArea > div > div > textarea {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        padding: 12px !important; font-size: 16px !important; color: #2d5a27 !important;
    }
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #2d5a27 0%, #1e3d1a 100%);
        color: white; border-radius: 14px; width: 100%; font-size: 18px; font-weight: 600; height: 54px; border: none;
        box-shadow: 0 8px 20px rgba(45, 90, 39, 0.25);
    }
    .footer { text-align: center; font-size: 12px; color: #8a9489; margin-top: 50px; letter-spacing: 1px; }
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
    
    st.markdown('<div class="product-badge">🥭 Selected Item: Organic Alphonso Mango (1 Dozen Premium)</div>', unsafe_allow_html=True)
    PRODUCT_NAME = "The Salvi Farms Organic Alphonso Mango (1 Dozen Premium)"
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Full Name *", placeholder="e.g. Rahul Salvi")
    with col2:
        phone = st.text_input("WhatsApp Number *", placeholder="e.g. 9876543210")
        
    quantity = st.selectbox("Select Quantity (Number of Dozens) *", [1, 2, 3, 5, 10, 20])
    
    st.write("---")
    st.markdown("<h4 style='color: #1e3d1a; font-size: 16px; margin-bottom: 2px;'>📍 Shipping Address Details</h4>", unsafe_allow_html=True)
    
    # --- JAVASCRIPT GEOLOCATION BRIDGE ---
    # Targets the first text input box (Detected Area) dynamically upon click
    st.components.v1.html("""
    <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition, showError);
            } else {
                alert("Geolocation is not supported by this browser.");
            }
        }

        function showPosition(position) {
            var lat = position.coords.latitude;
            var lon = position.coords.longitude;
            
            var url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}&addressdetails=1`;
            
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if(data && data.display_name) {
                        const inputs = window.parent.document.getElementsByTagName('input');
                        for (let idx = 0; idx < inputs.length; idx++) {
                            if (inputs[idx].placeholder.includes("Click button to locate")) {
                                inputs[idx].value = data.display_name;
                                inputs[idx].dispatchEvent(new Event('input', { bubbles: true }));
                                break;
                            }
                        }
                    }
                })
                .catch(err => alert("Error fetching location details. Please type manually."));
        }

        function showError(error) {
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    alert("Location permission denied. Please type your address fields manually.");
                    break;
                case error.POSITION_UNAVAILABLE:
                    alert("Location information unavailable.");
                    break;
                case error.TIMEOUT:
                    alert("Location request timed out.");
                    break;
            }
        }
    </script>
    <button type="button" onclick="getLocation()" style="
        background-color: #bfa15f; color: white; border: none; 
        padding: 10px 16px; border-radius: 12px; font-weight: bold; 
        cursor: pointer; width: 100%; font-size: 14px; box-shadow: 0 4px 10px rgba(191,161,95,0.25);
        font-family: sans-serif; margin-bottom: 5px;">
        📍 Auto-Detect My Nearby Location / City
    </button>
    """, height=46)
    
    # Auto-detected tracking row entry
    gps_address = st.text_input("Detected Area / Region", placeholder="Click button to locate your general area...")
    
    # Exact Manual Address tab row entry
    exact_address = st.text_area("Exact Flat/Room No., Building Name & Landmark *", placeholder="Type your room number, floor, wing, building name, road name, and landmarks...")
    
    submitted = st.form_submit_button("PLACE ORDER & SHARE")

# --- TRENDING WHATSAPP REDIRECTION TRIGGER ---
if submitted:
    if not name or not phone or not exact_address:
        st.error("⚠️ Please fill out all required fields (* Name, Phone, and Exact Address) before submitting.")
    else:
        # Beautifully stitch the verified area with the custom handwritten unit direction details
        full_shipping_destination = f"{exact_address}\n🗺️ Region Profile: {gps_address if gps_address else 'Entered Manually'}"
        
        order_details = (
            f"📦 *THE SALVI FARMS — NEW MANGO ORDER*\n"
            f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
            f"👤 *Client Name:* {name}\n"
            f"📱 *WhatsApp:* {phone}\n\n"
            f"🥭 *Item Selected:* {PRODUCT_NAME}\n"
            f"🔢 *Total Quantity:* {quantity} Dozen(s)\n\n"
            f"📍 *Exact Parcel Destination:*\n{full_shipping_destination}\n"
            f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
            f"✨ _Order submitted via Instant Store App_"
        )
        
        encoded_message = urllib.parse.quote(order_details)
        whatsapp_url = f"https://wa.me/{MY_WHATSAPP_NUMBER}?text={encoded_message}"
        
        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
                <div style="background: linear-gradient(135deg, #25D366 0%, #1cbd55 100%); 
                color: white; text-align: center; padding: 16px; border-radius: 14px; 
                font-weight: 600; font-size: 18px; margin-top: 20px;
                box-shadow: 0 10px 25 rgba(37, 211, 102, 0.4); transition: transform 0.2s;">
                    💬 Launch WhatsApp to Confirm Order Delivery
                </div>
            </a>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='footer'>THE SALVI FARMS • EST. 2026 • ORGANIC LUXURY</div>", unsafe_allow_html=True)
