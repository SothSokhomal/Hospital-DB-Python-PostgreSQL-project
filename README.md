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

Made with ❤️ by ByteBabe
Happy coding! 🚀