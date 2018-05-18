# SQL injection example

## Requirements
Python 3

## Setup
1. Create virtual environment: `python3 -m venv venv`
2. Activate virtual environment: `source venv/bin/activate` (Bash) or `./venv/Scripts/Activate.ps1` (PowerShell)
3. Install dependencies: `pip install -r requirements.txt`

## Run
1. Run `FLASK_APP=app.py python -m flask run` (Bash) or `$Env:FLASK_APP = 'app.py'; python -m flask run` (PowerShell)
2. Visit http://localhost:5000

## Try
Syntax: `username:password`

- Invalid credentials: `anything:anything`
- Valid credentials: `firstuser:firstpassword`, `jo:jospassword`, `ed:edspassword`
- SQL injection: `' or 1=1;--:anything`

View the application logs to see what SQL queries are being run.

Run `db.py` to see some example queries.
