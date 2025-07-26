import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="💧 Smart Water Temperature Monitoring", layout="centered")
st.title("💧 Smart Water Temperature Monitoring System")

file_path = "data_temperature_log.csv"

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    try:
        df = pd.read_csv(file_path)
        if df.empty or "Temperature" not in df.columns:
            st.warning("CSV file is present but has no usable data.")
        else:
            st.line_chart(df["Temperature"])
            st.success("Data loaded and chart displayed!")
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
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
