import psycopg2

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="hospital_db",
        user="postgres",
        password="123",
        port="5433"
    )

    print("Connected to PostgreSQL successfully!")

    # Create cursor
    cursor = conn.cursor()

    # Run query
    cursor.execute("""
    SELECT 
        p.patient_name,
        d.doctor_name,
        h.hospital_name,
        t.test_name,
        a.admission_name
    FROM admission_tbl a
    JOIN patient_tbl p ON a.patient_id = p.patient_id
    JOIN doctor_tbl d ON a.doctor_id = d.doctor_id
    JOIN hospital_tbl h ON a.hospital_id = h.hospital_id
    JOIN testResult_tbl t ON a.test_id = t.test_id;
    """)

    # Fetch all rows
    rows = cursor.fetchall()

    # ────────────────────────────────────────────────
    # Print nice table header
    print("\nHospital Admission Data")
    print("─" * 100)
    print(f"{'Patient':<20} {'Doctor':<20} {'Hospital':<25} {'Test':<20} {'Admission Type':<30}")
    print("─" * 100)

    # Print each row in table format
    for row in rows:
        patient, doctor, hospital, test, admission = row
        print(f"{patient:<20} {doctor:<20} {hospital:<25} {test:<20} {admission:<30}")

    print("─" * 100)

    # Clean up
    cursor.close()
    conn.close()

except Exception as e:
    print("Error:", e)