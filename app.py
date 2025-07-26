import streamlit as st
import time
import random
from PIL import Image

st.set_page_config(page_title="Smart Water Temperature Monitoring System", layout="centered")

st.title("🌊 Smart Water Temperature Monitoring System")

# Load water image
water_image = Image.open("images/water_live.jpg")  # Make sure you have this image in the images folder

# Placeholder for the temperature display
temp_placeholder = st.empty()

# Placeholder for the image with temperature overlay
image_placeholder = st.empty()

# Control buttons
start = st.button("Start Monitoring")
stop = st.button("Stop Monitoring")

# Session state to keep track of running status and temperature
if "running" not in st.session_state:
    st.session_state.running = False

if "temperature" not in st.session_state:
    st.session_state.temperature = 25.0  # initial temperature

if start:
    st.session_state.running = True
    st.success("Monitoring started...")

if stop:
    st.session_state.running = False
    st.warning("Monitoring stopped.")

def simulate_temperature():
    # Simulate temperature changes slightly
    new_temp = st.session_state.temperature + random.uniform(-0.3, 0.3)
    # Keep temp between 20 and 35 for realism
    new_temp = max(20, min(new_temp, 35))
    st.session_state.temperature = round(new_temp, 2)

def show_temperature_image(temp):
    # Display water image with floating temperature overlay using markdown + HTML
    html_code = f"""
    <div style="position: relative; width: 100%; max-width: 600px;">
        <img src="images/water_live.jpg" style="width: 100%; border-radius: 12px;"/>
ur image filename
try:
    img = Image.open(image_path)
    st.image(img, width=100)
except FileNotFoundError:
    st.warning(f"Image file '{image_path}' not found.")
except UnidentifiedImageError:
    st.warning(f"Cannot identify image file '{image_path}'. Please check the file.")

st.title("🌊 Smart Water Temperature Monitoring System")

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

# Use .get() to safely access session state
if st.session_state.get("monitoring", False):
    for _ in range(20):
        if not st.session_state.get("monitoring", False):
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

if not st.session_state.get("monitoring", False) and st.session_state.data:
    st.subheader("📊 Full Temperature Log")
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df, use_container_width=True)

    with open("data_temperature_log.csv", "rb") as f:
        st.download_button("⬇️ Download CSV", f, file_name="temperature_log.csv", mime="text/csv")
 image filename
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
