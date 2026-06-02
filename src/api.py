from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Personal Finance & Investment Intelligence Platform",
        "status": "running"
    }

@app.get("/users")
def get_users():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    conn.close()

    return {"users": rows}

@app.get("/income")
def get_income():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM income")
    rows = cursor.fetchall()

    conn.close()

    return {"income": rows}

@app.get("/expenses")
def get_expenses():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    return {"expenses": rows}

@app.get("/investments")
def get_investments():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM investments")
    rows = cursor.fetchall()

    conn.close()

    return {"investments": rows}
@app.get("/financial-health")
def financial_health():

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    return {
    "total_income": total_income,
    "total_expenses": total_expenses,
    "savings": savings,
    "savings_rate": round(savings_rate, 2)
}

@app.get("/top-expenses")
def top_expenses():

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    ORDER BY SUM(amount) DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return {"top_expenses": rows}
@app.get("/budget-plan")
def budget_plan():

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM income")
    income = cursor.fetchone()[0] or 0

    recommended_budget = {
        "Needs (50%)": income * 0.50,
        "Wants (30%)": income * 0.30,
        "Savings (20%)": income * 0.20
    }

    conn.close()

    return recommended_budget
@app.get("/savings-forecast")
def savings_forecast():

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM income")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM expenses")
    expenses = cursor.fetchone()[0] or 0

    monthly_savings = income - expenses

    forecast = {
        "1_month": monthly_savings,
        "6_months": monthly_savings * 6,
        "12_months": monthly_savings * 12
    }

    conn.close()

    return forecast
@app.get("/dashboard")
def dashboard():

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM income")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM expenses")
    expenses = cursor.fetchone()[0] or 0

    cursor.execute("SELECT COUNT(*) FROM investments")
    investments = cursor.fetchone()[0] or 0

    savings = income - expenses

    conn.close()

    return {
        "total_income": income,
        "total_expenses": expenses,
        "total_savings": savings,
        "investment_count": investments
    }