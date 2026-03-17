import streamlit as st
from utils import run_query
import plotly.express as px

st.title("📊 Analytics")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Conditions")
    cond = run_query("""
        SELECT 
            c.condition_name, 
            COUNT(*) as count
        FROM patient_tbl p
        JOIN medicalCondition_tbl c ON p.condition_id = c.condition_id
        GROUP BY c.condition_name
        ORDER BY count DESC
    """)
    st.plotly_chart(px.pie(cond, names="condition_name", values="count", title="Condition Distribution"), use_container_width=True)

with col2:
    st.subheader("Medications")
    meds = run_query("""
        SELECT 
            m.medication_name, 
            COUNT(*) as count
        FROM patient_tbl p
        JOIN medication_tbl m ON p.medication_id = m.medication_id
        GROUP BY m.medication_name
        ORDER BY count DESC
    """)
    st.plotly_chart(px.bar(meds, x="medication_name", y="count", title="Most Prescribed Medications"), use_container_width=True)

# Extra chart
st.subheader("Admissions by Hospital")
adm = run_query("""
    SELECT 
        h.hospital_name, 
        COUNT(*) as total
    FROM admission_tbl a
    JOIN hospital_tbl h ON a.hospital_id = h.hospital_id
    GROUP BY h.hospital_name
""")
st.plotly_chart(px.bar(adm, x="hospital_name", y="total", title="Admissions per Hospital"), use_container_width=True)