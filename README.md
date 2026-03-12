# Hospital-DB-Python-PostgreSQL-project
# Hospital Database Management System

A simple Python application that connects to a PostgreSQL database to manage and display hospital admission records, including patients, doctors, hospitals, tests, and admission types.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## Features

- Connects to PostgreSQL database using `psycopg2`
- Joins multiple tables to show complete admission information
- Displays data in a clean, formatted table in the terminal
- Includes sample data for 10 patients/admissions

## Project Structure
Database-project/
├── connect_db.py          # Main script to query and display data
├── database.sql           # SQL script to create tables + insert sample data
├── README.md              # This file
└── .venv/                 # (virtual environment - not committed)


## Prerequisites

- Python 3.8+
- PostgreSQL installed and running (on port 5433 in this example)
- `psycopg2` Python library (`pip install psycopg2-binary`)

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/SothSokhomal/Hospital-DB-Python-PostgreSQL-project.git
   cd https://github.com/SothSokhomal/Hospital-DB-Python-PostgreSQL-project.git