import streamlit as st
from chatbot import ask_granite
from utils import generate_budget_summary, spending_insights, demographic_prompt

st.set_page_config(page_title="Personal Finance Chatbot", layout="centered")

st.title("💰 Personal Finance Chatbot")
st.write("Intelligent guidance for savings, taxes, and investments.")

# USER TYPE
user_type = st.radio("Select User Type:", ["Student", "Professional"])

# CHATBOT SECTION
st.subheader("🧠 Chatbot (AI Guidance)")
user_input = st.text_area("Ask something about savings, taxes or investments:")

if st.button("Ask Bot"):
    prompt = (
        demographic_prompt(user_type)
        + "\nProvide finance guidance.\nUser Question: "
        + user_input
    )
    answer = ask_granite(prompt)
    st.success(answer)

# BUDGET SUMMARY SECTION
st.subheader("📊 Budget Summary Generator")

income = st.number_input("Monthly Income (₹)", min_value=0, value=20000)

st.write("Enter Monthly Expenses:")
categories = ["Rent", "Food", "Transport", "Shopping", "Other"]
expenses = {}

for cat in categories:
    expenses[cat] = st.number_input(f"{cat} (₹)", min_value=0, value=0)

if st.button("Generate Budget Summary"):
    summary = generate_budget_summary(income, expenses)
    st.info(summary)

# SPENDING INSIGHTS
if st.button("Get Spending Insights"):
    insights = spending_insights(expenses)
    st.warning(insights)

st.caption("Powered by IBM Granite 3.3 2B Instruct Model")
