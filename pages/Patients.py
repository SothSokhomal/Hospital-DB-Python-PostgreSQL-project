import streamlit as st
from utils import run_query, get_connection
import pandas as pd 

st.set_page_config(page_title="Patients Management", layout="wide")

st.title("👥 Patients Management")

# ─── 1. ADD NEW ENTITIES (Condition, Medication, Insurance) ─────────────────
with st.expander("➕ Add New Metadata (Condition / Medication / Insurance)"):
    tab1, tab2, tab3 = st.tabs(["Condition", "Medication", "Insurance"])

    with tab1:
        new_cond = st.text_input("New Condition Name", key="nc")
        if st.button("Add Condition") and new_cond.strip():
            try:
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("INSERT INTO medicalCondition_tbl (condition_name) VALUES (%s)", (new_cond.strip(),))
                conn.commit()
                st.success(f"Added: {new_cond}")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

    with tab2:
        new_med = st.text_input("New Medication Name", key="nm")
        if st.button("Add Medication") and new_med.strip():
            try:
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("INSERT INTO medication_tbl (medication_name) VALUES (%s)", (new_med.strip(),))
                conn.commit()
                st.success(f"Added: {new_med}")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

    with tab3:
        new_ins = st.text_input("New Insurance Provider", key="ni")
        if st.button("Add Insurance") and new_ins.strip():
            try:
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("INSERT INTO insurance_tbl (provider_name) VALUES (%s)", (new_ins.strip(),))
                conn.commit()
                st.success(f"Added: {new_ins}")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()

# ─── 2. SEARCH PATIENTS ─────────────────────────────────────────────────────
search_term = st.text_input("🔍 Search patient name", "").strip()

query = """
    SELECT p.patient_id, p.patient_name, c.condition_name, m.medication_name, i.provider_name
    FROM patient_tbl p
    LEFT JOIN medicalCondition_tbl c ON p.condition_id = c.condition_id
    LEFT JOIN medication_tbl m ON p.medication_id = m.medication_id
    LEFT JOIN insurance_tbl i ON p.insurance_id = i.insurance_id
"""

if search_term:
    query += " WHERE p.patient_name ILIKE %s"
    # Using pd.read_sql with parameters
    df = pd.read_sql(query, get_connection(), params=(f"%{search_term}%",))
else:
    df = run_query(query)

st.caption(f"Showing {len(df)} patient(s)")

# ─── 3. DATA TABLE & EDITING ───────────────────────────────────────────────
if not df.empty:
    # Fetch options for dropdowns
    cond_options = [""] + sorted(run_query("SELECT condition_name FROM medicalCondition_tbl")["condition_name"].tolist())
    med_options = [""] + sorted(run_query("SELECT medication_name FROM medication_tbl")["medication_name"].tolist())
    ins_options = [""] + sorted(run_query("SELECT provider_name FROM insurance_tbl")["provider_name"].tolist())

    edited_df = st.data_editor(
        df,
        column_config={
            "patient_id": st.column_config.NumberColumn("ID", disabled=True),
            "patient_name": st.column_config.TextColumn("Name", required=True),
            "condition_name": st.column_config.SelectboxColumn("Condition", options=cond_options),
            "medication_name": st.column_config.SelectboxColumn("Medication", options=med_options),
            "provider_name": st.column_config.SelectboxColumn("Insurance", options=ins_options)
        },
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True,
        key="patient_editor"
    )

    if st.button("💾 Save All Changes", type="primary"):
        conn = get_connection()
        cur = conn.cursor()
        try:
            # 1. Handle Deletions (rows in df but not in edited_df)
            current_ids = edited_df['patient_id'].dropna().tolist()
            original_ids = df['patient_id'].tolist()
            deleted_ids = [idx for idx in original_ids if idx not in current_ids]
            
            for d_id in deleted_ids:
                cur.execute("DELETE FROM patient_tbl WHERE patient_id = %s", (int(d_id),))

            # 2. Handle Updates and New Rows
            for _, row in edited_df.iterrows():
                # Get IDs for the names selected in dropdowns
                c_id = None
                if row["condition_name"]:
                    res = run_query(f"SELECT condition_id FROM medicalCondition_tbl WHERE condition_name = '{row['condition_name']}'")
                    if not res.empty: c_id = int(res.iloc[0,0])
                
                m_id = None
                if row["medication_name"]:
                    res = run_query(f"SELECT medication_id FROM medication_tbl WHERE medication_name = '{row['medication_name']}'")
                    if not res.empty: m_id = int(res.iloc[0,0])

                i_id = None
                if row["provider_name"]:
                    res = run_query(f"SELECT insurance_id FROM insurance_tbl WHERE provider_name = '{row['provider_name']}'")
                    if not res.empty: i_id = int(res.iloc[0,0])

                if pd.isna(row["patient_id"]): # New row
                    cur.execute(
                        "INSERT INTO patient_tbl (patient_name, condition_id, medication_id, insurance_id) VALUES (%s,%s,%s,%s)",
                        (row["patient_name"], c_id, m_id, i_id)
                    )
                else: # Existing row update
                    cur.execute(
                        "UPDATE patient_tbl SET patient_name=%s, condition_id=%s, medication_id=%s, insurance_id=%s WHERE patient_id=%s",
                        (row["patient_name"], c_id, m_id, i_id, int(row["patient_id"]))
                    )
            
            conn.commit()
            st.success("Database Updated!")
            st.rerun()
        except Exception as e:
            conn.rollback()
            st.error(f"Failed to save: {e}")

# ─── 4. QUICK STATS ──────────────────────────────────────────────────────────
st.sidebar.header("Patient Statistics")
st.sidebar.write(f"Total Patients: {len(df)}")