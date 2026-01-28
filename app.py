import streamlit as st

st.set_page_config(page_title="Worker Safety Risk System", page_icon="🦺")

st.title("🦺 Worker Safety Risk Assessment System")

st.write("Assess workplace risk based on basic safety parameters.")

# Inputs
temperature = st.slider("🌡️ Working Temperature (°C)", 20, 60, 30)
hours = st.slider("⏱️ Working Hours per Shift", 4, 16, 8)
ppe = st.selectbox("🦺 Is PPE being used?", ["Yes", "No"])

# Button
if st.button("Assess Risk"):
    risk_score = 0

    if temperature > 45:
        risk_score += 2
    elif temperature > 35:
        risk_score += 1

    if hours > 12:
        risk_score += 2
    elif hours > 8:
        risk_score += 1

    if ppe == "No":
        risk_score += 2

    # Result
    if risk_score >= 5:
        st.error("🔴 HIGH RISK: Immediate action required!")
    elif risk_score >= 3:
        st.warning("🟡 MEDIUM RISK: Improve safety conditions.")
    else:
        st.success("🟢 LOW RISK: Conditions are safe.")

