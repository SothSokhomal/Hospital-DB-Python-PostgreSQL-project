🏥 Hospital Database Management System (Python + PostgreSQL)

A simple Python project that connects to a PostgreSQL database to display hospital admission records, including patient details, assigned doctors, hospitals, test results, and admission types.

🔹 Features

Connects to PostgreSQL using psycopg2

Performs JOIN queries across multiple tables

Displays results in a clean, aligned table format in the terminal

Includes sample data for 10 patients and admissions

🔹 Project Structure
Hospital-DB-Python-PostgreSQL-project/
├── connect_db.py       # Main Python script to query and display data
├── database.sql        # SQL script: creates tables + inserts 10 sample records
├── README.md           # This file
└── .venv/              # Virtual environment (not committed)
🔹 Prerequisites

PostgreSQL installed via Stack Builder (EnterpriseDB)

Recommended version: 15 or 16

Default port: 5433 (change in code if using 5432)

Default user: postgres

Default password: 123 (⚠️ change for real use)

Python 3.8+

psycopg2 library

🔹 Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/SothSokhomal/Hospital-DB-Python-PostgreSQL-project.git
cd Hospital-DB-Python-PostgreSQL-project
2️⃣ Create & activate virtual environment

macOS / Linux

python -m venv .venv
source .venv/bin/activate

Windows

python -m venv .venv
.venv\Scripts\activate
3️⃣ Install required packages
pip install psycopg2-binary
4️⃣ Set up the database

Make sure PostgreSQL is running (via Stack Builder or Services)

Create the database

psql -U postgres -h localhost -p 5433 -c "CREATE DATABASE hospital_db;"

Create tables and insert sample data

psql -U postgres -h localhost -p 5433 -d hospital_db -f database.sql

You should see messages like CREATE TABLE and INSERT 0 10.

🔹 Run the Program
python connect_db.py

Expected Output (example)

Hospital Admission Data
─────────────────────────────────────────────────────────────────────────────
Patient        Doctor       Hospital              Test        Admission Type
─────────────────────────────────────────────────────────────────────────────
John Doe       Dr. Smith    Central Hospital     Blood Test  Emergency Admission
Jane Smith     Dr. Johnson  City Medical Center  X-Ray       Routine Checkup
...
─────────────────────────────────────────────────────────────────────────────
🔹 Important Notes

The project uses port 5433 by default.

If your PostgreSQL uses port 5432, update connect_db.py:

port="5433"  # change to 5432 if needed

⚠️ Security: Never use 123 as a password in production or on shared servers.

🔹 How to Contribute

Fork the repository

Create your branch:

git checkout -b feature/your-feature

Commit your changes:

git commit -m 'Add feature XYZ'

Push to your branch:

git push origin feature/your-feature

Open a Pull Request

Made with ❤️ by ByteBabe
Happy coding! 🚀