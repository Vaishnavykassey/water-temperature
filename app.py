import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime
from PIL import Image, UnidentifiedImageError

# Initialize session state variables
if "monitoring" not in st.session_state:
    st.session_state.monitoring = False

if "data" not in st.session_state:
    st.session_state.data = []

# Set page title and layout
st.set_page_config(page_title="Smart Water Temperature Monitoring", layout="wide")

# Safe image loading
image_path = "assest_logo.png"  # Change this to your image filename
try:
    img = Image.open(image_path)
    st.image(img, width=100)
except FileNotFoundError:
    st.warning(f"Image file '{image_path}' not found.")
except UnidentifiedImageError:
    st.warning(f"Cannot identify image file '{image_path}'. Please check the file.")

st.title("🌊 Smart Water Temperature Monitoring System")

# Start/Stop buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ Start Monitoring"):
        st.session_state.monitoring = True
        st.success("Monitoring started!")

with col2:
    if st.button("⏹ Stop Monitoring"):
        st.session_state.monitoring = False
        st.warning("Monitoring stopped!")

placeholder = st.empty()

def simulate_sensor_data():
    return round(random.uniform(20.0, 40.0), 2)

# Monitoring loop
if st.session_state.monitoring:
    for _ in range(20):  # simulate 20 readings; adjust or remove this limit as needed
        if not st.session_state.monitoring:
            break

        temp = simulate_sensor_data()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        st.session_state.data.append({
            "Timestamp": now,
            "Temperature (°C)": temp
        })

        df = pd.DataFrame(st.session_state.data)
        placeholder.dataframe(df.tail(10), use_container_width=True)

        df.to_csv("data_temperature_log.csv", index=False)
        time.sleep(2)

# Show full log and download option when not monitoring
if not st.session_state.monitoring and st.session_state.data:
    st.subheader("📊 Full Temperature Log")
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df, use_container_width=True)

    with open("data_temperature_log.csv", "rb") as f:
        st.download_button("⬇️ Download CSV", f, file_name="temperature_log.csv", mime="text/csv")

col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ Start Monitoring"):
        st.session_state.monitoring = True
        st.success("Monitoring started!")

with col2:
    if st.button("⏹ Stop Monitoring"):
        st.session_state.monitoring = False
        st.warning("Monitoring stopped!")

# ✅ Realtime monitoring display
placeholder = st.empty()

def simulate_sensor_data():
    return round(random.uniform(20.0, 40.0), 2)

# ✅ Start the loop if monitoring is active
if st.session_state.monitoring:
    for _ in range(20):  # simulate 20 readings
        if not st.session_state.monitoring:
            break

        temp = simulate_sensor_data()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        st.session_state.data.append({
            "Timestamp": now,
            "Temperature (°C)": temp
        })

        df = pd.DataFrame(st.session_state.data)
        placeholder.dataframe(df.tail(10), use_container_width=True)

        df.to_csv("data_temperature_log.csv", index=False)
        time.sleep(2)

# ✅ Show full log after monitoring
if not st.session_state.monitoring and st.session_state.data:
    st.subheader("📊 Full Temperature Log")
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df, use_container_width=True)

    with open("data_temperature_log.csv", "rb") as f:
        st.download_button("⬇️ Download CSV", f, file_name="temperature_log.csv", mime="text/csv")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Start Monitoring"):
        st.session_state.monitoring = True
        st.success("Monitoring started!")

with col2:
    if st.button("Stop Monitoring"):
        st.session_state.monitoring = False
        st.warning("Monitoring stopped!")

# ✅ Simulate & Display Temperature Data
placeholder = st.empty()

def simulate_sensor_data():
    return round(random.uniform(20.0, 40.0), 2)

# ✅ Monitoring loop
if st.session_state.monitoring:
    for _ in range(20):
        if not st.session_state.monitoring:
            break

        temp = simulate_sensor_data()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        st.session_state.data.append({
            "Timestamp": now,
            "Temperature (°C)": temp
        })

        df = pd.DataFrame(st.session_state.data)
        placeholder.dataframe(df.tail(10), use_container_width=True)

        df.to_csv("data_temperature_log.csv", index=False)

        time.sleep(2)

# ✅ Display saved data
if not st.session_state.monitoring and st.session_state.data:
    st.subheader("Full Temperature Log")
    st.dataframe(pd.DataFrame(st.session_state.data), use_container_width=True)

    with open("data_temperature_log.csv", "rb") as f:
        st.download_button("Download CSV", f, file_name="temperature_log.csv", mime="text/csv")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Start Monitoring"):
        st.session_state.monitoring = True
        st.success("Monitoring started!")

with col2:
    if st.button("Stop Monitoring"):
        st.session_state.monitoring = False
        st.warning("Monitoring stopped!")

# ✅ Simulate & Display Temperature Data
placeholder = st.empty()

def simulate_sensor_data():
    # Random temperature between 20°C and 40°C
    return round(random.uniform(20.0, 40.0), 2)

# ✅ Continuous monitoring loop
if st.session_state.monitoring:
    for _ in range(20):  # You can increase or remove limit if needed
        if not st.session_state.monitoring:
            break

        current_temp = simulate_sensor_data()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        st.session_state.data.append({
            "Timestamp": current_time,
            "Temperature (°C)": current_temp
        })

        # Show updated data
        df = pd.DataFrame(st.session_state.data)
        placeholder.dataframe(df.tail(10), use_container_width=True)

        # Save data to CSV
        df.to_csv("data_temperature_log.csv", index=False)

        time.sleep(2)

# ✅ Show full data if monitoring is stopped
if not st.session_state.monitoring and st.session_state.data:
    st.subheader("Full Temperature Log")
    st.dataframe(pd.DataFrame(st.session_state.data), use_container_width=True)

    with open("data_temperature_log.csv", "rb") as f:
        st.download_button("Download CSV", f, file_name="temperature_log.csv", mime="text/csv")

else:
    st.warning("CSV file not found or is empty. Please upload or generate valid data.")

# Monitoring logic
if st.session_state.monitoring:
    temperature = get_water_temperature()
    timestamp = pd.Timestamp.now()

    # Append current reading
    st.session_state.data.append({"Timestamp": timestamp, "Temperature": temperature})

    # Show current temperature
    st.metric("🌡️ Current Water Temperature", f"{temperature} °C")

    # Alerts
    if temperature > 30:
        st.error("🔥 Alert: Temperature too high!")
    elif temperature < 24:
        st.warning("❄️ Warning: Temperature too low")
    else:
        st.success("✅ Temperature is normal")

    # Show temperature history chart
    df = pd.DataFrame(st.session_state.data)
    df.set_index("Timestamp", inplace=True)
    st.line_chart(df["Temperature"])

    # Small delay so UI doesn't freeze
    time.sleep(2)

    # Rerun the app to update live
    st.experimental_rerun()

else:
    st.info("Press ▶️ Start Monitoring to begin reading water temperature.")

    # If we have any data, show last readings and allow export
    if st.session_state.data:
        df = pd.DataFrame(st.session_state.data)
        df.set_index("Timestamp", inplace=True)

        st.subheader("📈 Temperature History")
        st.line_chart(df["Temperature"])

        # Show data table
        st.dataframe(df)

        # Export CSV
        csv = df.to_csv().encode('utf-8')
        st.download_button(
            label="⬇️ Download Temperature Log as CSV",
            data=csv,
            file_name='temperature_log.csv',
            mime='text/csv'
        )
