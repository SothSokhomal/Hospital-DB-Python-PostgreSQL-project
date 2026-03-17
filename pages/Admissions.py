import streamlit as st
from utils import run_query, get_connection
import plotly.express as px

st.title("📋 Admissions Overview")

df = run_query("""
    SELECT 
        p.patient_name, d.doctor_name, h.hospital_name,
        t.test_name, a.admission_name
    FROM admission_tbl a
    JOIN patient_tbl p ON a.patient_id = p.patient_id
    JOIN doctor_tbl d ON a.doctor_id = d.doctor_id
    JOIN hospital_tbl h ON a.hospital_id = h.hospital_id
    JOIN testResult_tbl t ON a.test_id = t.test_id
    ORDER BY a.admission_id DESC
""")

col1, col2 = st.columns(2)
with col1:
    hospital = st.selectbox("Filter Hospital", ["All"] + sorted(df["hospital_name"].unique()))
with col2:
    doctor = st.selectbox("Filter Doctor", ["All"] + sorted(df["doctor_name"].unique()))

filtered = df
if hospital != "All": filtered = filtered[filtered["hospital_name"] == hospital]
if doctor != "All":   filtered = filtered[filtered["doctor_name"] == doctor]

st.dataframe(filtered, use_container_width=True, hide_index=True)

colA, colB = st.columns(2)
with colA:
    st.plotly_chart(px.bar(filtered, x="hospital_name", title="Admissions by Hospital"), use_container_width=True)
with colB:
    st.plotly_chart(px.pie(filtered, names="doctor_name", title="Admissions by Doctor"), use_container_width=True)

# Add New Admission
st.subheader("➕ Add New Admission")
with st.form("add_form"):
    patients = run_query("SELECT patient_id, patient_name FROM patient_tbl")
    doctors = run_query("SELECT doctor_id, doctor_name FROM doctor_tbl")
    hospitals = run_query("SELECT hospital_id, hospital_name FROM hospital_tbl")
    tests = run_query("SELECT test_id, test_name FROM testResult_tbl")

    pat = st.selectbox("Patient", patients["patient_name"])
    doc = st.selectbox("Doctor", doctors["doctor_name"])
    hos = st.selectbox("Hospital", hospitals["hospital_name"])
    tst = st.selectbox("Test", tests["test_name"])
    adm_name = st.text_input("Admission Type", "Emergency Admission")

    if st.form_submit_button("Add Admission"):
        p_id = patients[patients["patient_name"] == pat]["patient_id"].iloc[0]
        d_id = doctors[doctors["doctor_name"] == doc]["doctor_id"].iloc[0]
        h_id = hospitals[hospitals["hospital_name"] == hos]["hospital_id"].iloc[0]
        t_id = tests[tests["test_name"] == tst]["test_id"].iloc[0]

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO admission_tbl (admission_name, patient_id, doctor_id, hospital_id, test_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (adm_name, int(p_id), int(d_id), int(h_id), int(t_id)))
            conn.commit()
            st.success("Added successfully!")
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")