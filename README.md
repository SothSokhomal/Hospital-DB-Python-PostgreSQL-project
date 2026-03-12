# Hospital Database Management System (Python + PostgreSQL)

A simple Python project that connects to a PostgreSQL database to display hospital admission records, including patient details, assigned doctors, hospitals, test results, and admission types.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## Features
- Connects to PostgreSQL using `psycopg2`
- Performs JOIN queries across multiple tables
- Displays results in a clean, aligned table format in the terminal
- Includes sample data for 10 patients and admissions

## Project Structure
Hospital-DB-Python-PostgreSQL-project/
├── connect_db.py       # Main Python script to query and display data
├── database.sql        # SQL script: creates tables + inserts 10 sample records
├── README.md           # This file
└── .venv/              # Virtual environment (not committed)
text## Prerequisites
- **PostgreSQL** installed via **PostgreSQL Stack Builder** (from EnterpriseDB)  
  - Recommended version: 15 or 16  
  - Port used in this project: **5433** (change in code if your installation uses 5432)  
  - Default user: `postgres`  
  - Password: `123` (please change this for real use!)

- Python 3.8+
- `psycopg2` library

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/SothSokhomal/Hospital-DB-Python-PostgreSQL-project.git
   cd Hospital-DB-Python-PostgreSQL-project

Create & activate virtual environmentBashpython -m venv .venv
source .venv/bin/activate          # macOS / Linux
# or on Windows: .venv\Scripts\activate
Install required packageBashpip install psycopg2-binary
Set up the database
(PostgreSQL must be running – started via Stack Builder or Services)
Create the database (if it doesn't exist):Bashpsql -U postgres -h localhost -p 5433 -c "CREATE DATABASE hospital_db;"
Create tables and insert sample data:Bashpsql -U postgres -h localhost -p 5433 -d hospital_db -f database.sqlYou should see many CREATE TABLE and INSERT 0 10 messages.

Run the programBashpython connect_db.py→ You should see a nicely formatted table with 10 records.

Example Output
textHospital Admission Data
────────────────────────────────────────────────────────────────────────────────────────────────────
Patient              Doctor               Hospital                  Test                 Admission Type                
────────────────────────────────────────────────────────────────────────────────────────────────────
John Doe             Dr. Smith            Central Hospital          Blood Test           Emergency Admission           
Jane Smith           Dr. Johnson          City Medical Center       X-Ray                Routine Checkup               
...
────────────────────────────────────────────────────────────────────────────────────────────────────
Important Notes

This project uses port 5433 (common when multiple PostgreSQL versions are installed via Stack Builder).
If your PostgreSQL is on port 5432, just change port="5433" → port="5432" in connect_db.py.
Security: Never use password 123 in production or on shared servers.

How to Contribute

Fork the repo
Create your branch (git checkout -b feature/your-feature)
Commit changes (git commit -m 'Add feature XYZ')
Push (git push origin feature/your-feature)
Open a Pull Request

Made by ByteBabe
Happy coding!