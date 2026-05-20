import streamlit as st
import urllib.parse
import os

# --- CONFIGURATION ---
MY_WHATSAPP_NUMBER = "917208974398"  

# --- APP PAGE SETUP ---
st.set_page_config(page_title="The Salvi Farms", page_icon="🥭", layout="centered")

# --- STARLINK-INSPIRED CINEMATIC UI CUSTOM STYLING ---
st.markdown("""
    <style>
    /* Global Reset & Cinematic Starlink Background Layout */
    .main { 
        background: url("https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2?auto=format&fit=crop&q=80&w=1600") no-repeat center center fixed;
        background-size: cover;
    }
    
    /* Make Streamlit container invisible to allow full-screen background immersion */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
    }
    
    /* Starlink Premium Floating Glass Card Container */
    .starlink-container {
        background: rgba(10, 15, 10, 0.7);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 0px; /* Sharp, geometric Starlink edges */
        padding: 40px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        color: #ffffff;
        margin-bottom: 30px;
    }
    
    /* Minimalist High-End Typography */
    .starlink-header {
        font-family: 'Inter', -apple-system, sans-serif;
        text-align: center;
        font-weight: 300;
        letter-spacing: 6px;
        color: #ffffff;
        font-size: 28px;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    
    .starlink-tagline {
        font-family: 'Inter', -apple-system, sans-serif;
        text-align: center;
        font-weight: 400;
        letter-spacing: 3px;
        color: #bfa15f; /* Elegant Gold accent */
        font-size: 11px;
        text-transform: uppercase;
        margin-bottom: 35px;
    }
    
    .section-title {
        font-family: 'Inter', -apple-system, sans-serif;
        font-weight: 300;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-size: 14px;
        color: #e0e0e0;
        margin-top: 25px;
        margin-bottom: 15px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        padding-bottom: 5px;
    }
    
    /* Starlink-Style Borderless Dark Inputs */
    div.stTextInput > div > div > input, 
    div.stSelectbox > div > div > div, 
    div.stTextArea > div > div > textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 0px !important; /* Minimalist sharp edges */
        padding: 12px !important;
        font-size: 15px !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s ease;
    }
    
    /* Input Hover & Focus States */
    div.stTextInput > div > div > input:focus, 
    div.stSelectbox > div > div > div:focus, 
    div.stTextArea > div > div > textarea:focus {
        border-color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        box-shadow: none !important;
    }
    
    /* Target the text color inside labels and dropdown selection states */
    label, p, div[data-baseweb="select"] span {
        color: #cccccc !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
        letter-spacing: 1px;
    }

    /* Starlink Iconic Solid Interactive Call-To-Action Button */
    div.stButton > button:first-child {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 0px !important;
        width: 100%;
        font-size: 14px;
        font-weight: 600;
        height: 50px;
        border: none;
        text-transform: uppercase;
        letter-spacing: 3px;
        transition: all 0.3s ease;
        margin-top: 20px;
    }
    div.stButton > button:first-child:hover {
        background-color: #bfa15f !important; /* Gold transition on hover */
        color: #ffffff !important;
        transform: none;
    }
    
    /* Minimalist Footer */
    .starlink-footer { 
        text-align: center; 
        font-size: 10px; 
        color: rgba(255,255,255,0.4); 
        margin-top: 60px; 
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# --- STARLINK MAIN WORKSPACE CARD ---
st.markdown('<div class="starlink-container">', unsafe_allow_html=True)

# 1. Elegant Geometric Header Replacement
st.markdown('<div class="starlink-header">THE SALVI FARMS</div>', unsafe_allow_html=True)
st.markdown('<div class="starlink-tagline">ORDER ALPHONSO • FROM TREE TO HOME</div>', unsafe_allow_html=True)

# 2. Logo Badge Render Option
if os.path.exists("logo.png"):
    # Center the logo beautifully within the glass container layout
    col_l1, col_l2, col_l3 = st.columns([1,2,1])
    with col_l2:
        st.image("logo.png", use_column_width=True)

# 3. Interactive Luxury Checkout Form Block
with st.form("starlink_order_form", clear_on_submit=False):
    
    st.markdown('<div class="section-title">01 / SELECT QUANTITY</div>', unsafe_allow_html=True)
    PRODUCT_NAME = "The Salvi Farms Organic Alphonso Mango (1 Dozen Premium)"
    
    # Beautifully display the item description as a static header string
    st.markdown(f"<p style='font-size: 16px !important; color: #ffffff !important; font-weight: 400; letter-spacing: 1px; margin-bottom: 15px;'>🥭 {PRODUCT_NAME}</p>", unsafe_allow_html=True)
    quantity = st.selectbox("Number of Dozens Required", [1, 2, 3, 5, 10, 20], label_visibility="collapsed")
    
    st.markdown('<div class="section-title">02 / CUSTOMER INFORMATION</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Full Name", placeholder="FIRST & LAST NAME")
    with col2:
        phone = st.text_input("WhatsApp Number", placeholder="PHONE NUMBER WITH COUNTRY CODE")
        
    st.markdown('<div class="section-title">03 / PARCEL DESTINATION</div>', unsafe_allow_html=True)
    
    # --- JAVASCRIPT GEOLOCATION BRIDGE ---
    st.components.v1.html("""
    <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition, showError);
            } else {
                alert("Geolocation support is missing on this browser.");
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
                            if (inputs[idx].placeholder.includes("GPS AREA PROFILE")) {
                                inputs[idx].value = data.display_name;
                                inputs[idx].dispatchEvent(new Event('input', { bubbles: true }));
                                break;
                            }
                        }
                    }
                })
                .catch(err => alert("Error resolving address parameters. Please type manually."));
        }

        function showError(error) {
            alert("Location access coordinate request unfulfilled. Please type details manually.");
        }
    </script>
    <button type="button" onclick="getLocation()" style="
        background-color: transparent; color: #ffffff; border: 1px solid rgba(255,255,255,0.4); 
        padding: 10px 16px; border-radius: 0px; font-weight: 400; 
        cursor: pointer; width: 100%; font-size: 12px; letter-spacing: 2px;
        text-transform: uppercase; font-family: sans-serif; transition: all 0.3s ease;">
        📍 CLICK TO AUTO-DETECT REGION
    </button>
    """, height=46)
    
    # Auto-detected tracking row entry
    gps_address = st.text_input("Detected Region / State Profile", placeholder="GPS AREA PROFILE WILL LOAD HERE...", label_visibility="collapsed")
    
    # Exact Manual Address configuration layout input
    st.markdown("<p style='margin-bottom:5px; margin-top:10px;'>Exact Door/Flat No, Building Name & Landmark *</p>", unsafe_allow_html=True)
    exact_address = st.text_area("Exact Address Tab", placeholder="ENTER WING, FLOOR, ROOM NUMBER, AND LOCAL LANDMARKS...", label_visibility="collapsed")
    
    submitted = st.form_submit_button("PLACE ORDER & SHARE")

# --- WHATSAPP REDIRECTION DISPATCH ---
if submitted:
    if not name or not phone or not exact_address:
        st.error("⚠️ CRITICAL: Enter Name, Contact, and Exact Delivery Address Details to proceed.")
    else:
        full_shipping_destination = f"{exact_address}\n🗺️ Region Profile: {gps_address if gps_address else 'Entered Manually'}"
        
        order_details = (
            f"🛰️ *THE SALVI FARMS — DIRECT MANGO ACQUISITION*\n"
            f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
            f"👤 *Customer:* {name}\n"
            f"📱 *Contact:* {phone}\n\n"
            f"🥭 *Product:* {PRODUCT_NAME}\n"
            f"🔢 *Quantity:* {quantity} Dozen(s)\n\n"
            f"📍 *Delivery Destination:*\n{full_shipping_destination}\n"
            f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
            f"⚡ _Processed via Luxury Direct-Storefront Protocol_"
        )
        
        encoded_message = urllib.parse.quote(order_details)
        whatsapp_url = f"https://wa.me/{MY_WHATSAPP_NUMBER}?text={encoded_message}"
        
        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #ffffff; color: #000000; text-align: center; 
                padding: 16px; border-radius: 0px; font-weight: 600; font-size: 14px; margin-top: 20px;
                letter-spacing: 3px; text-transform: uppercase; box-shadow: 0 10px 30px rgba(255,255,255,0.1);
                transition: all 0.3s ease;">
                    💬 Initialize WhatsApp Order Confirmation
                </div>
            </a>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Minimal Starlink Style bottom credits line
st.markdown("<div class='starlink-footer'>THE SALVI FARMS © 2026 • PRIVACY & LEGAL • SUPPLY CHAIN INTEGRITY</div>", unsafe_allow_html=True)
