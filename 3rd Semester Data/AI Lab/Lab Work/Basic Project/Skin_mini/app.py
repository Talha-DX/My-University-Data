import streamlit as st
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from PIL import Image
import json
import sqlite3
import datetime

# Page configuration
st.set_page_config(
    page_title="SkinScan Mini - AI Dermatology Assistant",
    page_icon="🩺",
    layout="wide"
)

# Load model and labels
@st.cache_resource
def load_model():
    model = keras.models.load_model('model/skin_classifier.h5')
    with open('model/class_labels.json', 'r') as f:
        class_labels = json.load(f)
    return model, class_labels

# Initialize database
def init_db():
    conn = sqlite3.connect('skinscan.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS diagnoses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  patient_id TEXT,
                  image_path TEXT,
                  prediction TEXT,
                  confidence REAL,
                  timestamp DATETIME)''')
    conn.commit()
    conn.close()

# Save diagnosis to database
def save_diagnosis(patient_id, img_path, prediction, confidence):
    conn = sqlite3.connect('skinscan.db')
    c = conn.cursor()
    c.execute('''INSERT INTO diagnoses 
                 (patient_id, image_path, prediction, confidence, timestamp)
                 VALUES (?, ?, ?, ?, ?)''',
              (patient_id, img_path, prediction, confidence, datetime.datetime.now()))
    conn.commit()
    conn.close()

# Preprocess uploaded image
def preprocess_image(image):
    img = np.array(image)
    if len(img.shape) == 2:  # Grayscale
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    elif img.shape[2] == 4:  # RGBA
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
    
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Main application
def main():
    st.title("🩺 SkinScan Mini - AI Dermatology Assistant")
    st.markdown("Upload a skin lesion image for AI-powered analysis")
    
    # Sidebar for patient info
    with st.sidebar:
        st.header("Patient Information")
        patient_id = st.text_input("Patient ID/Name", "P001")
        
        st.header("Previous Diagnoses")
        conn = sqlite3.connect('skinscan.db')
        history = conn.execute("SELECT * FROM diagnoses WHERE patient_id = ? ORDER BY timestamp DESC LIMIT 5", 
                               (patient_id,)).fetchall()
        conn.close()
        
        if history:
            for record in history:
                st.write(f"**{record[3]}** ({record[4]:.1%})")
                st.caption(f"{record[5][:16]}")
        else:
            st.info("No previous diagnoses")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader("Choose a skin lesion image", 
                                         type=['jpg', 'jpeg', 'png'])
        
        if uploaded_file is not None:
            # Display image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Process button
            if st.button("🔍 Analyze Image", type="primary"):
                with st.spinner("AI is analyzing..."):
                    # Load model
                    model, class_labels = load_model()
                    
                    # Preprocess and predict
                    processed_img = preprocess_image(image)
                    predictions = model.predict(processed_img, verbose=0)
                    
                    # Get top 3 predictions
                    top_indices = np.argsort(predictions[0])[-3:][::-1]
                    
                    # Display results
                    st.success("Analysis Complete!")
                    
                    # Show top prediction with confidence
                    top_class_idx = str(top_indices[0])
                    top_confidence = predictions[0][top_indices[0]]
                    
                    st.subheader(f"Primary Diagnosis: **{class_labels[top_class_idx]}**")
                    st.metric("Confidence", f"{top_confidence:.1%}")
                    
                    # Show progress bars for top 3
                    st.subheader("Top 3 Possibilities:")
                    for idx in top_indices:
                        label = class_labels[str(idx)]
                        confidence = predictions[0][idx]
                        st.progress(float(confidence), text=f"{label}: {confidence:.1%}")
                    
                    # Save to database
                    save_diagnosis(patient_id, uploaded_file.name, 
                                  class_labels[top_class_idx], float(top_confidence))
                    
                    # Show disclaimer (VERY IMPORTANT)
                    st.warning("""
                    ⚠️ **Medical Disclaimer**  
                    This tool is for educational purposes only.  
                    It is NOT a substitute for professional medical advice.  
                    Always consult a qualified dermatologist for actual diagnosis.
                    """)
                    
                    # Explanation of condition
                    st.subheader("About this condition:")
                    condition_info = {
                        'Melanocytic Nevus': 'Common mole, usually harmless but monitor for changes.',
                        'Melanoma': 'Serious skin cancer requiring immediate medical attention.',
                        'Basal Cell Carcinoma': 'Most common skin cancer, grows slowly, treatable.',
                        'Benign Keratosis': 'Non-cancerous skin growth, common in older adults.',
                        'Dermatofibroma': 'Harmless hard bump, often after insect bite.',
                        'Actinic Keratosis': 'Pre-cancerous from sun damage, should be monitored.',
                        'Vascular Lesion': 'Blood vessel abnormalities, usually benign.'
                    }
                    
                    diagnosis = class_labels[top_class_idx]
                    if diagnosis in condition_info:
                        st.info(condition_info[diagnosis])
    
    with col2:
        st.subheader("📋 Quick Guide")
        st.markdown("""
        1. **Enter patient ID** in sidebar
        2. **Upload clear image** of skin lesion
        3. **Click 'Analyze Image'**
        4. **Review AI diagnosis**
        5. **Consult dermatologist** for actual treatment
        
        **Best practices:**
        - Use good lighting
        - Include scale reference
        - Focus on lesion
        - Take multiple angles
        """)
        
        st.subheader("📊 Model Information")
        model, class_labels = load_model()
        st.write(f"**Classes:** {len(class_labels)} skin conditions")
        st.write(f"**Input:** 224×224 color images")
        st.write(f"**Training:** HAM10000 dataset")

# Initialize and run app
if __name__ == "__main__":
    init_db()
    main()