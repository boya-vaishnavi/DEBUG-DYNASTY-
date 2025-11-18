def generate_budget_summary(income, expenses):
    total_expenses = sum(expenses.values())
    savings = income - total_expenses

    summary = f"""
    Budget Summary:
    - Total Income: ₹{income}
    - Total Expenses: ₹{total_expenses}
    - Savings: ₹{savings}

    Expense Breakdown:
    """
    for k, v in expenses.items():
        summary += f"\n    • {k}: ₹{v}"

    return summary


def spending_insights(expenses):
    highest = max(expenses, key=expenses.get)
    insights = f"""
    Spending Insights:
    - You spend the most on **{highest}**.
    - Consider reducing unnecessary expenses in this category.
    - Track spending weekly to improve discipline.
    """
    return insights


def demographic_prompt(user_type):
    if user_type == "Student":
        return "Use simple, friendly, student-friendly tone."
    return "Use professional, concise tone suitable for working professionals."
