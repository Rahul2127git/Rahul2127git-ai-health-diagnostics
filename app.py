import streamlit as st
import pandas as pd
import json
import fitz
from PIL import Image
import pytesseract

st.set_page_config(page_title="AI Health Diagnostics", layout="wide")

st.title("🩺 AI Health Diagnostics - Multi-Model Analysis")

# -----------------------------
# SIDEBAR - Patient Profile
# -----------------------------
st.sidebar.header("Patient Profile")

patient_name = st.sidebar.text_input("Full Name")
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
history = st.sidebar.text_area("Medical History / Symptoms")

uploaded_file = st.sidebar.file_uploader(
    "Upload Blood Report",
    type=["csv", "json", "pdf", "txt", "png", "jpg", "jpeg"],
    help="Supported formats: CSV, JSON, PDF, TXT, PNG, JPG"
)

run_button = st.sidebar.button("Run Diagnosis")

# -----------------------------
# MAIN EXECUTION
# -----------------------------
if run_button and uploaded_file is not None:

    file_type = uploaded_file.name.split(".")[-1].lower()

    # =============================
    # CSV
    # =============================
    if file_type == "csv":
        df = pd.read_csv(uploaded_file)

    # =============================
    # JSON
    # =============================
    elif file_type == "json":
        data = json.load(uploaded_file)
        df = pd.json_normalize(data)

    # =============================
    # PDF
    # =============================
    elif file_type == "pdf":
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()

        st.subheader("📄 Extracted PDF Text")
        st.write(text[:3000])
        st.stop()

    # =============================
    # IMAGE
    # =============================
    elif file_type in ["png", "jpg", "jpeg"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")

        extracted_text = pytesseract.image_to_string(image)

        st.subheader("🖼 Extracted Text from Image")
        st.write(extracted_text[:3000])
        st.stop()

    # =============================
    # TXT
    # =============================
    elif file_type == "txt":
        text = uploaded_file.read().decode("utf-8")
        st.subheader("📄 Extracted Text File")
        st.write(text[:3000])
        st.stop()

    else:
        st.error("Unsupported file type")
        st.stop()

    # =============================
    # DATA CLEANING
    # =============================
    df.fillna("Unknown", inplace=True)

    # =============================
    # MODEL 1 - Pattern Recognition
    # =============================
    def identify_pattern(condition, age):
        if condition in ["Diabetes", "Hypertension"] and age >= 45:
            return "Metabolic Syndrome Pattern"
        elif condition == "Cancer":
            return "Oncology Pattern"
        elif condition == "Asthma":
            return "Respiratory Pattern"
        elif condition == "Obesity":
            return "Lifestyle Disorder Pattern"
        else:
            return "General Health Pattern"

    df["Condition_Pattern"] = df.apply(
        lambda x: identify_pattern(x.get("Medical Condition", "Unknown"), age),
        axis=1
    )

    # =============================
    # MODEL 2 - Risk Assessment
    # =============================
    def assess_risk(age, condition):
        if age > 60 and condition in ["Diabetes", "Hypertension", "Cancer"]:
            return "Very High Risk"
        elif condition == "Cancer":
            return "High Risk"
        elif condition in ["Diabetes", "Hypertension"]:
            return "Moderate Risk"
        else:
            return "Low Risk"

    df["Risk_Level"] = df.apply(
        lambda x: assess_risk(age, x.get("Medical Condition", "Unknown")),
        axis=1
    )

    # =============================
    # MODEL 3 - Contextual Analysis
    # =============================
    def contextual_risk(age, gender, risk):
        if age >= 60 and risk in ["High Risk", "Very High Risk"]:
            return "Critical Risk (Age Factor)"
        if gender == "Male" and risk == "High Risk":
            return "Elevated Risk (Gender Factor)"
        return risk

    df["Contextual_Risk"] = df["Risk_Level"].apply(
        lambda x: contextual_risk(age, gender, x)
    )

    # =============================
    # RECOMMENDATION GENERATION
    # =============================
    def recommendation(condition):
        if condition == "Diabetes":
            return "Monitor glucose levels, balanced diet, regular exercise."
        elif condition == "Hypertension":
            return "Reduce salt intake, manage stress, regular BP monitoring."
        elif condition == "Cancer":
            return "Consult oncologist immediately."
        elif condition == "Asthma":
            return "Avoid allergens and use inhaler as prescribed."
        elif condition == "Obesity":
            return "Adopt weight management plan and healthy lifestyle."
        else:
            return "Maintain a healthy lifestyle and regular check-ups."

    df["Recommendation"] = df["Medical Condition"].apply(recommendation)

    # =============================
    # SYNTHESIS
    # =============================
    df["System_Conclusion"] = (
        "Health risks identified using a multi-model AI analytical approach."
    )

    df["Disclaimer"] = (
        "⚠️ This AI-generated health report is for educational purposes only "
        "and does not replace professional medical advice."
    )

    # =============================
    # DISPLAY RESULTS
    # =============================
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Clinical Interpretation")
        st.dataframe(df[["Medical Condition", "Risk_Level", "Contextual_Risk"]])

    with col2:
        st.subheader("🧠 Pattern & Risk Analysis")
        st.dataframe(df[["Condition_Pattern", "Risk_Level"]])

    st.markdown("---")

    st.subheader("💡 Health Summary")
    overall = df["Contextual_Risk"].value_counts().idxmax()
    st.success(f"Overall Risk Level: {overall}")

    st.subheader("📝 Actionable Recommendations")
    st.write(df["Recommendation"].unique())

    st.markdown("---")

    st.warning(df["Disclaimer"].iloc[0])

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Final Health Report",
        data=csv,
        file_name="final_health_report.csv",
        mime="text/csv"
    )

elif run_button:
    st.warning("Please upload a report before running diagnosis.")
    