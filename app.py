import streamlit as st
import urllib.parse
import smtplib
from email.mime.text import MIMEText

# --- CONFIGURATION (EDIT THESE DETAILS) ---
MY_WHATSAPP_NUMBER = "917208974398"  # Replace with your number (Country code first, no +)
MY_EMAIL = "akshaysalvi948@gmail.com"     # Replace with your Gmail
EMAIL_PASSWORD = "your-app-password"  # Replace with your Gmail App Password

# --- APP PAGE SETUP ---
st.set_page_config(page_title="The Salvi Farms", page_icon="🥭", layout="centered")

# Custom Styling for Forest Green and Gold theme
st.markdown("""
    <style>
    .main { background-color: #fbf9f4; }
    h1 { color: #2d5a27; text-align: center; font-family: 'Georgia', serif; }
    .subtitle { color: #d4af37; text-align: center; font-style: italic; margin-bottom: 30px; font-size: 18px; }
    div.stButton > button:first-child {
        background-color: #2d5a27; color: white; border-radius: 8px;
        width: 100%; font-size: 18px; font-weight: bold; height: 50px;
        border: 2px solid #d4af37;
    }
    div.stButton > button:first-child:hover { background-color: #1e3d1a; color: white; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>THE SALVI FARMS</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Pure Organic Alphonso Mangoes — From Tree to Home</p>", unsafe_allow_html=True)

# --- ORDER FORM ---
with st.form("order_form", clear_on_submit=False):
    st.subheader("Place Your Alphonso Order")
    
    name = st.text_input("Your Full Name *")
    phone = st.text_input("WhatsApp Number *")
    
    mango_type = st.selectbox("Select Mango Box Type *", [
        "Premium Devgad Alphonso (1 Dozen)",
        "Premium Ratnagiri Alphonso (1 Dozen)",
        "Organic Alphonso Family Pack (5 Kg)"
    ])
    
    quantity = st.selectbox("Quantity (Number of Boxes) *", [1, 2, 3, 5, 10])
    address = st.text_area("Complete Delivery Address *")
    
    submitted = st.form_submit_button("🚀 Submit Order via WhatsApp & Email")

# --- FORM SUBMISSION LOGIC ---
if submitted:
    if not name or not phone or not address:
        st.error("Please fill out all required fields.")
    else:
        # 1. Format the Order Message
        order_details = (
            f"*NEW MANGO ORDER - THE SALVI FARMS*\n\n"
            f"*Customer Name:* {name}\n"
            f"*WhatsApp No:* {phone}\n"
            f"*Product:* {mango_type}\n"
            f"*Quantity:* {quantity} Box(es)\n"
            f"*Delivery Address:* {address}"
        )
        
        # 2. Free Email Notification Sender (Backend Process)
        try:
            msg = MIMEText(order_details.replace('*', '')) # Remove asterisks for clean email text
            msg['Subject'] = f"New Mango Order from {name}"
            msg['From'] = MY_EMAIL
            msg['To'] = MY_EMAIL
            
            # Connect to Gmail SMTP
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(MY_EMAIL, EMAIL_PASSWORD)
            server.sendmail(MY_EMAIL, [MY_EMAIL], msg.as_string())
            server.quit()
            st.success("✅ Order email logged successfully!")
        except Exception as e:
            # If email configuration isn't completed yet, let them proceed to WhatsApp
            st.warning("Order processing... Proceed to WhatsApp link below.")

        # 3. Create Free WhatsApp Link Generator
        encoded_message = urllib.parse.quote(order_details)
        whatsapp_url = f"https://wa.me/{MY_WHATSAPP_NUMBER}?text={encoded_message}"
        
        # Provide a prominent click link to open WhatsApp
        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank">
                <div style="background-color: #25D366; color: white; text-align: center; 
                padding: 15px; border-radius: 8px; font-weight: bold; font-size: 18px; 
                margin-top: 15px; text-decoration: none; border: 1px solid #128C7E;">
                    💬 Click Here to Confirm Order on WhatsApp
                </div>
            </a>
        """, unsafe_allow_html=True)
