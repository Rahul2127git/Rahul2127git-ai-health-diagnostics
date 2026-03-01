import streamlit as st
import pandas as pd
import json
import fitz
from PIL import Image
import pytesseract
<<<<<<< HEAD
import plotly.express as px
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
=======
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4

st.set_page_config(page_title="AI Health Diagnostics", layout="wide")

st.title("🩺 AI Health Diagnostics - Multi-Model Analysis")

<<<<<<< HEAD
# =============================
# SIDEBAR - PATIENT PROFILE
# =============================
=======
# -----------------------------
# SIDEBAR - Patient Profile
# -----------------------------
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
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

<<<<<<< HEAD
# =============================
# MAIN EXECUTION
# =============================
=======
# -----------------------------
# MAIN EXECUTION
# -----------------------------
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
if run_button and uploaded_file is not None:

    file_type = uploaded_file.name.split(".")[-1].lower()

<<<<<<< HEAD
    # ===== CSV =====
    if file_type == "csv":
        df = pd.read_csv(uploaded_file)

    # ===== JSON =====
=======
    # =============================
    # CSV
    # =============================
    if file_type == "csv":
        df = pd.read_csv(uploaded_file)

    # =============================
    # JSON
    # =============================
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
    elif file_type == "json":
        data = json.load(uploaded_file)
        df = pd.json_normalize(data)

<<<<<<< HEAD
    # ===== PDF =====
=======
    # =============================
    # PDF
    # =============================
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
    elif file_type == "pdf":
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
<<<<<<< HEAD
=======

>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
        st.subheader("📄 Extracted PDF Text")
        st.write(text[:3000])
        st.stop()

<<<<<<< HEAD
    # ===== IMAGE =====
    elif file_type in ["png", "jpg", "jpeg"]:
        image = Image.open(uploaded_file)
        st.image(image)
        extracted_text = pytesseract.image_to_string(image)
        st.subheader("🖼 Extracted Text")
        st.write(extracted_text[:3000])
        st.stop()

    # ===== TXT =====
=======
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
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
    elif file_type == "txt":
        text = uploaded_file.read().decode("utf-8")
        st.subheader("📄 Extracted Text File")
        st.write(text[:3000])
        st.stop()

    else:
        st.error("Unsupported file type")
        st.stop()

<<<<<<< HEAD
=======
    # =============================
    # DATA CLEANING
    # =============================
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
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

<<<<<<< HEAD
    df["Condition_Pattern"] = df["Medical Condition"].apply(
        lambda x: identify_pattern(x, age)
=======
    df["Condition_Pattern"] = df.apply(
        lambda x: identify_pattern(x.get("Medical Condition", "Unknown"), age),
        axis=1
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
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

<<<<<<< HEAD
    df["Risk_Level"] = df["Medical Condition"].apply(
        lambda x: assess_risk(age, x)
=======
    df["Risk_Level"] = df.apply(
        lambda x: assess_risk(age, x.get("Medical Condition", "Unknown")),
        axis=1
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
    )

    # =============================
    # MODEL 3 - Contextual Analysis
    # =============================
    def contextual_risk(age, gender, risk):
<<<<<<< HEAD
        if age >= 60 and "High" in risk:
=======
        if age >= 60 and risk in ["High Risk", "Very High Risk"]:
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
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
<<<<<<< HEAD
            return "Monitor glucose levels and maintain balanced diet."
        elif condition == "Hypertension":
            return "Reduce salt intake and monitor BP regularly."
        elif condition == "Cancer":
            return "Consult oncologist immediately."
        elif condition == "Asthma":
            return "Avoid allergens and use inhaler."
        elif condition == "Obesity":
            return "Adopt healthy lifestyle and exercise."
        else:
            return "Maintain regular health check-ups."
=======
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
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4

    df["Recommendation"] = df["Medical Condition"].apply(recommendation)

    # =============================
<<<<<<< HEAD
    # DASHBOARD METRICS
    # =============================
    st.markdown("## 📊 Health Overview")

    col1, col2, col3 = st.columns(3)

    total_records = len(df)
    high_risk = len(df[df["Contextual_Risk"].str.contains("High")])
    low_risk = len(df[df["Contextual_Risk"].str.contains("Low")])

    col1.metric("Total Records", total_records)
    col2.metric("High Risk Cases", high_risk)
    col3.metric("Low Risk Cases", low_risk)

    # =============================
    # CHARTS
    # =============================
    st.markdown("## 📈 Risk Distribution")

    risk_counts = df["Contextual_Risk"].value_counts().reset_index()
    risk_counts.columns = ["Risk Level", "Count"]

    fig1 = px.pie(risk_counts, names="Risk Level", values="Count")
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("## 🏥 Condition Frequency")

    condition_counts = df["Medical Condition"].value_counts().reset_index()
    condition_counts.columns = ["Condition", "Count"]

    fig2 = px.bar(condition_counts, x="Condition", y="Count", color="Condition")
    st.plotly_chart(fig2, use_container_width=True)

    # =============================
    # AI CLINICAL INTERPRETATION
    # =============================
    st.markdown("## 🤖 AI Clinical Interpretation")

    def generate_ai_summary(df):
        high = len(df[df["Contextual_Risk"].str.contains("High")])
        moderate = len(df[df["Contextual_Risk"].str.contains("Moderate")])
        low = len(df[df["Contextual_Risk"].str.contains("Low")])

        return f"""
        The multi-model AI system analyzed the uploaded health dataset.
        {high} high-risk cases, {moderate} moderate-risk cases,
        and {low} low-risk cases were identified.
        Higher risk cases require medical consultation and lifestyle monitoring.
        """

    ai_summary = generate_ai_summary(df)

    st.info(ai_summary)

    # =============================
    # PDF REPORT GENERATION
    # =============================
    def generate_pdf_report(df, summary):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []
        styles = getSampleStyleSheet()

        elements.append(Paragraph("AI Health Diagnostics Report", styles["Heading1"]))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph(summary, styles["Normal"]))
        elements.append(Spacer(1, 0.5 * inch))

        table_data = [df.columns.tolist()] + df.head(10).values.tolist()
        table = Table(table_data)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black)
        ]))

        elements.append(table)
        doc.build(elements)
        buffer.seek(0)
        return buffer

    st.markdown("## 📄 Download Professional Report")

    pdf_file = generate_pdf_report(df, ai_summary)

    st.download_button(
        label="Download PDF Report",
        data=pdf_file,
        file_name="AI_Health_Report.pdf",
        mime="application/pdf"
    )

    # CSV download
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV Report",
=======
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
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
        data=csv,
        file_name="final_health_report.csv",
        mime="text/csv"
    )

<<<<<<< HEAD
    st.warning("⚠ This AI-generated report is for educational purposes only and does not replace professional medical advice.")

elif run_button:
    st.warning("Please upload a report before running diagnosis.")
=======
elif run_button:
    st.warning("Please upload a report before running diagnosis.")
    
>>>>>>> 8c585a7a20bbfe16183f63164142e4d33d2e97f4
