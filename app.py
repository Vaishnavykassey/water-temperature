import streamlit as st
import os
from PIL import Image
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import pandas as pd
import random
import io
import base64

# Email Configuration
EMAIL_ADDRESS = "your_email@gmail.com"           # 🔁 Replace with your email
EMAIL_PASSWORD = "your_app_password_here"        # 🔁 Replace with your app password (not your regular password)
ALERT_RECIPIENT = "recipient_email@example.com"  # 🔁 Replace with recipient email

def send_alert_email(temp):
    subject = "Water Temperature Alert"
    body = f"Warning! Water temperature has reached {temp} °C."

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ALERT_RECIPIENT
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# Load alert sound (simple beep) from base64-encoded WAV
ALERT_SOUND_BASE64 = """
UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YQAAAAA=
"""  # very short beep sound

def play_alert_sound():
    sound_bytes = base64.b64decode(ALERT_SOUND_BASE64)
    st.audio(sound_bytes, format='audio/wav')

# Session state
if "monitoring" not in st.session_state:
    st.session_state.monitoring = False
if "data" not in st.session_state:
    st.session_state.data = []
if "alert_sent" not in st.session_state:
    st.session_state.alert_sent = False

# Page Setup
st.set_page_config(page_title="Smart Water Temp Monitor", layout="wide")
st.title("🌊 Smart Water Temperature Monitoring System")

# Logo from URL
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Google-flutter-logo.png/768px-Google-flutter-logo.png",
    width=100
)

# Sidebar Settings
st.sidebar.header("⚙️ Alert Settings")
high_threshold = st.sidebar.slider("High Temp Alert (°C)", 30, 100, 60)
low_threshold = st.sidebar.slider("Low Temp Alert (°C)", 0, 29, 15)

# Start / Stop Monitoring
col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ Start Monitoring"):
        st.session_state.monitoring = True
        st.session_state.alert_sent = False
        st.success("Monitoring started!")
with col2:
    if st.button("⏹ Stop Monitoring"):
        st.session_state.monitoring = False
        st.success("Monitoring stopped!")

# Placeholders
data_placeholder = st.empty()
status_placeholder = st.empty()
chart_placeholder = st.empty()

# Simulate temperature sensor
def simulate_sensor_data():
    return round(random.uniform(10.0, 70.0), 2)

# Monitoring Logic
if st.session_state.monitoring:
    temp = simulate_sensor_data()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.data.append({"Timestamp": now, "Temperature (°C)": temp})

    # Alerts
    if temp > high_threshold:
        status_placeholder.error(f"🔥 High Temp Alert: {temp} °C")
        if not st.session_state.alert_sent:
            send_alert_email(temp)
            play_alert_sound()
            st.session_state.alert_sent = True
    elif temp < low_threshold:
        status_placeholder.warning(f"❄️ Low Temp Alert: {temp} °C")
        st.session_state.alert_sent = False
    else:
        status_placeholder.success(f"✅ Temperature Normal: {temp} °C")
        st.session_state.alert_sent = False

    # Display Data Table
    df = pd.DataFrame(st.session_state.data)
    data_placeholder.dataframe(df.tail(10), use_container_width=True)

    # Line Chart
    chart_placeholder.line_chart(df.set_index("Timestamp")["Temperature (°C)"])

    # Refresh every 5 seconds
    time.sleep(5)
    st.rerun()  # ✅ Updated from deprecated st.experimental_rerun()

else:
    if st.session_state.data:
        st.subheader("📊 Temperature Log")
        df = pd.DataFrame(st.session_state.data)
        st.dataframe(df, use_container_width=True)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download CSV Log", data=csv, file_name="temperature_log.csv", mime="text/csv")
    else:
        st.info("ℹ️ No data yet. Click Start Monitoring.")

# Display Live Water Images
st.subheader("📸 Live Water Images")

image_folder = "live_images"  # Make sure this folder exists and has images

if os.path.exists(image_folder):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(valid_extensions)])
else:
    image_files = []

st.write("🗂️ Files in 'live_images' folder:", image_files)  # For debugging

if image_files:
    for img_file in image_files:
        try:
            img_path = os.path.join(image_folder, img_file)
            image = Image.open(img_path)
            st.image(image, caption=img_file, use_container_width=True)
        except Exception as e:
            st.warning(f"⚠️ Could not load {img_file}: {e}")
else:
    st.info("📁 No live images found. Please add images to the 'live_images/' folder.")

# Footer
st.markdown("---")
st.caption("🚀 Built with ❤️ by Vaishnavy Kassey | Smart Water Temp Monitor")
