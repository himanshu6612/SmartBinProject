import streamlit as st
import cv2
from model import predict_waste

st.title("♻️ Smart Bin AI")
st.write("Real-time Waste Classification System")

run = st.button("Start Camera")

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret:
        st.write("Failed to access camera")
        break
    
    # Show camera feed
    FRAME_WINDOW.image(frame, channels="BGR")
    
    # Predict waste type
    prediction = predict_waste(frame)
    
    st.subheader(f"🧠 Prediction: {prediction}")
    
camera.release()
