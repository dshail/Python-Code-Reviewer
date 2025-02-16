import os
import ast
import streamlit as st
import google.generativeai as genai

# Securely fetch API Key from environment variable
api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    st.error("🚨 API key is missing! Set 'GENAI_API_KEY' as an environment variable.")
    st.stop()

genai.configure(api_key=api_key)

# System instruction for AI
system_prompt = """You are an advanced Python code reviewer. Your task is to:
- Identify errors in the given Python code.
- Categorize issues as Syntax, Logic, or Performance-related.
- Suggest improvements or optimizations.
- Provide an overall rating (out of 5) based on code quality.
- Output the response in a structured format."""

# Initialize Gemini AI
gemini = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

# Streamlit UI
st.title("🚀 Python Code Reviewer with Gemini AI")
st.markdown("### 📝 Paste your Python code below:")
user_prompt = st.text_area("📌 Enter your Python code:", height=250)

# Syntax validation function
def is_valid_python_code(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

# Process user input
if st.button("🔍 Review Code"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a Python code snippet first.")
    elif not is_valid_python_code(user_prompt):
        st.error("🚨 Invalid Python code! Please check for syntax errors.")
    else:
        with st.spinner("🔎 Analyzing your code..."):
            response = gemini.generate_content(user_prompt)
        
        # Display AI Review
        st.subheader("✅ AI Review:")
        st.write(response.text)

        # Extract rating if available
        if "Rating:" in response.text:
            rating = response.text.split("Rating:")[-1].strip().split("\n")[0]
            st.subheader(f"⭐ Code Quality Rating: {rating}/5")

        # Suggested improvements
        if "Suggested Improvements:" in response.text:
            st.subheader("💡 Suggested Improvements:")
            suggestions = response.text.split("Suggested Improvements:")[-1].strip()
            st.write(suggestions)
