from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

# FastAPI App Initialization
app = FastAPI(
    title="PocketSmart AI",
    description="Your Smart Budget & Recommendation Engine",
    version="1.0.0"
)

# Request Data Model
class BudgetRequest(BaseModel):
    user_id: str
    monthly_income: float
    expenses: dict  # e.g., {"rent": 5000, "food": 3000}
    savings_goal: float

# Home Route
@app.get("/")
def read_root():
    return {
        "status": "Online",
        "project": "PocketSmart AI",
        "message": "Welcome to PocketSmart AI API!"
    }

# Health Check Route
@app.get("/health")
def health_check():
    return {"status": "Healthy", "database": "Connected"}

# Sample Budget Recommendation Route
@app.post("/api/v1/recommend-budget")
def recommend_budget(data: BudgetRequest):
    total_expenses = sum(data.expenses.values())
    remaining_balance = data.monthly_income - total_expenses
    
    if remaining_balance < 0:
        recommendation = "Warning: Your expenses exceed your income! Consider cutting non-essential costs."
    else:
        recommendation = f"Great! You have a surplus of ₹{remaining_balance}. Allocate some to your goal of ₹{data.savings_goal}."
        
    return {
        "user_id": data.user_id,
        "total_income": data.monthly_income,
        "total_expenses": total_expenses,
        "remaining_balance": remaining_balance,
        "recommendation": recommendation
    }
  @app.get("/")
def read_root():
    return {"message": "Welcome to PocketSmart AI API!"}

@app.post("/recommend")
def get_recommendation(request: BudgetRequest):
    total_expenses = sum(request.expenses.values())
    remaining = request.monthly_income - total_expenses
    
    status = "Good" if remaining >= request.savings_goal else "Needs Improvement"
    
    return {
        "user_id": request.user_id,
        "total_expenses": total_expenses,
        "remaining_balance": remaining,
        "status": status,
        "recommendation": "Try to save more on non-essential expenses." if remaining < request.savings_goal else "Great job staying within budget!"
    }
